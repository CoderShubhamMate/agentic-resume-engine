#!/usr/bin/env python3
"""
match_resume.py - JD-vs-Master_Data / JD-vs-Resume matching tool.

Usage:
  python match_resume.py --mode pre|post --folder "<Company> - <Job Title>"
  OR explicit paths:
  python match_resume.py --mode pre|post --jd <path> --master-dir <dir>
      [--resume <path>] --title "..." --out-dir <dir>
      [--threshold 90] [--fit-floor 60] [--baseline <job-match-baseline.json>]
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import jobmatch

# ---------------------------------------------------------------------------
# A1. JD GUARD
# ---------------------------------------------------------------------------
JD_GUARD_FILENAME = re.compile(r"(?i)prompt\.md$")
JD_GUARD_CONTENT  = re.compile(r"SOURCE OF TRUTH|Never invent", re.I)

def guard_jd(jd_path, jd_text):
    if JD_GUARD_FILENAME.search(str(jd_path)):
        print("ERROR: The JD file appears to be a prompt/instruction file (filename matches 'prompt.md').\n"
              "       Run the matcher only on 'job-description.md', not on prompt.md.", file=sys.stderr)
        sys.exit(2)
    if JD_GUARD_CONTENT.search(jd_text):
        print("ERROR: The JD text contains instruction phrases ('SOURCE OF TRUTH' or 'Never invent').\n"
              "       This looks like a prompt file, not a real job description. Aborting.", file=sys.stderr)
        sys.exit(2)

# ---------------------------------------------------------------------------
# A4. MASTER_DATA LOADER with section-heading tracking and ignore-line filter
# ---------------------------------------------------------------------------
IGNORE_PATTERN = re.compile(
    r"\b(not verified|unverified|do not|never|learning|planned|want to|interested in)\b", re.I
)

SECTION_MAP = {
    "skills": "skills", "technolog": "skills",
    "experience": "experience", "work": "experience", "intern": "experience",
    "project": "projects",
    "certif": "certification", "education": "education",
    "summary": "summary", "about": "summary", "background": "summary", "profile": "summary",
}

def _heading_section(heading_text):
    low = heading_text.lower()
    for kw, sec in SECTION_MAP.items():
        if kw in low:
            return sec
    return "other"

def load_master_data(master_dir):
    """
    Returns:
      lines        – list of (fname, lineno, content, section)
      ignored_lines – list of {"file": fname, "line": lineno, "content": text}
    """
    lines, ignored = [], []
    p = Path(master_dir)
    md_files = sorted(p.glob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"No .md files found in master directory: {master_dir}")

    for mf in md_files:
        current_section = "other"
        with open(mf, "r", encoding="utf-8", errors="ignore") as f:
            for i, raw in enumerate(f, 1):
                clean = raw.strip()
                if not clean:
                    continue
                # Detect markdown headings
                if clean.startswith("#"):
                    current_section = _heading_section(clean.lstrip("#").strip())
                    continue
                # Detect bold section labels like "## Skills & Technologies"
                if clean.startswith("**") and clean.endswith("**") and len(clean) < 80:
                    current_section = _heading_section(clean.strip("*"))
                    continue
                if IGNORE_PATTERN.search(clean):
                    ignored.append({"file": mf.name, "line": i, "content": clean[:160]})
                    continue
                lines.append((mf.name, i, clean, current_section))
    return lines, ignored

# ---------------------------------------------------------------------------
# A4. EVIDENCE TIERS
# ---------------------------------------------------------------------------
SECTION_PRIORITY = {"skills": 0, "experience": 1, "projects": 2,
                    "certification": 3, "education": 4, "summary": 5, "other": 6}

def _usage_tier(best_section):
    if best_section in ("skills", "experience", "projects"):
        return "strong"
    if best_section in ("certification", "education"):
        return "cert_only"
    return "summary_only"

def find_best_evidence(pattern, master_lines):
    """
    Return (evidence_str, section, usage_tier) or (None, None, None).
    Prefers skills/experience/projects over summary/other.
    """
    best = None  # (priority, fname, lineno, content, section)
    for fname, lno, content, section in master_lines:
        if not pattern.search(content):
            continue
        pri = SECTION_PRIORITY.get(section, 99)
        if best is None or pri < best[0]:
            best = (pri, fname, lno, content, section)
    if best is None:
        return None, None, None
    _, fname, lno, content, section = best
    ev = f"{fname}:{lno} {content[:160].strip()}"
    return ev, section, _usage_tier(section)

# ---------------------------------------------------------------------------
# A6. LONGEST-MATCH-WINS deduplication
# ---------------------------------------------------------------------------
def deduplicate_by_longest(skills_dict):
    """
    If a longer canonical name matches a span, remove the shorter sub-name.
    E.g. if 'react native' is in the dict, drop 'react' from it.
    """
    canonicals = list(skills_dict.keys())
    to_remove = set()
    for longer in canonicals:
        for shorter in canonicals:
            if shorter == longer:
                continue
            # shorter is a proper sub-phrase of longer
            if re.search(r'\b' + re.escape(shorter) + r'\b', longer, re.I):
                to_remove.add(shorter)
    return {k: v for k, v in skills_dict.items() if k not in to_remove}

# ---------------------------------------------------------------------------
# A3/A5. CLASSIFY SKILLS with evidence tiers and longest-match dedup
# ---------------------------------------------------------------------------
def classify_skills(hard_skills, master_lines):
    verified, true_gaps = [], []

    # Apply longest-match dedup across the skills dict being tested
    # (hard_skills is already filtered from the JD, so just process as-is)
    seen_spans = set()  # canonical names already consumed by a longer match

    # Sort by length of name descending so longer matches are processed first
    sorted_skills = sorted(hard_skills, key=lambda h: len(h["name"]), reverse=True)

    for h in sorted_skills:
        name = h["name"]
        # Check if this name is a sub-phrase of an already-matched longer name
        already_covered = any(
            re.search(r'\b' + re.escape(name) + r'\b', longer, re.I)
            for longer in seen_spans
        )
        if already_covered:
            # Still classify for completeness but mark as deduplicated
            continue

        aliases = jobmatch.SKILLS.get(name, [])
        pat = jobmatch.term_pattern([name] + aliases)
        ev, section, tier = find_best_evidence(pat, master_lines)
        priority = "Required" if h.get("required") else "Nice-to-have" if h.get("nice") else "Normal"

        item = {
            "name": name,
            "priority": priority,
            "jd_count": h.get("jd_count", 0),
            "found_in_resume": h.get("found", False),
        }

        if ev:
            item["evidence"] = ev
            item["evidence_section"] = section
            item["usage_tier"] = tier
            verified.append(item)
            seen_spans.add(name)
        else:
            true_gaps.append(item)

    return verified, true_gaps

# ---------------------------------------------------------------------------
# A7. FABRICATION CHECK: skills in resume but not in Master_Data
# ---------------------------------------------------------------------------
def fabrication_check(resume_text, master_lines):
    # Strip 'Areas of Interest' section before checking for unverified skills
    # to avoid false-positive fabrication warnings on declared learning interests
    clean_text = re.split(r"(?i)\b(areas\s+of\s+interest|interests)\b", resume_text, maxsplit=1)[0]
    unverified = []
    for canon, aliases in jobmatch.SKILLS.items():
        pat = jobmatch.term_pattern([canon] + aliases)
        if not pat.search(clean_text):
            continue
        # Found in resume – is it in Master_Data?
        ev, _, _ = find_best_evidence(pat, master_lines)
        if not ev:
            unverified.append(canon)
    return unverified

# ---------------------------------------------------------------------------
# A3. VERDICT + REASONS + MAX_HONEST_SCORE
# ---------------------------------------------------------------------------
def compute_verdict(score, threshold, fit_floor):
    if score >= threshold:
        return "good_fit"
    if score >= fit_floor:
        return "acceptable_fit"
    return "weak_fit"

def compute_reasons(result, verified_omitted, true_gaps, threshold, fit_floor):
    reasons = []
    req_gaps = [g["name"] for g in true_gaps if g["priority"] == "Required"]
    if req_gaps:
        reasons.append(f"Required skills missing from Master_Data: {', '.join(req_gaps)}")

    for comp_name, val in result["comp"].items():
        if val is not None and val < 0.5:
            if comp_name == "Experience years" and result.get("need_years"):
                reasons.append(
                    f"Experience years: JD asks {result['need_years']}+, "
                    f"resume shows {result['resume_years']}"
                )
            else:
                reasons.append(f"{comp_name}: only {round(val*100)}% (below 50%)")

    failing = [c[0] for c in result["checks"] if not c[1]]
    for f in failing:
        reasons.append(f"ATS check failing: {f}")

    return reasons

def compute_max_honest_score(result, verified_omitted):
    """Recompute overall as if all verified_omitted skills were found."""
    import copy, math
    fake_hard = copy.deepcopy(result["hard"])
    omitted_names = {v["name"] for v in verified_omitted}
    for h in fake_hard:
        if h["name"] in omitted_names:
            h["found"] = True
            h["resume_count"] = 1

    wsum = lambda rows, f: (
        sum(r["weight"] * f(r) for r in rows) / sum(r["weight"] for r in rows)
        if rows else None
    )
    fake_hard_score = wsum(fake_hard, lambda r: r["found"])
    comp = dict(result["comp"])
    if fake_hard_score is not None:
        comp["Hard skills"] = fake_hard_score

    live = {k: v for k, v in comp.items() if v is not None}
    if not live:
        return result["overall"]
    total = 100 * sum(jobmatch.WEIGHTS[k] * v for k, v in live.items()) / sum(jobmatch.WEIGHTS[k] for k in live)
    return round(total)

# ---------------------------------------------------------------------------
# A9. JOB-MATCH-SUMMARY.MD
# ---------------------------------------------------------------------------
def write_summary_md(out_dir, title, verdict, score, threshold, comp, result,
                     verified_omitted, true_gaps, unverified_in_resume,
                     max_honest_score, baseline_data=None):
    lines = [
        f"# Job Match Summary — {title}",
        f"_Generated: {datetime.date.today()}_",
        "",
        "## 1. Verdict and Score",
    ]
    if baseline_data:
        lines.append(f"- Baseline score: {baseline_data.get('score', '?')}%")
        lines.append(f"- Final score:    {score}%  ({verdict.replace('_', ' ').title()})")
    else:
        lines.append(f"- Score: {score}% ({verdict.replace('_', ' ').title()})")
    lines.append(f"- Threshold: {threshold}%")
    lines += ["", "## 2. Score by Component"]
    for k, v in comp.items():
        val = "N/A" if v is None else f"{round(v*100)}%"
        lines.append(f"- {k} ({jobmatch.WEIGHTS[k]}%): {val}")

    lines += ["", "## 3. Keywords Added in Revisions"]
    if baseline_data and verified_omitted:
        baseline_omit = {v["name"] for v in baseline_data.get("verified_omitted", [])}
        added = [v for v in verified_omitted if v["name"] not in baseline_omit and v["found_in_resume"]]
        if added:
            lines.append("| Skill | Usage Tier | Evidence |")
            lines.append("|---|---|---|")
            for a in added:
                lines.append(f"| {a['name']} | {a.get('usage_tier','?')} | {a.get('evidence','?')} |")
        else:
            lines.append("_(none added yet — revision not yet run)_")
    else:
        lines.append("_(no baseline provided — first run)_")

    lines += ["", "## 4. Other Changes Made for This Job", ""]

    lines += ["", "## 5. Honest Gaps"]
    for g in true_gaps:
        prefix = "Mandatory requirement gap" if g["priority"] == "Required" else "Preferred gap"
        lines.append(f"- {prefix}: {g['name']}")
    if unverified_in_resume:
        lines.append("")
        lines.append("**⚠ Skills in resume NOT supported by Master_Data (remove):**")
        for u in unverified_in_resume:
            lines.append(f"  - {u}")

    if verdict == "weak_fit":
        lines += ["", "## 6. Why This Is a Weak Match"]
        lines.append(f"Score {score}% is below the weak-fit floor of 60%.")
        lines.append(f"Estimated ceiling with all truthful additions: {max_honest_score}%.")
        req_gaps = [g["name"] for g in true_gaps if g["priority"] == "Required"]
        if req_gaps:
            lines.append(f"Required skills with no Master_Data evidence: {', '.join(req_gaps)}.")
        lines.append("Delivering the best truthful resume per rule file Section 14.")

    out_path = Path(out_dir) / "job-match-summary.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="JD-vs-Resume matching tool")
    parser.add_argument("--mode", choices=["pre", "post"], required=True)
    parser.add_argument("--folder", help="'<Company> - <Job Title>' shorthand")
    parser.add_argument("--jd", help="Path to job-description.md")
    parser.add_argument("--master-dir", default="Master_Data")
    parser.add_argument("--resume", help="Path to resume.pdf (post mode)")
    parser.add_argument("--title")
    parser.add_argument("--out-dir")
    parser.add_argument("--threshold", type=int, default=90,
                        help="Good-fit threshold (default 90)")
    parser.add_argument("--fit-floor", type=int, default=60,
                        help="Acceptable-fit floor; below this is weak_fit (default 60)")
    parser.add_argument("--baseline", help="Path to a previous job-match.json for before/after comparison")
    args = parser.parse_args()

    # --folder shorthand
    if args.folder:
        folder_path = Path(args.folder).resolve()
        folder_name = folder_path.name
        default_title = folder_name.split(" - ", 1)[1] if " - " in folder_name else folder_name
        args.jd      = args.jd      or str(folder_path / "job-description.md")
        args.title   = args.title   or default_title
        args.out_dir = args.out_dir or str(folder_path)
        if args.mode == "post":
            args.resume = args.resume or str(folder_path / "resume.pdf")

    out_dir = Path(args.out_dir or ".").resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Merge skills_extra.json
    skills_extra_path = TOOLS_DIR / "skills_extra.json"
    if skills_extra_path.exists():
        with open(skills_extra_path, encoding="utf-8") as f:
            jobmatch.SKILLS.update(json.load(f))

    # Validate + load JD
    if not args.jd or not Path(args.jd).exists():
        print(f"Error: JD file not found: {args.jd}", file=sys.stderr); sys.exit(1)
    jd_text = jobmatch.read_text(args.jd).strip()
    if not jd_text:
        print(f"Error: JD file is empty: {args.jd}", file=sys.stderr); sys.exit(1)

    # A1 GUARD
    guard_jd(args.jd, jd_text)

    master_lines, ignored_lines = load_master_data(args.master_dir)
    target_title = args.title or next((l.strip() for l in jd_text.splitlines() if l.strip()), "")

    # Load baseline if given
    baseline_data = None
    if args.baseline and Path(args.baseline).exists():
        with open(args.baseline, encoding="utf-8") as f:
            baseline_data = json.load(f)

    # -------------------------------------------------------------------------
    if args.mode == "pre":
        jd_wlines = jobmatch.jd_weighted_lines(jd_text)
        hard_skills = jobmatch.analyse_dictionary(jd_wlines, "", jobmatch.SKILLS)
        verified, true_gaps = classify_skills(hard_skills, master_lines)

        payload = {
            "title": target_title,
            "total_jd_hard_skills": len(hard_skills),
            "verified_count": len(verified),
            "true_gap_count": len(true_gaps),
            "verified": verified,
            "true_gaps": true_gaps,
            "ignored_lines": ignored_lines,
        }
        out_path = out_dir / "jd-keywords.json"
        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

        print(f"\n=== PRE-MODE KEYWORD ANALYSIS ===")
        print(f"Target Title : {target_title}")
        print(f"JD Hard Skills     : {len(hard_skills)}")
        print(f"Verified in Master : {len(verified)}")
        print(f"True Gaps          : {len(true_gaps)}")
        if ignored_lines:
            print(f"Ignored lines      : {len(ignored_lines)} (see jd-keywords.json)")
        print()
        print("--- Verified Skills (safe to emphasize) ---")
        for v in verified:
            tier = v.get("usage_tier", "?")
            print(f"[{v['priority']}] {v['name']}  tier={tier}  (JD mentions: {v['jd_count']})")
            print(f"    {v['evidence']}")
        print()
        print("--- True Gaps (DO NOT ADD) ---")
        for g in true_gaps:
            print(f"[{g['priority']}] {g['name']}  (JD mentions: {g['jd_count']})")
        print(f"\nWritten: {out_path}")

    # -------------------------------------------------------------------------
    elif args.mode == "post":
        if not args.resume or not Path(args.resume).exists():
            print(f"Error: Resume not found: {args.resume}", file=sys.stderr); sys.exit(1)

        resume_path = Path(args.resume)
        pages = 0
        if resume_path.suffix.lower() == ".pdf":
            import pdfplumber
            try:
                with pdfplumber.open(resume_path) as pdf:
                    pages = len(pdf.pages)
            except Exception as e:
                print(f"Warning: page count failed: {e}", file=sys.stderr)

        resume_text = jobmatch.read_text(str(resume_path)).strip()
        if len(resume_text) < 100:
            print(f"Error: Resume text too short ({len(resume_text)} chars) – image PDF?",
                  file=sys.stderr); sys.exit(1)

        result = jobmatch.analyse(resume_text, jd_text, target_title)
        verified, true_gaps = classify_skills(result["hard"], master_lines)
        verified_omitted = [v for v in verified if not v["found_in_resume"]]

        # A7 fabrication check
        unverified_in_resume = fabrication_check(resume_text, master_lines)
        has_unverified = bool(unverified_in_resume)

        # A3 extras
        score        = result["overall"]
        threshold    = args.threshold
        fit_floor    = args.fit_floor
        verdict      = compute_verdict(score, threshold, fit_floor)
        reasons      = compute_reasons(result, verified_omitted, true_gaps, threshold, fit_floor)
        max_honest   = compute_max_honest_score(result, verified_omitted)
        needs_revision = score < threshold and bool(verified_omitted) and pages == 1

        missing_kws    = [k["name"] for k in result["kws"] if not k["found"]]
        failing_checks = [c[0] for c in result["checks"] if not c[1]]

        # Assemble JSON
        payload = {
            "score": score,
            "threshold": threshold,
            "fit_floor": fit_floor,
            "verdict": verdict,
            "reasons": reasons,
            "max_honest_score": max_honest,
            "pages": pages,
            "needs_revision": needs_revision,
            "has_unverified": has_unverified,
            "comp": result["comp"],
            "verified": verified,
            "verified_omitted": verified_omitted,
            "true_gaps": true_gaps,
            "unverified_in_resume": unverified_in_resume,
            "missing_keywords": missing_kws,
            "failing_checks": failing_checks,
            "recommendations": jobmatch.recommendations(result),
        }

        # Add baseline delta
        if baseline_data:
            payload["baseline_score"] = baseline_data.get("score")
            payload["score_delta"] = score - baseline_data.get("score", score)
            baseline_omit = {v["name"] for v in baseline_data.get("verified_omitted", [])}
            payload["skills_added_in_revisions"] = [
                v for v in verified
                if v["found_in_resume"] and v["name"] not in baseline_omit
            ]

        json_path = out_dir / "job-match.json"
        json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

        # PDF report
        result["pages"] = pages
        result["threshold"] = threshold
        result["verified"] = verified
        result["verified_omitted"] = verified_omitted
        result["true_gaps"] = true_gaps
        result["unverified_in_resume"] = unverified_in_resume
        result["verdict"] = verdict
        result["reasons"] = reasons
        result["max_honest_score"] = max_honest
        pdf_path = out_dir / "job-match-report.pdf"
        jobmatch.build_pdf(result, str(pdf_path))

        # Summary md
        summary_path = write_summary_md(
            out_dir, target_title, verdict, score, threshold,
            result["comp"], result, verified_omitted, true_gaps,
            unverified_in_resume, max_honest, baseline_data
        )

        # Console output
        print(f"\n=== POST-MODE MATCH SUMMARY ===")
        if baseline_data:
            print(f"Score  : {baseline_data.get('score','?')}% → {score}%  (Δ {score - baseline_data.get('score',score):+d})")
        else:
            print(f"Score  : {score}% (Threshold: {threshold}%, Floor: {fit_floor}%)")
        print(f"Verdict: {verdict.replace('_',' ').upper()}")
        print(f"Pages  : {pages}   needs_revision={needs_revision}")
        print(f"Ceiling: {max_honest}% (if all verified-omitted skills were added)")

        if reasons:
            print("\nReasons:")
            for r in reasons:
                print(f"  - {r}")

        print("\nComponent Breakdown:")
        for k, v in result["comp"].items():
            val = "N/A" if v is None else f"{round(v*100)}%"
            print(f"  {k} ({jobmatch.WEIGHTS[k]}%): {val}")

        print(f"\nVerified Omitted (safe to add): {len(verified_omitted)}")
        for vo in verified_omitted:
            print(f"  [{vo['priority']}] {vo['name']}  tier={vo.get('usage_tier','?')}")
            print(f"       {vo.get('evidence','')}")

        print(f"\nTrue Gaps: {len(true_gaps)}")
        for tg in true_gaps:
            print(f"  [{tg['priority']}] {tg['name']}")

        if has_unverified:
            print(f"\n⚠  FABRICATION CHECK — Skills in resume NOT in Master_Data (REMOVE THESE):")
            for u in unverified_in_resume:
                print(f"  ⚠  {u}")

        print(f"\nOutputs:")
        print(f"  JSON   : {json_path}")
        print(f"  PDF    : {pdf_path}")
        print(f"  Summary: {summary_path}\n")

if __name__ == "__main__":
    main()

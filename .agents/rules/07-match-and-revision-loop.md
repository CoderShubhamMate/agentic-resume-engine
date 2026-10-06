---
trigger: always_on
---

# 07 — JD MATCH, SCORE AND TRUTHFUL REVISION LOOP

Before step 1 of every application, read `tools\MATCH_RULES.md` in full. It holds the detailed procedure for scoring and match steps.
Files 00, 01, 02, 04, 05 and 08 always win over it. If this file and `tools\MATCH_RULES.md` disagree on match, score or report steps, follow `tools\MATCH_RULES.md` and report the conflict.

## 7.1 Essentials
- Scripts only MEASURE. They never edit the resume. The agent writes and revises every change.
- Matcher input is only this job's `job-description.md`, `Master_Data\*.md` and this folder's `resume.pdf`. Never run it on `prompt.md` (the script refuses).
- Commands, from the project root:
  - PRE: `python tools/match_resume.py --mode pre --folder "<Company> - <Job Title>"`
  - POST: `python tools/match_resume.py --mode post --folder "<Company> - <Job Title>"` (add `--baseline job-match-baseline.json` on every run after the first)
- If the matcher, the scripts or `tools\MATCH_RULES.md` are missing or fail, finish the resume normally and report "match step skipped" with the reason.

## 7.2 Flow
- **PRE:** use VERIFIED skills, required ones first, to shape the summary, skill order and bullets. True-gap skills never appear in Skills, Experience or Projects.
- **POST (first run):** save the result as `job-match-baseline.json`. Back up this version (`resume.tex` and `resume_render.html`) in `_match_work\`.
- **Revision loop:** only while `needs_revision` is true, MAX 3 passes. Each pass may add `verified_omitted` skills ONLY where Master_Data evidence and the usage tier allow, in natural wording inside a truthful skills line, bullet or project line.
  - Never keyword-stuff, add new claims, invent metrics, rename roles, projects or dates.
  - Never change project names or stack lines (02).
  - Never move Areas of Interest items into Skills or bullets.
  - Edit BOTH `resume.tex` and `resume_render.html`, keep exactly one page, recompile, run POST with `--baseline`.
  - Keep the pass only if the score improved, the PDF is one page and there are no true unverified skills (7.3). Otherwise restore the best earlier version and stop.
- **Stop** when the score is 90 or higher, when `verified_omitted` is empty, or after 3 passes. The final resume is the best valid version, not the last attempt.
- Rebuild `resume.pdf` and `job-match.json` from that final version.
- Do not chase the score. Stopping below 90 because of real gaps is correct.

## 7.3 Handling `unverified_in_resume`
The checker scans the whole PDF, including the Areas of Interest section.
- A flagged item that appears ONLY in the Areas of Interest section is NOT fabrication. It is an honest expression of interest.
- To confirm, search `resume.tex` for each flagged item and note where it appears.
- A flagged item that appears in Skills, Summary, a bullet, a project line or a certification is a violation. Remove or reword it, recompile, and rerun POST.
- Items found only in Areas of Interest never count toward the match score.

## 7.4 Verdicts
- 90 or more: Good fit.
- 60 to 89: Acceptable fit (name the gaps).
- Below 60: WEAK FIT. Still deliver the best truthful resume, but state plainly that it is a weak match, explaining the reasons, the estimated ceiling, and what verified evidence would be needed.

## 7.5 Report
At the end, compile `job-match-summary.md` and use it for `job-match-report.pdf`. Then `_match_work\` is removed during cleanup (08).

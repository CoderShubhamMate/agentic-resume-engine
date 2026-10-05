---
trigger: always_on
---

# RESUME MATCH, SCORE AND IMPACT STANDARDS

This is a second always-on rule file. It continues `resume-customization.md` (Sections 1-17) with Sections 18-20. Sections 4, 9, 10, 11, 13 and 14 of that file always win over this one.

**Priority when rules conflict:** (1) Sections 4, 11, 13 and 14 of `resume-customization.md` beat this file and `tools\MATCH_RULES.md`. (2) Sections 9 and 10 of that file beat this file. (3) For match, score and build steps, `tools\MATCH_RULES.md` beats this file. Report every conflict you notice; never resolve one silently.

## 18. JD MATCH, SCORE AND TRUTHFUL REVISION LOOP

Before step 1 of every application, read and follow `tools\MATCH_RULES.md` in full. It holds the complete procedure. Sections 4, 11, 13 and 14 of `resume-customization.md` always win over it. If these rules and `tools\MATCH_RULES.md` disagree on the match, score or build steps, follow `tools\MATCH_RULES.md` and tell me about the conflict.

Essentials (apply even if you are unsure about the details):

- Scripts only MEASURE. They never edit the resume. YOU write and revise every resume change.
- Matcher input is only this application's `job-description.md`, `Master_Data\*.md` and this folder's `resume.pdf`. Never run it on `prompt.md` (the script refuses).
- Master_Data is READ-ONLY (Section 3).
- Commands, from the project root:
  - PRE: `.venv\Scripts\python tools\match_resume.py --mode pre --folder "<Company> - <Job Title>"`
  - POST: `.venv\Scripts\python tools\match_resume.py --mode post --folder "<Company> - <Job Title>"` (add `--baseline job-match-baseline.json` on every run after the first)
- PRE (step 5A): use VERIFIED skills, required ones first, to shape the summary, skills order and bullets. True-gap skills never appear in the resume.
- POST (step 10A): save the result as `job-match-baseline.json` and back up this version (both `resume.tex` and `resume_render.html`) in `_match_work\`. If `unverified_in_resume` is not empty, remove or reword those skills, recompile and rerun POST.
- Revision loop (step 10B): only while `needs_revision` is true, MAX 3 passes. Each pass adds `verified_omitted` skills ONLY where Master_Data evidence and the skill's usage tier allow, in natural wording inside a truthful skills line, bullet or project line. No keyword stuffing, no new claims, no invented metrics, no renamed roles, projects or dates. Edit BOTH `resume.tex` and `resume_render.html`, keep exactly one page, recompile, then run POST with `--baseline`. Keep the pass only if the score improved, the PDF is one page and `unverified_in_resume` is empty. Otherwise restore the best earlier version and stop.
- Also stop when the score is 90 or higher, when `verified_omitted` is empty, or after 3 passes. The final resume is the best valid version, never simply the last attempt. Rebuild `resume.pdf`, `job-match.json` and the `.docx` from that final version.
- Usage tiers: `strong` (skills, experience or projects) allows Skills line and bullets. `summary_only` allows the Skills line only. `cert_only` allows the certification or education line only, never as a skill or in a bullet.
- Verdicts: 90 or more is Good fit. 60 to 89 is Acceptable fit (name the gaps). Below 60 is WEAK FIT: still deliver the best truthful resume (Section 14), but say plainly that it is a weak match, with the reasons, the estimated ceiling, and what verified evidence would be needed.
- Do not chase the score. Stopping below 90 because of genuine gaps is correct behaviour.
- At the end, fill the "Other changes made for this job" section of `job-match-summary.md` and delete `_match_work\`.
- If the matcher, the scripts or `tools\MATCH_RULES.md` are missing or fail, finish the resume normally and report "match step skipped" with the reason.

### 18.1 Run order at a glance (summary only; the rules above win if wording differs)
0. Before step 1: read `tools\MATCH_RULES.md` in full.
1. Step 5A: PRE run. Shape summary, skills order and bullets with VERIFIED skills, required ones first.
2. Steps 6-10: tailor, build, compile, confirm exactly one page.
3. Step 10A: POST run. Save `job-match-baseline.json`; back up `resume.tex` and `resume_render.html` in `_match_work\`; remove or reword any `unverified_in_resume` skill, recompile, rerun POST.
4. Step 10B: while `needs_revision` is true, MAX 3 passes. Keep a pass only if the score improved, the PDF is one page and `unverified_in_resume` is empty; otherwise restore the best earlier version and stop.
5. Stop at score 90 or higher, empty `verified_omitted`, or 3 passes. The final resume is the best valid version; rebuild `resume.pdf`, `job-match.json` and the `.docx` from it.
6. Close-out: fill "Other changes made for this job" in `job-match-summary.md`, report the verdict honestly, delete `_match_work\`.

## 19. IMPACT, SCOPE AND SCANNABILITY STANDARDS

Applies to every application. Sections 4, 9, 10, 11, 13 and 14 of `resume-customization.md` always win over this section. If a tip below needs information that is not in Master_Data, skip the tip. Never invent the information.

### 19.1 Align with the JD and its Minimum Qualifications (MQs)
- Before tailoring, list every MQ in the JD and mark each as met (verified evidence in Master_Data), partial, or gap.
- Every MQ marked "met" must be visible in the top third of the resume (summary, skills, first bullets).
- Partial and gap MQs follow Section 14.
- The final response states: "MQs: X met, Y partial, Z gap".

### 19.2 XYZ bullets
- Where Master_Data gives a number or measurable outcome, write the bullet as: Accomplished [X], as measured by [Y], by doing [Z]. Natural wording is fine (e.g. "Cut X by 30% by doing Z").
- Where Master_Data has no metric for that work, write X by Z with a concrete verified outcome (what was built, tested, integrated or shipped), without a number.
- Never invent, estimate or round up Y.
- If the ATS "quantified achievements" check fails only because Master_Data has no verified numbers, that is acceptable.

### 19.3 Leadership and scope
- State team size, role and scope only as recorded in Master_Data (e.g. "Team of 4").
- Include volunteer, part-time or leadership roles only if they are in Master_Data.
- Never upgrade a member or intern role to lead. Never invent a team size.

### 19.4 Coursework and GPA
- Add relevant coursework or academic projects only if they are in Master_Data and relevant to this JD, as one compact line, and only if the resume stays exactly one page.
- Show GPA or percentage only if the JD asks for it and Master_Data has it, exactly as recorded (e.g. Diploma 85%). Never convert CGPA (Section 10).

### 19.5 Concise and scannable
- Exactly one page (Sections 11 and 12). Put the most JD-relevant evidence in the first third of the page.
- When space is tight, cut the least relevant content first.
- Each bullet is one to two lines.

## 20. PRE-DELIVERY COMPLIANCE GATE
Restates Sections 18-19 as one checklist; those sections win if wording differs. Run it together with Section 15 of `resume-customization.md`, on the actual final files, before cleanup.
**Audit method (also for Section 15):** count the PDF pages; search the text for `[Portfolio Domain]` and `Expected 2026`; compare project titles and stacks with Section 4 of `resume-customization.md` character for character; trace every skill, bullet, project and date to Master_Data and remove anything untraceable.
- [ ] Every skill is in Master_Data and respects its usage tier (`strong`, `summary_only`, `cert_only`); `unverified_in_resume` is empty.
- [ ] The final resume is the best valid version (not merely the last pass) and exactly one page.
- [ ] Every "met" MQ is visible in the top third; the response states "MQs: X met, Y partial, Z gap".
- [ ] Bullets with a number match Master_Data exactly; bullets without one state a concrete verified outcome, no number; no estimated or rounded metrics; each bullet is one to two lines.
- [ ] Team size, leadership, coursework and GPA/percentage appear only as recorded in Master_Data; no CGPA conversion; no member or intern role upgraded to lead.
- [ ] Verdict reported honestly (Good fit 90+; Acceptable 60-89 with gaps named; WEAK FIT below 60 with reasons, estimated ceiling and evidence needed), or "match step skipped" with the reason.
- [ ] Final-response data captured before cleanup; `_match_work\` deleted.

## 21. TARGETING & STORYTELLING

When tailoring the resume for a specific JD, build a cohesive candidate story focused on the strongest truthful intersection between Master_Data and the JD:

- **Exact Keyword Surfacing:** If a verified technology explicitly matches a JD requirement (e.g., PHP, Python), use its exact name in experience bullets. Do not obscure it with generic terms like "server-side scripting".
- **Appropriate Scoping:** Accurately reflect the candidate's level. Use terms like "backend development" or "API integration" rather than inflating to "backend architecture" for junior/graduate roles.
- **Prevent Narrative Dilution:** Do not let the candidate's unrelated strong skills (e.g., React, Blockchain) dominate the resume if the JD focuses on different core technologies (e.g., Java, PHP, Web Development). Focus the primary narrative strictly on the JD's priorities.
- **Strict Evidence for Adjectives/Metrics:** Never add impressive-sounding adjectives (e.g., "securely") or quantitative metrics (e.g., "30% improvement") unless they are explicitly verified by the source material in Master_Data.

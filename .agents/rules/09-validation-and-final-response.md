---
trigger: always_on
---

# 09 — FINAL VALIDATION AND FINAL RESPONSE

## 9.1 Checklist (run before cleanup, fix anything that fails)

**Job and files**
- [ ] Correct company, role and job folder name
- [ ] Original `prompt.md` text preserved exactly
- [ ] `job-description.md` created
- [ ] `resume_render.html` matches `resume.tex` exactly
- [ ] `resume.pdf` compiled from the final HTML
- [ ] Exactly one page, visually clean, no render or LaTeX errors, ATS-readable
- [ ] Match step completed (or reported as skipped with the reason)
- [ ] `job-match-report.pdf` created

**Truth and locks**
- [ ] Contact details correct and factual; no portfolio placeholder
- [ ] Role titles, employers and dates exactly as in 01 and Master_Data
- [ ] Project names exactly as in Master_Data (02)
- [ ] Project stack sets exactly as in Master_Data (reorder only)
- [ ] No fabricated skills, experience, projects, metrics, adjectives
- [ ] Every skill has Master_Data evidence and respects its usage tier
- [ ] No true unverified skill outside Areas of Interest (07 section 7.3)
- [ ] Mandatory gaps not falsely claimed
- [ ] MQs marked met / partial / gap

**Writing**
- [ ] No unfinished placeholder left anywhere
- [ ] Target company name does NOT appear anywhere in the resume
- [ ] Summary has no cover-letter wording (03 section 3.4)
- [ ] Summary and first bullets reflect THIS JD's own emphasis, not template defaults
- [ ] Relevant JD keywords included only where truthful
- [ ] Areas of Interest is last, 3 to 8 items (or fewer with reason), interest wording only (04)

## 9.2 Final response format

```
Completed: <Company> — <Role>
```
Then include:
- Files in the folder (the 4 final files)
- Major tailoring changes
- Mandatory requirement gaps, if any
- Any important issue preventing a perfect match
- MQs: X met, Y partial, Z gap
- Match result: verdict, baseline → final score, keywords added and where, top gaps (or "match step skipped" with the reason)
- Rule conflict, if any
- One line: "Build files are archived in prompt.md (repair bundle)." or the list of files kept under 8.6

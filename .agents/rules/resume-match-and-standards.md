# RESUME MATCH, SCORE AND IMPACT STANDARDS

This is the second rule file for ATS match scoring and content impact standards.

## 1. JD MATCH, SCORE AND REVISION LOOP

- Scripts only MEASURE. They never edit the resume. The agent writes and revises every resume change.
- Matcher input is only this application's `job-description.md`, `Master_Data\*.md` and this folder's `resume.pdf`.
- Master_Data is READ-ONLY.
- Commands:
  - PRE: `python tools/match_resume.py --mode pre --folder "<Company> - <Job Title>"`
  - POST: `python tools/match_resume.py --mode post --folder "<Company> - <Job Title>"`
- PRE: Use VERIFIED skills to shape summary, skills order, and bullets. True-gap skills never appear in the resume.
- POST: Run POST mode match and verify `unverified_in_resume` is empty.
- Revision loop: Up to 3 passes. Each pass adds verified omitted skills ONLY where Master_Data evidence allows.
- Verdicts: 90+ Good fit, 60-89 Acceptable fit, <60 Weak fit.
- Stop when score is 90+, `verified_omitted` is empty, or after 3 passes.

## 2. IMPACT & SCANNABILITY STANDARDS

- Align with JD Minimum Qualifications (MQs): mark met, partial, gap.
- Bullets follow Action + Work + Outcome.
- Maintain strict 1-page compliance.

# ATS MATCH RULES & STANDARDS

This document contains technical matching rules and procedure details for `match_resume.py`.

## Part 1. Objective Matching Procedure
- Scripts only MEASURE. They never edit the resume. The agent writes and revises every resume change.
- Matcher input is only this application's `job-description.md`, `Master_Data\*.md` and this folder's `resume.pdf`.
- Master_Data is READ-ONLY.

## Part 2. Execution Modes
- PRE-Mode: `python tools/match_resume.py --mode pre --folder "<Company> - <Job Title>"`
- POST-Mode: `python tools/match_resume.py --mode post --folder "<Company> - <Job Title>"`

## Part 3. Score Thresholds & Revision Loop
- Target Score: 90% (Good fit).
- Floor Score: 60% (Acceptable fit).
- Max 3 revision passes.
- Stop when score >= 90%, verified omitted list is empty, or after 3 passes.

## Part 4. Application Logging
Whenever a customized resume package is generated:
- Optionally run `tools/sync_excel.py` to log application metadata:
  ```bash
  python tools/sync_excel.py --company "<Company>" --role "<Role>" [--status "Applied"]
  ```

---
trigger: always_on
---

# 06 — BUILD PIPELINE

Whenever a job `prompt.md` is provided, execute the full pipeline to produce the completed application package.

## 6.1 Job input
Every `prompt.md` is ONE application unless specified otherwise. Read the entire file first. It contains company, job title, job ID, location, full JD, requirements, and customization instructions.

## 6.2 Folder naming
Create a NEW folder in the project root: `<Company> - <Job Title>`
If a Job ID helps: `<Company> - <Job Title> - <Job ID>`
Never overwrite or mix another application's files.

## 6.3 Application isolation (fresh start every time)
- Each job is independent. Never open or copy from another job folder.
- Always start `resume.tex` from the template in `05-resume-template.md`, never from a previous resume.
- Never carry over another company's name, role, JD requirements, keywords, assumptions, match scores, reports, or revision history.
- Read this job's `prompt.md` from scratch and write the JD analysis (03 section 3.1) BEFORE touching the resume, so this job's own emphasis is not lost.

## 6.4 Steps (in order)
1. Read `prompt.md` completely.
2. Read rule files 00 to 09, `tools\MATCH_RULES.md`, and `Master_Data\*.md`.
3. Create the job folder. Keep `prompt.md` there unchanged.
4. Create `job-description.md`: a clean copy of the full JD from the prompt.
5. Analyze the JD (03 section 3.1), including MQs marked met / partial / gap.
6. Run the matcher in PRE mode (07).
7. Create `resume.tex` from the template and tailor it (03, 04).
8. Create `resume_render.html`, an exact HTML mirror of `resume.tex` (same content, same order).
9. Compile `resume.pdf` from the HTML with headless Chrome (6.5).
10. Inspect the PDF and fix problems (6.6). It must be exactly one page.
11. Run POST mode and the revision loop (07).
12. Run final validation (09).
13. Compile `job-match-report.pdf` (per `tools\MATCH_RULES.md`).
14. Run cleanup and write the repair bundle (08).
15. Verify the folder contains exactly the 4 final files, then send the final response (09).

## 6.5 Compile command (pdflatex is not installed)
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="resume.pdf" "resume_render.html"
```
*(On macOS/Linux, substitute `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` or `google-chrome`)*

Every content change must be made in BOTH `resume.tex` and `resume_render.html`, then recompiled. A change in only one of them does not reach the PDF.

## 6.6 Inspect and fix
Check the compiled PDF for: render errors, page overflow, bad line breaks, orphan headings, excess whitespace, alignment problems, certifications or Areas of Interest spilling to a second page.
If it overflows: (1) remove redundant wording, (2) tighten content, (3) adjust spacing carefully, (4) make layout changes only as needed. Never make the text unreadably small.

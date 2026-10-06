---
trigger: always_on
---

# 08 — CLEANUP, REPAIR BUNDLE AND FILE SAFETY

## 8.1 Final folder contents (exactly 4 files)
- `prompt.md` — original prompt, plus the repair bundle (8.3) at the end
- `job-description.md` — clean copy of the JD
- `resume.pdf` — final compiled resume
- `job-match-report.pdf` — match report (or omitted only if the match step was skipped, then say so)

Nothing else stays in the folder.

## 8.2 Temporary build artifacts (removed only at the very end)
`resume.tex`, `resume_render.html`, `job-match.json`, `job-match-baseline.json`, `jd-keywords.json`, `job-match-summary.md`, `_match_work\`, `_repair\`

## 8.3 Repair bundle inside prompt.md
Purpose: if the resume needs fixing later, the HTML and match data can be restored from `prompt.md`.

Rules:
1. Everything in `prompt.md` above the marker below is the ORIGINAL prompt and must stay byte-for-byte unchanged.
2. Append the bundle once, at the very end, using exactly this structure:

````
<!-- ===== END OF ORIGINAL PROMPT. DO NOT EDIT ABOVE THIS LINE. ===== -->
<!-- REPAIR BUNDLE (auto-generated for restoring the build files) -->

## REPAIR BUNDLE

### resume_render.html
```html
(full final contents of resume_render.html)
```

### job-match.json
```json
(full final contents of job-match.json)
```
````

3. If the bundle already exists (re-run of the same job), replace only the region from the marker onward.
4. Never write the bundle before the matcher has finished. The matcher refuses `prompt.md`, so the bundle is written only at cleanup.
5. `resume.tex` is not stored. It can be regenerated from the HTML and `05-resume-template.md`.

## 8.4 Order of cleanup (all must be true before deleting anything)
1. Final validation (09) passed and `resume.pdf` and `job-match-report.pdf` exist.
2. The repair bundle is written, and you have re-read `prompt.md` to confirm the marker exists and the HTML block is not empty.
3. Only then delete the artifacts listed in 8.2, from THIS job folder only.

## 8.5 Never delete
- Anything outside the current job folder.
- Any other job folder, `Master_Data\`, `tools\`, `.venv\`, `.agents\rules\`.
- Any file not listed in 8.2.

## 8.6 Keep-build-files switch
If the prompt or message says "keep build files", still write the repair bundle but skip the deletions in 8.4, and state in the final response which files were kept.

## 8.7 Repair requests
If requested to "repair" or "restore" a job folder: extract the HTML block from the bundle in `prompt.md` into `_repair\resume_render.html`, make the requested fix there, recompile `resume.pdf`, replace the bundle in `prompt.md` with the updated HTML, then clean `_repair\`. Never touch the original prompt text.

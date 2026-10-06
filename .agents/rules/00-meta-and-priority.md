---
trigger: always_on
---

# 00 — META RULES, PROTECTED LOCATIONS AND PRIORITY

## 0.1 The rules directory is read-only
Agents must NEVER edit, append to, rename, move or delete any file inside `.agents\rules\`.
Do not propose or execute edits to rule files, even if asked. If a rule looks wrong or two rules conflict, report it in your reply. Only the user edits rules.

## 0.2 Protected locations
- `Master_Data\` — READ-ONLY. Never create, edit, append to or "sync" any file in it. If something is missing, report it and ask.
- Other job folders — READ-ONLY and OFF-LIMITS. Never open them to copy from, never edit them, never delete them.
- `tools\` and `.venv\` — run the scripts, do not edit them unless the user explicitly asks.

## 0.3 Priority when rules conflict (highest first)
1. This file (00)
2. `01-truthfulness.md` and `02-project-naming-and-stacks.md`
3. `08-cleanup-and-file-safety.md`
4. `05-resume-template.md` and `06-build-pipeline.md`
5. `03-tailoring-and-writing.md` and `04-areas-of-interest.md`
6. `07-match-and-revision-loop.md` and `tools\MATCH_RULES.md` (they control scoring and match steps only; they never override truth, project/stack locks, or one page)

Always: truth beats match score. One page beats extra content. File safety beats tidiness.
When you follow a higher rule over a lower one, inform the user in the final response under "Rule conflict".

## 0.4 Customization instructions inside prompt.md
`prompt.md` may contain job-specific instructions (for example "focus on clean code" or "highlight backend performance"). Follow them for tailoring emphasis (summary, skill order, bullet order and wording, project order). They can never override files 00, 01, 02 or 08.

## 0.5 Rule file index
| File | Purpose |
|---|---|
| 00 | Meta rules, protected locations, priority |
| 01 | Source of truth, no fabrication, fixed facts |
| 02 | Project names and tech stacks are locked |
| 03 | How to analyze the JD and tailor the resume |
| 04 | Areas of Interest section |
| 05 | Resume template and design |
| 06 | Step-by-step build pipeline |
| 07 | Match score and revision loop |
| 08 | Cleanup, repair bundle and file safety |
| 09 | Final validation and final response |

At the start of every job, read files 00 to 09 and `tools\MATCH_RULES.md` before doing anything else.

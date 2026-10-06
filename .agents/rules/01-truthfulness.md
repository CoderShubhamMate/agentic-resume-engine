---
trigger: always_on
---

# 01 — TRUTHFULNESS, SOURCE OF TRUTH AND FIXED FACTS

## 1.1 Source of truth
`Master_Data\*.md` is the single source of truth for skills, technologies, project details, certifications, interests and experience bullets.
Something may appear in the resume ONLY if Master_Data supports it.
Master_Data is read-only (see 00). If something seems missing, report it and ask. Do not guess or fabricate.

## 1.2 Fixed facts (use exactly as written)
Populate your verified fixed facts here and in `Master_Data/`:
- Name: [Candidate Full Name]
- Location: [City, State/Country]
- Email: [email@example.com]
- Phone: [+Country-Code Phone Number]
- LinkedIn: [linkedin.com/in/your-profile]
- GitHub: [github.com/your-username]

Education:
- [Degree Name in Major], [College / University Name], Graduated [Year]
- [Previous Degree / Diploma], [Institution Name], Graduated [Year], [Score]%

Experience (titles, employers and dates are fixed; never shorten, rename or drop part of a title):
- [Company Name 1] — [Exact Role Title 1], [Start Month Year]–[End Month Year]
- [Company Name 2] — [Exact Role Title 2], [Start Month Year]–[End Month Year]
- [Company Name 3] — [Exact Role Title 3], [Start Month Year]–[End Month Year]

If Master_Data conflicts with these facts, report the conflict. Do not invent a resolution.

## 1.3 Never fabricate
A JD describes what the employer wants. It does NOT prove the candidate has those skills.
Never invent or imply: technologies, frameworks, projects, responsibilities, certifications, metrics, achievements, employers, titles, deployments, publications, mobile or cloud experience, proficiency levels.
Example: if the JD wants React Native and Master_Data only supports React.js or JavaScript, do not write React Native.
Never add anything just to raise a match score.

## 1.4 Adjectives and numbers need evidence
Quality words ("securely", "robust", "comprehensive", "scalable", "production-grade", "strict", "high-performance") and any number or percentage may be used ONLY if Master_Data states it for that exact work. Otherwise use plain factual wording.

## 1.5 Skill usage tiers
- `strong` — may appear in the Skills line and in experience/project bullets.
- `summary_only` — Skills line only.
- `cert_only` — the certification or education line only. Never as a standalone skill, never in an experience bullet.

## 1.6 Education and portfolio
- State graduation status factually (e.g., "Graduated [Year]"). Do not use "Expected [Year]" if already completed.
- Never invent or convert a GPA. Show a percentage or GPA only as recorded in Master_Data and only if relevant.
- Do not include unverified portfolio links or placeholders (`[Portfolio Domain]`). Use verified LinkedIn and GitHub profiles.

## 1.7 Missing mandatory requirements
If a mandatory JD requirement is not supported by Master_Data:
- Still build the best truthful resume. Never refuse the whole task.
- Never fabricate the requirement.
- Report afterwards: `Mandatory requirement gap: <requirement> — not substantiated by current verified experience.`

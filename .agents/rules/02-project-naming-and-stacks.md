---
trigger: always_on
---

# 02 — PROJECT NAMES AND TECH STACKS ARE LOCKED

Why: project names and stacks must match the candidate's GitHub, portfolio, published papers, and interview answers. Renaming projects and editing stacks to match JDs causes severe discrepancies during technical interviews.

## 2.1 The lock
1. **Name:** copy the project name exactly as written in `Master_Data\Projects.md`. Never rename, shorten, genericize or "reframe" it.
2. **Stack line:** the technologies shown beside the project name must be exactly the set listed in `Master_Data\Projects.md` for that project.
   - Never add a technology (e.g. no SQL/MySQL unless Master_Data lists it for that project).
   - Never remove a core technology (never delete specialized domains like Android, Blockchain, or Machine Learning to look more "standard").
   - You MAY reorder the items to put the most JD-relevant verified technologies first.
3. **Tailor through bullets only.** Emphasis for a JD goes into the bullet wording, never into the project title or the stack header.
4. You MAY choose which projects appear and in what order. Keep verified projects unless strict 1-page constraints force a cut. Cut the least relevant project first.

## 2.2 Snapshot (Master_Data wins if it differs; report any difference)
Populate your key projects from `Master_Data/Projects.md`:
| Project name | Verified stack |
|---|---|
| [Project Title 1, e.g. Distributed Task Queue] | [Stack 1: e.g. Python, Celery, Redis, Docker, PostgreSQL] |
| [Project Title 2, e.g. Microservices E-Commerce API] | [Stack 2: e.g. Go, gRPC, PostgreSQL, Docker] |

## 2.3 Forbidden examples
- Renaming "[Specialized Domain Project]" to "[Generic Web App]" instead of the real repository name.
- Dropping core technologies (e.g., dropping `Redis` or `Docker`) to look like a standard web stack.
- Adding unverified technologies (e.g., adding `Kubernetes` or `AWS`) to the stack line just because the JD requests them.
- Inventing a subtitle or alternate identity for non-specialized roles.

## 2.4 How to tailor bullets instead
- Backend / API roles: lead with endpoint architecture, query optimization, API testing.
- Systems / DevOps roles: lead with containerization, caching workflows, performance benchmarks.
- General engineering roles: lead with OOP design, test automation, modular structure.
- Specialized roles: lead with the domain-specific component (e.g. ML models, distributed consensus).
Every bullet must still be supported by Master_Data (see 01).

## 2.5 Publications & Research
If Master_Data records that a project was published as a research paper or won an award, one bullet or the project line may mention it, exactly as recorded (journal name or competition name included). Include it when it helps the role; never embellish it.

# 📄 Agentic Resume Engine — AI ATS-Friendly Resume Builder & Job Description Tailor

**Autonomous 5-Agent AI Resume Tailor & ATS Resume Builder powered by Google Gemini (`@google/genai` SDK), Python, Jinja2, and Headless Chrome.**

[Use This Template](https://www.google.com/search?q=https://github.com/CoderShubhamMate/agentic-resume-engine/generate)
[](https://github.com/CoderShubhamMate/agentic-resume-engine/blob/main/LICENSE)
[](https://github.com/CoderShubhamMate/agentic-resume-engine)

> **Stop rewriting your resume manually for every job application.** Transform a single master career JSON file (`master_data.json`) into targeted, single-page, **ATS-friendly PDF resumes** custom-tailored to any **Job Description (JD)** in seconds—with **zero hallucinated experience**.

## 🎯 Why Job Seekers Clone This ATS Resume Builder

The **Agentic Resume Engine** treats custom resume creation as an automated software compilation pipeline. Instead of spending 45+ minutes manually editing Word or LaTeX files for every job posting, you maintain one **Master Resume Data (`Master_Data/master_data.json`)** file containing your complete, verified career history.

Whenever you find a role you want to apply for, paste the **Job Description (JD)** and run the pipeline. Five specialized AI agents analyze the JD, filter your most relevant achievements, enforce a strict single-page line budget, verify every claim against your master history, and compile four ready-to-use outputs:

1. 📄 **Single-Page ATS-Friendly PDF Resume** (`output/<date_company>/resume_<name>.pdf`) — Clean, selectable text rendered via Headless Chrome with zero multi-column parsing traps.
2. 🌐 **Editable HTML Resume Source** (`output/<date_company>/resume_render.html`) — Semantic HTML + inline CSS built from customizable Jinja2 templates (`tools/templates/`).
3. 🎯 **ATS Keyword Match & Skill Gap Scorecard** (`output/<date_company>/job-match.json`) — Deterministic 0–100% ATS match breakdown across Hard Skills, Job Keywords, Title Alignment, Tenure, Formatting, and Soft Skills.
4. 📋 **Full Audit & Prompt Trace** (`output/<date_company>/prompt.md`) — Complete multi-agent reasoning log plus an embedded `## REPAIR BUNDLE` backup of your rendered HTML and JSON score.

## 🏛 Multi-Agent Architecture & Compilation Flow

1. **Input Stage**: Raw Job Description (`jd.txt`) + Candidate Career Profile (`Master_Data/master_data.json`)
2. **Agent 1 — JD Analyst (`AJDPrompts/jd-analyst.md`)**: Extracts core technical skills, domain keywords, required tenure, and soft skills into a structured JD profile.
3. **Agent 2 — Section Planner (`AJDPrompts/section-planner.md`)**: Calculates strict visual line-budget limits per section to guarantee a single-page layout and selects your highest-impact items.
4. **Agent 3 — Truth Engine (`AJDPrompts/truth-engine.md`)**: Enforces zero-hallucination governance—maps verified history to JD keywords without inventing roles, skills, or metrics.
5. **Agent 4 — Resume Writer & Layout Guard (`AJDPrompts/resume-writer.md`)**: Compiles semantic HTML via Jinja2 templates (`tools/templates/`) with strict inline CSS formatting bounds.
6. **Agent 5 — ATS Matcher & Auditor (`AJDPrompts/ats-matcher.md`)**: Audits the compiled resume against the target JD across 7 weighted ATS dimensions and outputs `job-match.json`.

### 🤖 The 5-Agent Pipeline Breakdown

| Agent Stage | Prompt Definition | Core ATS & Tailoring Responsibility |
| :--- | :--- | :--- |
| **Agent 1: JD Analyst** | `AJDPrompts/jd-analyst.md` | Parses the target job description to extract required hard skills, domain keywords, experience tenure, and role expectations. |
| **Agent 2: Section Planner** | `AJDPrompts/section-planner.md` | Computes line-budget constraints per resume section so the final PDF never spills onto a second page. |
| **Agent 3: Truth Engine** | `AJDPrompts/truth-engine.md` | Guarantees 100% factual accuracy by grounding every bullet point in `master_data.json` with zero fabricated experience. |
| **Agent 4: Resume Writer & Layout Guard** | `AJDPrompts/resume-writer.md` | Renders ATS-parsable semantic HTML using Jinja2 templates (`tools/templates/`) and Headless Chrome print styling. |
| **Agent 5: ATS Matcher & Auditor** | `AJDPrompts/ats-matcher.md` | Scores the final resume (0–100%) across Hard Skills, Keywords, Text Similarity, Tenure, ATS Formatting, and Soft Skills. |

## 🔒 Truth Engine: Zero-Hallucination Resume Tailoring

Unlike generic AI resume generators that invent fake skills to stuff keywords, the **Truth Engine** (`AJDPrompts/truth-engine.md`) enforces strict factual guardrails:

* **Verified Experience Only**: Every bullet point must originate from documented entries in `Master_Data/master_data.json`.
* **Smart Action-Verb & Keyword Alignment**: Phrasing and technical context are dynamically tailored to mirror the employer's exact terminology where your background genuinely matches.
* **Immutable Metrics**: Quantified impact numbers (percentages, latency reductions, revenue, scale) are preserved strictly as recorded in your master file.
* **Honest Skill-Gap Handling**: If a job description requires a tool or skill you haven't used yet, the engine never fakes it in your Experience or Skills sections—instead, it surfaces relevant domain terms transparently under **Areas of Interest** (e.g., *"Interested in developing expertise in: Kubernetes, Distributed Systems"*).

## 🚀 Quick Start: Clone & Build Custom Resumes in 2 Minutes

### Prerequisites

* **Python 3.10+**
* **Google Gemini API Key** (`GEMINI_API_KEY`)
* **Google Chrome** installed locally (used in headless mode for pixel-perfect PDF compilation)

### Step 1: Create Your Own Repository or Clone Locally

Click **[Use this template](https://www.google.com/search?q=https://github.com/CoderShubhamMate/agentic-resume-engine/generate)** at the top of the repository to create your own personal copy on GitHub, or clone it directly to your machine:

```bash
git clone https://github.com/CoderShubhamMate/agentic-resume-engine.git
cd agentic-resume-engine
```

### Step 2: Install Dependencies

```bash
pip install -e .
```

### Step 3: Configure Your Gemini API Key

* **Linux / macOS:**
  ```bash
  export GEMINI_API_KEY="your-api-key-here"
  ```
* **Windows (Command Prompt):**
  ```cmd
  set GEMINI_API_KEY=your-api-key-here
  ```
* **Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="your-api-key-here"
  ```

### Step 4: Tailor Your Resume to Any Job Description

1. Add your complete career history once inside `Master_Data/master_data.json`.
2. Paste your target job posting into a text file (for example, `JDs/target_jd.txt`).
3. Run the automated 5-agent compilation pipeline:

```bash
python tools/run_pipeline.py --jd JDs/target_jd.txt --master Master_Data/master_data.json
```

## 🛠 Repository Structure

```text
agentic-resume-engine/
├── .agents/
│   └── rules/           # Cursor / Agentic system rules
├── AJDPrompts/          # Prompt templates for the 5 AI Agents
│   ├── jd-analyst.md
│   ├── section-planner.md
│   ├── truth-engine.md
│   ├── resume-writer.md
│   └── ats-matcher.md
├── Master_Data/         # Single source of truth for your career history
│   └── master_data.json
├── examples/            # Sample Job Descriptions and generated resume outputs
├── tools/               # Pipeline runner & ATS-friendly Jinja2 HTML templates
│   ├── run_pipeline.py
│   └── templates/
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
└── setup.py
```

## ⚙️ Customization & Manual PDF Rendering

* **Master Career Profile**: Edit `Master_Data/master_data.json` once with all your work experience, projects, education, technical skills, and certifications.
* **Custom Resume Templates**: Tweak the Jinja2 HTML/CSS templates in `tools/templates/` to adjust typography, margins, or section order while keeping single-column ATS compatibility.
* **Direct Headless Chrome PDF Export**: If you manually tweak `resume_render.html` and want to re-compile the PDF directly:
  * **Windows:**
    ```cmd
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="resume.pdf" resume_render.html
    ```
  * **macOS:**
    ```bash
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="resume.pdf" resume_render.html
    ```
  * **Linux:**
    ```bash
    google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="resume.pdf" resume_render.html
    ```

## ❓ Frequently Asked Questions (FAQ)

**Q: How does the ATS Matcher calculate my resume score?**  
Agent 5 (`AJDPrompts/ats-matcher.md`) evaluates your tailored resume against the target job description on a 0–100% scale weighted across seven hiring criteria: **Hard Skills (40%)**, **Job Keywords (20%)**, **Text Similarity (10%)**, **Job Title Alignment (10%)**, **Experience Tenure (8%)**, **ATS Formatting (7%)**, and **Soft Skills (5%)**.

**Q: What if a job posting asks for a skill I don't have in `master_data.json`?**  
The Truth Engine never fabricates unverified skills inside your Experience, Projects, or core Skills sections. Instead, if the skill is relevant to your target domain, it places it transparently under **Areas of Interest** so you capture legitimate keyword alignment without misrepresenting your background.

**Q: How can I recover my generated HTML or match report after cleaning up build folders?**  
Every completed run appends a `## REPAIR BUNDLE` section at the bottom of `prompt.md` containing the complete final `resume_render.html` and `job-match.json` blocks for instant restoration.

## 📄 License

Distributed under the [MIT License](https://github.com/CoderShubhamMate/agentic-resume-engine/blob/main/LICENSE). Feel free to clone, fork, and customize it for your job search!

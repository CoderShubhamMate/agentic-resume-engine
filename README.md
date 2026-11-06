# 📄 Agentic Resume Engine — AI ATS-Friendly Resume Builder & Job Description Tailor

**Autonomous 5-Agent AI Resume Tailor & ATS Resume Builder powered by Google Gemini (`@google/genai` SDK), Python, Jinja2, and Headless Chrome.**

An autonomous, agentic AI resume production pipeline that transforms job descriptions into **truthful**, **ATS-optimized**, **1-page PDF resumes** and companion **interview preparation guides** using your local AI coding assistant (Cursor, Antigravity, Windsurf, Claude Code, or VS Code) and Headless Chrome.

> **Zero-Fabrication Contract**: This engine enforces a strict truth boundary. It tailors resumes strictly using verified facts from your personal `Master_Data/` files and **never** hallucinates skills, employers, projects, or metrics to artificially inflate match scores.

## 🎯 Why Job Seekers Clone This ATS Resume Builder

The **Agentic Resume Engine** treats custom resume creation as an automated software compilation pipeline. Instead of spending 45+ minutes manually editing Word or LaTeX files for every job posting, you maintain one **Master Resume Data (`Master_Data/master_data.json`)** file containing your complete, verified career history.

Traditional AI resume generators frequently hallucinate credentials, invent fake percentages, or output multi-page documents that fail Applicant Tracking Systems (ATS).

**Agentic Resume Engine** treats resume tailoring like an engineering compilation pipeline with an AI agent-in-the-loop:

- 🛡️ **Master Data as Ground Truth:** The agent can NEVER add a skill, tool, or metric unless it exists in your verified `Master_Data/` markdown files.
- 📄 **Guaranteed 1-Page Layout:** Rendered via semantic HTML/CSS and compiled with Headless Chrome (`--print-to-pdf`) with sub-millimeter print margin guards.
- 🎯 **Deterministic ATS Scoring Loop:** Measures hard-skill keyword density, Minimum Qualifications (MQs), and ATS formatting with up to 3 truthful revision passes using `tools/match_resume.py`.
- 📦 **Disaster-Proof Repair Bundles:** Intermediate HTML and scoring state are automatically serialized into `prompt.md` comments before temporary build files are cleaned up.
- 💻 **Cross-Platform Compilation:** Built-in auto-detection for Google Chrome, Chromium, and Edge across Windows, macOS, and Linux via `tools/compile_pdf.py`.
- 🧠 **Companion Technical Interview Guides:** Automatically generates an 8-module technical systems engineering study guide for every application using `tools/generate_interview_prep.py`.
- 💰 **Zero API Key Cost:** Runs directly with your existing AI coding assistant (Antigravity, Cursor, Windsurf, Claude, Copilot). No extra paid API subscriptions required.

1. **Input Stage**: Raw Job Description (`jd.txt`) + Candidate Career Profile (`Master_Data/master_data.json`)
2. **Agent 1 — JD Analyst (`AJDPrompts/jd-analyst.md`)**: Extracts core technical skills, domain keywords, required tenure, and soft skills into a structured JD profile.
3. **Agent 2 — Section Planner (`AJDPrompts/section-planner.md`)**: Calculates strict visual line-budget limits per section to guarantee a single-page layout and selects your highest-impact items.
4. **Agent 3 — Truth Engine (`AJDPrompts/truth-engine.md`)**: Enforces zero-hallucination governance—maps verified history to JD keywords without inventing roles, skills, or metrics.
5. **Agent 4 — Resume Writer & Layout Guard (`AJDPrompts/resume-writer.md`)**: Compiles semantic HTML via Jinja2 templates (`tools/templates/`) with strict inline CSS formatting bounds.
6. **Agent 5 — ATS Matcher & Auditor (`AJDPrompts/ats-matcher.md`)**: Audits the compiled resume against the target JD across 7 weighted ATS dimensions and outputs `job-match.json`.

### 🤖 The 5-Agent Pipeline Breakdown

```mermaid
flowchart TD
    A["👤 User pastes target JD into AJDPrompts/Prompt.md"] --> B["AI Agent extracts:\n• Hard skills & MQs\n• ATS keywords\n• JD themes"]
    B --> C{"PRE-mode Analysis\ntools/match_resume.py"}
    C --> D[("Master_Data/*.md\nYour verified career facts")]
    D --> C
    C --> E["Agent classifies requirements:\n✅ Verified Matches\n⚠️ Partial Matches\n❌ True Gaps (Areas of Interest)"]
    E --> F["Agent crafts tailored resume\nresume.tex + resume_render.html"]
    F --> G["Headless Chrome compiles resume.pdf\n(Strict 1-Page Guarantee)"]
    G --> H{"POST-mode ATS Scoring\ntools/match_resume.py"}
    H --> I{"Score ≥ 90% or\n3 passes completed?"}
    I -- "No (Needs Revision)" --> J["Add verified_omitted facts naturally"]
    J --> F
    I -- "Yes" --> K["Embed Repair Bundle into prompt.md\nClean build artifacts"]
    K --> L["Generate Companion Interview Prep Guide\ntools/generate_interview_prep.py"]
    L --> M[("📁 Clean Application Package")]

## 🔒 Truth Engine: Zero-Hallucination Resume Tailoring

Unlike generic AI resume generators that invent fake skills to stuff keywords, the **Truth Engine** (`AJDPrompts/truth-engine.md`) enforces strict factual guardrails:

* **Verified Experience Only**: Every bullet point must originate from documented entries in `Master_Data/master_data.json`.
* **Smart Action-Verb & Keyword Alignment**: Phrasing and technical context are dynamically tailored to mirror the employer's exact terminology where your background genuinely matches.
* **Immutable Metrics**: Quantified impact numbers (percentages, latency reductions, revenue, scale) are preserved strictly as recorded in your master file.
* **Honest Skill-Gap Handling**: If a job description requires a tool or skill you haven't used yet, the engine never fakes it in your Experience or Skills sections—instead, it surfaces relevant domain terms transparently under **Areas of Interest** (e.g., *"Interested in developing expertise in: Kubernetes, Distributed Systems"*).

```mermaid
flowchart LR
    JD(["Job Description\nRequires: Kubernetes"]) --> V{"Is it in\nMaster_Data?"}
    V -- "✅ Verified" --> R["Added to resume\nbullet / skill line"]
    V -- "⚠️ Partial Match" --> P["Added with honest framing\ne.g. 'Docker, Containers'"]
    V -- "❌ Not Found" --> G["Reported as gap\nPlaced in 'Areas of Interest'\nNEVER fabricated"]

### Prerequisites

* **Python 3.10+**
* **Google Gemini API Key** (`GEMINI_API_KEY`)
* **Google Chrome** installed locally (used in headless mode for pixel-perfect PDF compilation)

### Step 1: Create Your Own Repository or Clone Locally

Every completed job application produces a pristine, isolated folder:

```
Akamai - Software Engineer/
├── prompt.md                               ← Target JD + prompt + Repair Bundle in comments
├── job-description.md                      ← Clean copy of the target JD
├── resume.pdf                              ← 1-page tailored ATS resume
├── job-match-report.pdf                    ← Scoring breakdown, keyword analysis, and gaps
└── Akamai_Software_Engineer_Interview_Prep.pdf ← Companion 8-module technical interview guide
```

---

## 🚀 Quick Start (5 Minutes)

### Option 1: AI Agent Setup Prompt (Recommended)

If you are using an AI coding assistant (**Antigravity**, **Cursor**, **Windsurf**, or **VS Code with Claude/Copilot**), simply paste this prompt into your agent chat:

```text
Initialize the Agentic Resume Engine in this workspace: run python setup.py, 
verify Google Chrome availability, and guide me through populating Master_Data/ 
with my verified background information!
```

### Option 2: Manual Terminal Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/CoderShubhamMate/agentic-resume-engine.git
   cd agentic-resume-engine
   ```

2. **Run 1-Click Bootstrap Wizard:**
   ```bash
   python setup.py
   ```
   *(Checks Python ≥ 3.10, auto-detects Google Chrome/Chromium/Edge, and installs dependencies from `tools/requirements.txt`)*

3. **Populate Your `Master_Data/`:**
   Edit the markdown files in `Master_Data/` with your real history:
   - `All_Info.md` — Core contact info, professional summary, and verified skills.
   - `Education_and_Skills.md` — Degree history, CGPA/percentages, and usage tiers (`strong`, `summary_only`, `cert_only`).
   - `Projects.md` — Locked project names, verified tech stacks, and publication links.
   - `Timeline.md` — Chronological master timeline across academic degrees and internships.

---

## 🎯 How to Tailor a Resume for Any Job

1. Open `AJDPrompts/Prompt.md` and paste the Job Description along with company details.
2. Tell your AI assistant:
   ```text
   Build a tailored application package for the job in AJDPrompts/Prompt.md 
   following the rules in .agents/rules/.
   ```
3. The agent will autonomously:
   - Run the PRE match check (`tools/match_resume.py --mode pre`).
   - Draft the tailored resume adhering to line-budget constraints.
   - Compile the 1-page PDF using `tools/compile_pdf.py`.
   - Run the POST scoring loop (`tools/match_resume.py --mode post`).
   - Generate the technical interview preparation guide (`tools/generate_interview_prep.py`).
   - Archive the build files into `prompt.md` and deliver the finished package.

---

## 📜 The 10-Rule Governance Suite

The engine is governed by 10 immutable operational rules located in `.agents/rules/`:

| Rule | File | Core Mandate |
| :---: | :--- | :--- |
| **00** | `00-meta-and-priority.md` | Meta rules, read-only protected locations, strict priority resolution. |
| **01** | `01-truthfulness.md` | Single source of truth in `Master_Data/`; zero-fabrication contract. |
| **02** | `02-project-naming-and-stacks.md` | Project names and stack lines are strictly locked to match your GitHub. |
| **03** | `03-tailoring-and-writing.md` | JD analysis, ATS keyword surfacing, professional summary framing. |
| **04** | `04-areas-of-interest.md` | Dedicated final section for unverified JD concepts (avoids fabrication). |
| **05** | `05-resume-template.md` | ATS-friendly monochrome left-rail layout template. |
| **06** | `06-build-pipeline.md` | Step-by-step compilation using cross-platform Headless Chrome. |
| **07** | `07-match-and-revision-loop.md` | Objective ATS scoring, pass thresholds, and revision loop termination. |
| **08** | `08-cleanup-and-file-safety.md` | Safe build artifact cleanup and `prompt.md` Repair Bundle archiving. |
| **09** | `09-validation-and-final-response.md` | Pre-flight validation checklist before delivering final files. |
| **10** | `10-security-and-credentials-policy.md` | Credential security policy: zero password or token leaks. |

---

## 🛠 Repository Structure

```text
agentic-resume-engine/
├── .agents/
│   └── rules/                     # The 10-rule agent governance suite
│       ├── 00-meta-and-priority.md
│       ├── 01-truthfulness.md
│       ├── ...
│       └── 10-security-and-credentials-policy.md
├── AJDPrompts/
│   └── Prompt.md                  # Input workspace for target job descriptions
├── Master_Data/                   # Single source of truth for your career history
│   ├── All_Info.md
│   ├── Education_and_Skills.md
│   ├── Projects.md
│   └── Timeline.md
├── examples/                      # Reference examples of prompts and master data
│   ├── job_prompt_example.md
│   └── Master_Data/
├── tools/                         # CLI automation scripts
│   ├── compile_pdf.py             # Headless Chrome/Edge cross-platform PDF compiler
│   ├── match_resume.py            # Objective ATS keyword and gap scoring engine
│   ├── generate_interview_prep.py # Companion 8-module technical interview guide builder
│   ├── master_resume_template.html# ATS semantic HTML/CSS base template
│   ├── master_resume_template.tex # LaTeX layout reference
│   ├── MATCH_RULES.md             # ATS scoring algorithms & weights
│   └── requirements.txt           # Python tool dependencies
├── LICENSE                        # MIT License
├── README.md                      # Documentation
└── setup.py                       # 1-click bootstrap wizard
```

---

## 💻 CLI Tools Reference

### 1. Compile PDF via Headless Chrome (`tools/compile_pdf.py`)
Auto-detects Google Chrome, Chromium, or Microsoft Edge across OS environments:
```bash
git clone https://github.com/CoderShubhamMate/agentic-resume-engine.git
cd agentic-resume-engine
```

### 2. ATS Match & Gap Scorer (`tools/match_resume.py`)
Run in PRE mode before writing, or POST mode to evaluate the compiled PDF:
```bash
# Pre-writing requirement analysis
python tools/match_resume.py --mode pre --folder "Company - Role"

# Post-compilation ATS score check
python tools/match_resume.py --mode post --folder "Company - Role"
```

### 3. Interview Preparation Guide Generator (`tools/generate_interview_prep.py`)
Generates an 8-module comprehensive systems engineering interview prep guide:
```bash
python tools/generate_interview_prep.py --folder "Company - Role"
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

<details>
<summary><strong>Q: How does the ATS Matcher score resumes?</strong></summary>
The score (0–100%) is calculated across weighted components: Hard Skills (40%), Job Keywords (20%), Text Similarity (10%), Job Title Alignment (10%), Experience Tenure (8%), ATS Formatting (7%), and Soft Skills (5%).
</details>

<details>
<summary><strong>Q: Do I need a Google Gemini or OpenAI API key to use this?</strong></summary>
No. The engine is powered directly by your local AI coding assistant (Antigravity, Cursor, Windsurf, Claude Code, GitHub Copilot) reading the governance rules in <code>.agents/rules/</code> and executing the local Python tools in <code>tools/</code>.
</details>

---

## 📄 License

Distributed under the [MIT License](https://github.com/CoderShubhamMate/agentic-resume-engine/blob/main/LICENSE). Feel free to clone, fork, and customize it for your job search!

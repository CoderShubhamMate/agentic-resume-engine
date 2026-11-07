# ⚡ Agentic Resume Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Zero Fabrication](https://img.shields.io/badge/Policy-Zero%20Fabrication-red.svg)]()
[![Output](https://img.shields.io/badge/Output-1--Page%20ATS%20PDF-success.svg)]()

An autonomous, agentic AI resume production pipeline that transforms job descriptions into **truthful**, **ATS-optimized**, **1-page PDF resumes** and companion **interview preparation guides** using your local AI coding assistant (Cursor, Antigravity, Windsurf, Claude Code, or VS Code) and Headless Chrome.

> **Zero-Fabrication Contract**: This engine enforces a strict truth boundary. It tailors resumes strictly using verified facts from your personal `Master_Data/` files and **never** hallucinates skills, employers, projects, or metrics to artificially inflate match scores.

---

## 🌟 Why Agentic Resume Engine?

Traditional AI resume generators frequently hallucinate credentials, invent fake percentages, or output multi-page documents that fail Applicant Tracking Systems (ATS).

**Agentic Resume Engine** treats resume tailoring like an engineering compilation pipeline with an AI agent-in-the-loop:

- 🛡️ **Master Data as Ground Truth:** The agent can NEVER add a skill, tool, or metric unless it exists in your verified `Master_Data/` markdown files.
- 📄 **Guaranteed 1-Page Layout:** Rendered via semantic HTML/CSS and compiled with Headless Chrome (`--print-to-pdf`) with sub-millimeter print margin guards.
- 🎯 **Deterministic ATS Scoring Loop:** Measures hard-skill keyword density, Minimum Qualifications (MQs), and ATS formatting with up to 3 truthful revision passes using `tools/match_resume.py`.
- 📦 **Disaster-Proof Repair Bundles:** Intermediate HTML and scoring state are automatically serialized into `prompt.md` comments before temporary build files are cleaned up.
- 💻 **Cross-Platform Compilation:** Built-in auto-detection for Google Chrome, Chromium, and Edge across Windows, macOS, and Linux via `tools/compile_pdf.py`.
- 🧠 **Companion Technical Interview Guides:** Automatically generates an 8-module technical systems engineering study guide for every application using `tools/generate_interview_prep.py`.
- 💰 **Zero API Key Cost:** Runs directly with your existing AI coding assistant (Antigravity, Cursor, Windsurf, Claude, Copilot). No extra paid API subscriptions required.

---

## 🏗️ Architecture & How It Works

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

    style A fill:#4f46e5,color:#fff
    style M fill:#16a34a,color:#fff
    style D fill:#b45309,color:#fff
    style C fill:#0f172a,color:#fff
    style H fill:#0f172a,color:#fff
```

---

## 🛡️ Truth Engine: What Gets Into Your Resume

```mermaid
flowchart LR
    JD(["Job Description\nRequires: Kubernetes"]) --> V{"Is it in\nMaster_Data?"}
    V -- "✅ Verified" --> R["Added to resume\nbullet / skill line"]
    V -- "⚠️ Partial Match" --> P["Added with honest framing\ne.g. 'Docker, Containers'"]
    V -- "❌ Not Found" --> G["Reported as gap\nPlaced in 'Areas of Interest'\nNEVER fabricated"]

    style JD fill:#4f46e5,color:#fff
    style R fill:#16a34a,color:#fff
    style P fill:#b45309,color:#fff
    style G fill:#dc2626,color:#fff
```

---

## 📦 Output: Clean Application Package

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

## 🤖 How to Use with Antigravity, Cursor & AI Coding Assistants

The Agentic Resume Engine is engineered specifically to pair-program with modern autonomous coding agents. The agent autonomously reads the 10 immutable governance rules in `.agents/rules/`, uses your `Master_Data/` as ground truth, and executes the CLI tools in `tools/` without hallucinating experience.

### 🌟 1. Google Antigravity
Antigravity automatically discovers and obeys the rules in `.agents/rules/` across all conversation turns.
* **Workflow:**
  1. Open the repository root in Antigravity.
  2. Paste your target Job Description into `AJDPrompts/Prompt.md`.
  3. Send this instruction in the Antigravity chat:
     ```text
     Read .agents/rules/ and build a tailored application package for the job in AJDPrompts/Prompt.md. Strictly enforce the zero-fabrication contract and 1-page PDF guarantee.
     ```
  4. Antigravity will autonomously:
     - Run `tools/match_resume.py --mode pre` to classify verified matches vs gaps.
     - Author `resume.tex` and mirror it in `resume_render.html`.
     - Compile `resume.pdf` using `tools/compile_pdf.py` with headless Chrome.
     - Run the revision loop (`match_resume.py --mode post`) until the score reaches ≥ 90% or 3 truthful passes complete.
     - Generate the companion 8-module systems engineering interview guide (`tools/generate_interview_prep.py`).
     - Embed the disaster-proof `## REPAIR BUNDLE` into `prompt.md` and clean up temporary build artifacts.

### ⚡ 2. Cursor (Agent Mode / Composer)
* **Workflow:**
  1. Open the repository in Cursor.
  2. Open **Composer** (`Ctrl+I` on Windows/Linux or `Cmd+I` on macOS) and select **Agent Mode**.
  3. Tag the rules and prompt:
     ```text
     @.agents/rules @AJDPrompts/Prompt.md Build the tailored resume package for this job following rules 00 through 10.
     ```
  4. Cursor will run the terminal commands, verify the layout constraints, and deliver the final application folder.

### 🌊 3. Windsurf (Cascade Agent)
* **Workflow:**
  1. Open the project in Windsurf and switch to Cascade.
  2. Send:
     ```text
     Follow the pipeline in .agents/rules/ to tailor my resume for the job in AJDPrompts/Prompt.md using Master_Data as the single source of truth.
     ```

### 💻 4. Claude Code / CLI Coding Agents
* **Workflow:**
  1. Launch `claude` or your preferred terminal agent in the repository root:
     ```bash
     claude
     ```
  2. Prompt:
     ```text
     Follow the step-by-step build pipeline in .agents/rules/06-build-pipeline.md to create the application package for AJDPrompts/Prompt.md.
     ```

---

## 🎯 Step-by-Step Resume Tailoring Walkthrough

Here is what happens during a complete resume tailoring run:

| Step | Phase | Autonomous Agent Action | Tool / Target |
| :---: | :--- | :--- | :--- |
| **1** | **Input** | Paste target company name, role title, and raw JD text | `AJDPrompts/Prompt.md` |
| **2** | **Pre-Scoring** | Extracts MQs, hard skills, ATS keywords; checks against verified history | `python tools/match_resume.py --mode pre --folder "<Company> - <Role>"` |
| **3** | **Drafting** | Authors semantic ATS HTML (`resume_render.html`) and LaTeX (`resume.tex`) | Adheres strictly to `tools/master_resume_template.html` |
| **4** | **Compilation** | Compiles selectable-text PDF using Headless Chrome print engine | `python tools/compile_pdf.py --html resume_render.html --pdf resume.pdf` |
| **5** | **Post-Scoring** | Audits output ATS match score (0–100%) and runs up to 3 revision passes | `python tools/match_resume.py --mode post --folder "<Company> - <Role>"` |
| **6** | **Interview Prep** | Generates companion 8-module deep technical interview preparation guide | `python tools/generate_interview_prep.py --folder "<Company> - <Role>"` |
| **7** | **Safety & Cleanup** | Serializes final HTML and match score into `## REPAIR BUNDLE` inside `prompt.md` | Cleans temporary build files, leaving exactly 4 production deliverables |

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
python tools/compile_pdf.py --html resume_render.html --pdf resume.pdf
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

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><strong>Q: What happens if a job requires a skill I do not have?</strong></summary>
The engine will never fabricate it in your Skills, Experience, or Projects sections. If the concept is relevant to the domain, it places it honestly into the <strong>Areas of Interest</strong> section (e.g., <em>"Interested in developing expertise in: Kubernetes, Distributed Systems"</em>). This allows you to surface relevant ATS keywords without being untruthful.
</details>

<details>
<summary><strong>Q: How do I restore build files after cleanup?</strong></summary>
Every completed run embeds a <code>## REPAIR BUNDLE</code> at the bottom of <code>prompt.md</code> containing the full final <code>resume_render.html</code> and <code>job-match.json</code>. You can copy the HTML block directly to restore the editable source code at any time.
</details>

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

This project is licensed under the [MIT License](LICENSE).

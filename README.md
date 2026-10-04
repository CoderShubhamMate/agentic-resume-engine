# 🚀 Agentic Resume Engine

An AI-agent-powered automated resume production pipeline that transforms job descriptions into **truthful**, **ATS-optimized**, **1-page PDF resumes** and **match report PDFs** using Headless Chrome.

> [!IMPORTANT]
> **Zero-Fabrication Policy**: This engine enforces a strict truth boundary. It tailors resumes strictly using verified facts from your personal `Master_Data/` files and will **never** invent skills or experience to artificially inflate match scores.

---

## ⚡ Instant Setup via AI Agent Prompt (One-Prompt Setup)

If you are using an AI-enabled IDE or Agent (such as **Antigravity**, **Cursor**, **Windsurf**, or **VS Code with AI Agent**), simply open your AI chat and paste this prompt:

> 💬 **Copy & Paste Prompt into your AI Agent:**
> ```text
> Clone the Agentic Resume Engine repository from https://github.com/CoderShubhamMate/agentic-resume-engine.git, set up the Python environment (.venv) using tools/requirements.txt, and guide me on updating the Master_Data/ files with my verified background information so I can generate tailored 1-page ATS resumes!
> ```

The AI agent will automatically clone the repository, install Python dependencies, and walk you through populating your verified candidate facts!

---

## ✨ Key Features

- 🎯 **Automated Job Description Analysis**: Extracts hard skill requirements, soft skills, and Minimum Qualifications (MQs).
- 🛡️ **Truth Engine Verification**: Validates every skill against your `Master_Data/` repository before adding it to the resume.
- 📄 **1-Page Visual Guarantee**: Renders HTML/CSS via Headless Chrome (`--print-to-pdf`) to ensure crisp formatting and strict 1-page compliance.
- 📊 **ATS Match & Scoring Engine**: Computes objective keyword match scores (0–100%) and exports a detailed `job-match-report.pdf`.
- 🧹 **Clean 4-File Application Isolation**: Every application receives a dedicated folder containing only 4 clean files:
  1. `prompt.md` (Preserved input prompt)
  2. `job-description.md` (Clean job description)
  3. `resume.pdf` (1-page tailored resume)
  4. `job-match-report.pdf` (Scoring & match report)

---

## 🛠️ System Requirements

- **Python 3.10+**
- **Google Chrome** (for headless PDF generation)
- **AI Coding Assistant** (Antigravity, Gemini, or Claude) capable of reading `.agents/rules/`.

---

## 🚀 Manual Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/CoderShubhamMate/agentic-resume-engine.git
cd agentic-resume-engine
```

### 2. Set Up Python Environment
```bash
python -m venv .venv

# On Windows PowerShell:
.\.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

pip install -r tools/requirements.txt
```

### 3. Personalize `Master_Data/` (Your Source of Truth)
Replace the placeholder files in `Master_Data/` with your verified background details:
- `Master_Data/All_Info.md`: Your complete contact details, work history, skills, and projects.
- `Master_Data/Education_and_Skills.md`: Your verified technical skills grouped into categories.
- `Master_Data/Projects.md`: Verified project details, team sizes, tech stacks, and outcomes.
- `Master_Data/Background.md`: Target roles and location preferences.

---

## 🎯 Generating a Tailored Resume via AI Agent

Whenever you want to apply for a new job, simply paste this prompt into your AI Agent:

> 💬 **Copy & Paste Prompt for any Job Application:**
> ```text
> I want to generate a tailored resume application package.
> 
> Company: [Company Name]
> Role: [Job Title]
> Location: [Location]
> 
> Job Description:
> [Paste full raw job description here]
> 
> Please write this to AJDPrompts/Prompt.md and process the resume generation pipeline.
> ```

The AI Agent will automatically:
1. Parse the JD and run PRE-mode keyword analysis.
2. Tailor your resume strictly using verified facts from `Master_Data/`.
3. Compile a 1-page `resume.pdf` via Headless Chrome.
4. Run POST-mode ATS scoring and optimization passes.
5. Produce `job-match-report.pdf` and clean up all temporary build files!

---

## 📄 License

[MIT License](LICENSE)

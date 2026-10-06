---
trigger: always_on
---

# 05 — RESUME TEMPLATE AND DESIGN

## 5.1 Design (fixed)
One-page, ATS-friendly, monochrome technical resume: centered name and compact contact line, clear section hierarchy, thin dividers, dense but readable, consistent alignment and spacing.
Never use: photos, graphics, skill bars, rating stars, decorative cards, extra colors, unnecessary visual elements.
Never shrink the font to an unreadable size just to fit one page.

## 5.2 Section order (fixed)
1. Professional Summary
2. Skills
3. Work History
4. Projects
5. Education
6. Certifications
7. Areas of Interest

## 5.3 How to use the template
- EVERY job starts from the canonical LaTeX template below. Never start from another job's `resume.tex`, `resume_render.html` or PDF.
- Replace every `[...]` placeholder.
- Fixed lines (header, role titles, dates, employer names, project names and stacks, education) stay as written. They must equal Master_Data and `01`/`02`. If Master_Data differs, Master_Data wins and you report the difference.
- Every content change is made in BOTH `resume.tex` and `resume_render.html` (see 06).

## 5.4 LaTeX template

```latex
\documentclass[10pt,letterpaper]{article}
\usepackage[left=0.5in, right=0.5in, top=0.5in, bottom=0.5in]{geometry}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

\pagestyle{empty}
\definecolor{lightgray}{gray}{0.85}

\newcommand{\cvsection}[2]{
    \vspace{6pt}
    \noindent
    \begin{minipage}[t]{0.22\textwidth}
        \vspace{0pt} 
        {\color{lightgray}\rule{0.9\linewidth}{4pt}}\par
        \vspace{2pt}\small\textbf{\uppercase{#1}}
    \end{minipage}%
    \hfill
    \begin{minipage}[t]{0.75\textwidth}
        \vspace{0pt} 
        \vspace{-2.5pt}\rule{\linewidth}{0.5pt}\par
        \vspace{2pt}\small #2
    \end{minipage}
}

\begin{document}

\begin{center}
    {\huge \textbf{[FULL NAME]}} \\[4pt]
    \small [City, State/Country] $|$ [+Country-Code Phone] $|$ \href{mailto:[email@example.com]}{[email@example.com]} $|$ \href{https://linkedin.com/in/[linkedin-id]}{LinkedIn} $|$ \href{https://github.com/[github-id]}{GitHub}
\end{center}
\vspace{6pt}

\cvsection{Professional Summary}{
    [Early-career / mid-level engineer summary highlighting core verified languages, systems experience, and technical focus relevant to the target role. Strictly objective, 2-3 sentences. No company names or cover-letter phrasing.]
}

\cvsection{Skills}{
    \textbf{Languages:} [Verified Languages, e.g. Python, Java, JavaScript, TypeScript, SQL] \newline
    \textbf{Frameworks \& APIs:} [Verified Frameworks, e.g. FastAPI, Spring Boot, Node.js, REST APIs] \newline
    \textbf{Databases:} [Verified Databases, e.g. PostgreSQL, MySQL, Redis] \newline
    \textbf{Tools \& Concepts:} [Verified Tools, e.g. Docker, Git, GitHub, Postman, CI/CD, Agile]
}

\cvsection{Work History}{
    \textbf{[ROLE TITLE 1]} $|$ [Company Name 1] \hfill \textit{[MM/YYYY to MM/YYYY]} \newline
    [City, State/Country]
    \begin{itemize}[leftmargin=*, nosep, topsep=2pt]
        \item [Action verb] + [Technology/Context] + [Work done] + [Purpose/Result].
        \item [Investigated application behavior, utilizing systematic debugging to isolate and resolve edge cases].
        \item [Collaborated with cross-functional engineering teams to deliver verified backend features].
    \end{itemize}
    \vspace{6pt}
    
    \textbf{[ROLE TITLE 2]} $|$ [Company Name 2] \hfill \textit{[MM/YYYY to MM/YYYY]} \newline
    [City, State/Country]
    \begin{itemize}[leftmargin=*, nosep, topsep=2pt]
        \item [Developed modular application components adhering strictly to clean code specifications].
        \item [Executed comprehensive unit and integration testing to uncover and address implementation flaws].
    \end{itemize}
}

\cvsection{Projects}{
    \textbf{[Project Title 1]} $|$ \textit{[Verified Tech Stack 1]}
    \begin{itemize}[leftmargin=*, nosep, topsep=2pt]
        \item [Engineered core services and data ingestion pipelines, ensuring robust validation].
        \item [Executed comprehensive API and workflow testing to validate application performance].
    \end{itemize}
    \vspace{6pt}
    \textbf{[Project Title 2]} $|$ \textit{[Verified Tech Stack 2]}
    \begin{itemize}[leftmargin=*, nosep, topsep=2pt]
        \item [Developed full-stack application logic connecting client interfaces to backend datastores].
        \item [Integrated automated workflows with structured error-handling to prevent data discrepancies].
    \end{itemize}
}

\cvsection{Education}{
    \textbf{[University / College Name]} \newline
    [Degree Name, Major, Graduated Month Year] \vspace{4pt}\newline
    \textbf{[Polytechnic / High School Name]} \newline
    [Diploma / Certificate Name, Score, Graduated Year]
}

\cvsection{Certifications}{
    [Certification 1] $|$ [Certification 2] $|$ [Certification 3]
}

\cvsection{Areas of Interest}{
    Interested in developing expertise in: [3 to 8 relevant JD technologies or emerging architectural concepts].
}

\end{document}
```

#!/usr/bin/env python3
"""
compile_pdf.py - Cross-platform Headless Chrome / Chromium PDF compiler.
Automatically locates the browser binary on Windows, macOS, and Linux
and compiles an HTML resume into a clean 1-page PDF.
"""

import os
import sys
import shutil
import argparse
import subprocess
from pathlib import Path

def find_chrome_binary():
    """Locate Google Chrome, Chromium, or Edge across operating systems."""
    # 1. Check user override from environment
    if os.environ.get("CHROME_BIN"):
        custom = Path(os.environ["CHROME_BIN"])
        if custom.is_file():
            return str(custom)

    # 2. Check standard PATH entries
    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "chrome",
        "msedge",
    ]
    for c in candidates:
        found = shutil.which(c)
        if found:
            return found

    # 3. Platform-specific known standard installation paths
    if sys.platform.startswith("win"):
        win_paths = [
            Path(os.environ.get("ProgramFiles", "C:\\Program Files")) / "Google\\Chrome\\Application\\chrome.exe",
            Path(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")) / "Google\\Chrome\\Application\\chrome.exe",
            Path(os.environ.get("LocalAppData", "")) / "Google\\Chrome\\Application\\chrome.exe",
            Path(os.environ.get("ProgramFiles", "C:\\Program Files")) / "Microsoft\\Edge\\Application\\msedge.exe",
            Path(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")) / "Microsoft\\Edge\\Application\\msedge.exe",
        ]
        for p in win_paths:
            if p.is_file():
                return str(p)

    elif sys.platform == "darwin":  # macOS
        mac_paths = [
            Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
            Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
            Path.home() / "Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ]
        for p in mac_paths:
            if p.is_file():
                return str(p)

    else:  # Linux / BSD / Unix
        linux_paths = [
            Path("/usr/bin/google-chrome"),
            Path("/usr/bin/google-chrome-stable"),
            Path("/usr/bin/chromium"),
            Path("/usr/bin/chromium-browser"),
            Path("/snap/bin/chromium"),
            Path("/usr/bin/microsoft-edge"),
        ]
        for p in linux_paths:
            if p.is_file():
                return str(p)

    return None

def compile_pdf(html_path: Path, pdf_path: Path, chrome_bin: str = None):
    html_file = html_path.resolve()
    pdf_file = pdf_path.resolve()

    if not html_file.is_file():
        print(f"Error: HTML input file not found: {html_file}", file=sys.stderr)
        return False

    chrome_exec = chrome_bin or find_chrome_binary()
    if not chrome_exec:
        print("Error: Could not locate Google Chrome or Chromium executable.", file=sys.stderr)
        print("Please set CHROME_BIN environment variable pointing to the browser binary.", file=sys.stderr)
        return False

    # Build local file URL
    file_url = html_file.as_uri()

    cmd = [
        chrome_exec,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={str(pdf_file)}",
        file_url
    ]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if pdf_file.is_file() and pdf_file.stat().st_size > 0:
            print(f"Successfully compiled: {pdf_file.name} ({pdf_file.stat().st_size} bytes)")
            return True
        else:
            print("Error: Headless Chrome finished but PDF was not created.", file=sys.stderr)
            if res.stderr:
                print(res.stderr, file=sys.stderr)
            return False
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed with exit code {e.returncode}:", file=sys.stderr)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Cross-platform Headless Chrome HTML-to-PDF compiler.")
    parser.add_argument("--html", required=True, help="Path to input HTML file (e.g. resume_render.html)")
    parser.add_argument("--pdf", required=True, help="Path to output PDF file (e.g. resume.pdf)")
    parser.add_argument("--chrome-bin", help="Optional explicit path to Chrome or Chromium binary")

    args = parser.parse_args()
    success = compile_pdf(Path(args.html), Path(args.pdf), args.chrome_bin)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()


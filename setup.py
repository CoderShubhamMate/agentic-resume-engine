#!/usr/bin/env python3
"""
setup.py - 1-Click Bootstrap & Environment Verification Script
Verifies system dependencies, Python version, Chrome availability,
and initializes the agentic resume workspace.
"""

import sys
import subprocess
import shutil
from pathlib import Path

MIN_PYTHON = (3, 10)

def check_python_version():
    if sys.version_info < MIN_PYTHON:
        print(f"❌ Error: Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ is required.")
        print(f"   Currently running: Python {sys.version.split()[0]}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]} (Supported)")

def check_chrome():
    tools_dir = Path(__file__).resolve().parent / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))

    try:
        import compile_pdf
        chrome_path = compile_pdf.find_chrome_binary()
        if chrome_path:
            print(f"✅ Headless Browser: Found at '{chrome_path}'")
            return True
        else:
            print("⚠️ Warning: Google Chrome or Chromium executable was not automatically detected.")
            print("   Please install Google Chrome or set the CHROME_BIN environment variable.")
            return False
    except Exception as e:
        print(f"⚠️ Warning: Could not check browser: {e}")
        return False

def verify_directories():
    base_dir = Path(__file__).resolve().parent
    master_data = base_dir / "Master_Data"
    rules_dir = base_dir / ".agents" / "rules"

    if master_data.is_dir():
        md_files = list(master_data.glob("*.md"))
        print(f"✅ Master_Data: {len(md_files)} specification files found.")
    else:
        print("❌ Error: Master_Data/ directory is missing.")

    if rules_dir.is_dir():
        rule_files = list(rules_dir.glob("*.md"))
        print(f"✅ Governance Rules: {len(rule_files)} rules verified in .agents/rules/.")
    else:
        print("❌ Error: .agents/rules/ directory is missing.")

def install_dependencies():
    req_file = Path(__file__).resolve().parent / "tools" / "requirements.txt"
    if not req_file.is_file():
        print("⚠️ Warning: tools/requirements.txt not found.")
        return

    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
        print("✅ Dependencies successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")

def main():
    print("=" * 60)
    print("⚡ Agentic Resume Engine — Environment Bootstrap")
    print("=" * 60)

    check_python_version()
    check_chrome()
    verify_directories()
    install_dependencies()

    print("\n🎉 Setup verified successfully!")
    print("\nNext steps:")
    print("1. Populate your real achievements in Master_Data/")
    print("2. Drop your target Job Description into prompt.md")
    print("3. Ask your AI coding agent (Antigravity, Cursor, Windsurf) to generate your resume!\n")

if __name__ == "__main__":
    main()

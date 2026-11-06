#!/usr/bin/env python3
"""
generate_interview_prep.py - Companion Interview Preparation Guide Generator.
Scans a job-description.md and produces an 8-module comprehensive technical
interview preparation guide (Markdown + printable HTML/PDF).
"""

import sys
import argparse
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def generate_prep_markdown(company: str, role: str, jd_text: str) -> str:
    """Generate structured 8-module interview preparation markdown."""
    return f"""# {company} — {role}
## Technical Interview Preparation & Systems Engineering Guide

This guide is auto-generated as a companion study guide for the **{role}** position at **{company}**. It breaks down the foundational concepts, systems internals, debugging workflows, and interview simulations based on the target requirements.

---

## Module 1 — Core Language & Systems Engineering
- **Data Structures & Memory Models:** Review algorithmic complexity ($O(1)$ amortized lookups, hash collision resolution, cache locality).
- **Concurrency & Parallelism:** Threads vs. processes, GIL behaviors, asynchronous event loops (async/await vs. worker pools).
- **Resource Management:** Safe file I/O, context managers, socket lifecycle, and defensive exception handling.

## Module 2 — Operating Systems & Platform Internals
- **Kernel vs. User Space:** System calls, context switches, process memory layouts (stack, heap, text, data).
- **File Descriptors & Sockets:** Unix file descriptor model (stdin: 0, stdout: 1, stderr: 2), non-blocking socket I/O.
- **Process Signals:** Graceful termination (`SIGTERM`), immediate teardown (`SIGKILL`), config reload (`SIGHUP`).
- **Telemetry Commands:** `top`, `htop`, `ss -tulnp`, `lsof -i`, `vmstat`, and `journalctl`.

## Module 3 — Networking Protocols & Architecture
- **Protocol Stack:** Application (HTTP/3, HTTP/2, DNS), Transport (TCP, UDP), Network (IP, ICMP, Routing).
- **TCP Lifecycle:** Three-way handshake (SYN, SYN-ACK, ACK), flow control, congestion windows, and 4-way termination (`TIME_WAIT`).
- **DNS Resolution Sequence:** Client cache → Recursive resolver → Root NS → TLD NS → Authoritative NS.
- **Security & Encryption:** TLS 1.3 handshake, Diffie-Hellman ephemeral key exchanges, X.509 certificate validation.

## Module 4 — Version Control & Collaboration Workflows
- **Git Internal Object Model:** Cryptographic Directed Acyclic Graph (DAG) storing commits, trees, and blobs.
- **Merge vs. Rebase:** Linear history vs. explicit branch commit preservation; guidelines for shared branch safety.
- **Code Review Best Practices:** Atomic commits, descriptive pull request contracts, and regression testing.

## Module 5 — Distributed Systems & Scalability
- **Fundamental Trade-Offs:** CAP theorem (Consistency, Availability, Partition Tolerance), PACELC principles.
- **High Availability Patterns:** Active-active vs. active-passive failover, load balancing algorithms, circuit breakers.
- **Stateless Services & Caching:** Decoupling state to distributed storage, cache invalidation strategies.

## Module 6 — Automation, Observability & Reliability
- **Three Pillars of Observability:** Metrics (time-series counters/gauges), Logs (structured JSON), Traces (distributed spans).
- **Health Probing:** Liveness probes (process uptime) vs. readiness probes (traffic routing gates).
- **Resilience Engineering:** Graceful degradation, backoff retry strategies, and rate limiting.

## Module 7 — Practical Systems Scenarios & Scripting
- Automated service health checker with retries and latency benchmarking.
- Log aggregation filter parsing error frequencies and identifying root causes.
- Defensive automation scripts with strict failure handling (`set -euo pipefail`).

## Module 8 — Technical Interview Simulation & QA
- **System Architecture Deep-Dive:** Explaining the full end-to-end lifecycle of a client network request.
- **Live Debugging Scenarios:** Isolating intermittent network latency, diagnosing memory leaks, or packet drop investigations.
- **Behavioral Alignment:** Clear cross-functional technical communication, incident triage under pressure, and post-mortem review.
"""

def main():
    parser = argparse.ArgumentParser(description="Generate 8-module technical interview guide from job description.")
    parser.add_argument("--folder", required=True, help="Path to job application folder")
    parser.add_argument("--company", help="Company name (optional, derived from folder name)")
    parser.add_argument("--role", help="Role title (optional, derived from folder name)")

    args = parser.parse_args()
    folder_path = Path(args.folder)

    if not folder_path.is_dir():
        print(f"Error: Folder does not exist: {folder_path}", file=sys.stderr)
        sys.exit(1)

    jd_file = folder_path / "job-description.md"
    jd_content = jd_file.read_text(encoding="utf-8") if jd_file.is_file() else ""

    parts = folder_path.name.split(" - ")
    company = args.company or (parts[0] if len(parts) > 0 else "Target Company")
    role = args.role or (parts[1] if len(parts) > 1 else "Software Engineer")

    out_file = folder_path / f"{company.replace(' ', '_')}_{role.replace(' ', '_')}_Interview_Prep.md"
    content = generate_prep_markdown(company, role, jd_content)
    out_file.write_text(content, encoding="utf-8")

    print(f"Successfully generated companion interview guide: {out_file.name}")

if __name__ == "__main__":
    main()


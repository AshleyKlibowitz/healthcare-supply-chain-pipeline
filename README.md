# Phase 1: Generate Data & PII Scrubber

Instructions to generate fake shipping data and scrub the `PatientName` column with SHA-256.

Prerequisites

- Python 3.8+
- A code editor (VS Code recommended)

Setup

1. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run

```bash
python3 generate_and_scrub.py
```

This will create `raw_shipping_data.csv` and `scrubbed_shipping_data.csv` in the project directory. The `PatientName` column in the scrubbed file is replaced with a SHA-256 hex digest.

# Local Setup

## Requirements

- Python 3.11 or newer
- Git

## Installation

```bash
git clone <repository-url>
cd agentic-engineering-foundation
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify Day 1:

```bash
python day01-agent-architecture/solution/agent_loop.py
```

Deactivate the environment with `deactivate` when finished.

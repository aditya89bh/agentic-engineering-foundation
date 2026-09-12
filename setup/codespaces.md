# GitHub Codespaces Setup

This repository includes a Python 3.11 dev container.

1. Open the repository on GitHub.
2. Select **Code**, then **Codespaces**.
3. Select **Create codespace on main** (or on your working branch).
4. When the terminal opens, verify the interpreter:

   ```bash
   python --version
   ```

5. Run the Day 1 solution:

   ```bash
   python day01-agent-architecture/solution/agent_loop.py
   ```

The container installs `requirements.txt`. Day 1 uses only the Python standard library, so it works even before any third-party packages are added.

Commit and push work from the Source Control panel or the terminal. Never commit secrets; Codespaces secrets can be configured in your GitHub settings if a later lesson requires an API key.

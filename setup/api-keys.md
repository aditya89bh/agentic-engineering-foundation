# API Key Safety

Day 1 does not require an API key. Its policy is deterministic and all supplier data is local.

For later lessons:

1. Create a `.env` file locally only if the lesson instructs you to do so.
2. Keep `.env` ignored by Git.
3. Prefer environment variables, secret managers, or Codespaces secrets over hard-coded keys.
4. Never paste a key into source code, notebooks, screenshots, issues, or pull requests.
5. Use restricted, course-specific keys where the provider supports them.
6. Revoke and rotate a key immediately if it is exposed.

Example shell variable:

```bash
export PROVIDER_API_KEY="replace-with-your-key"
```

Read it in Python without printing it:

```python
import os

api_key = os.environ.get("PROVIDER_API_KEY")
if not api_key:
    raise RuntimeError("PROVIDER_API_KEY is not configured")
```

# API Key Safety

The deterministic Day 1 runtime does not require an API key. The optional Day 1 LLM-policy exercise does.

## Rules

1. Keep API keys in environment variables, Codespaces secrets, or a secret manager.
2. Never hard-code a key in source code.
3. Never commit a `.env` file containing secrets.
4. Never paste keys into screenshots, issues, pull requests, notebooks, or logs.
5. Prefer restricted, course-specific keys where the provider supports them.
6. Revoke and rotate a key immediately if it is exposed.

For the optional Day 1 OpenAI example:

```bash
export OPENAI_API_KEY="replace-with-your-key"
export OPENAI_MODEL="model-available-to-your-account"
```

The code reads these values from the environment and does not print them.

```python
import os

api_key = os.environ.get("OPENAI_API_KEY")
model = os.environ.get("OPENAI_MODEL")

if not api_key or not model:
    raise RuntimeError("OPENAI_API_KEY and OPENAI_MODEL must be configured")
```

The course intentionally keeps the model name configurable rather than hard-coding one model into the curriculum.

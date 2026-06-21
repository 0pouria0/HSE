# PentestAI (skeleton)

This repository contains the foundational skeleton for PentestAI: configuration, database models, tool abstractions, parsers, and an AI orchestration skeleton.

Quick start (development):

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -e .
```

2. Copy `.env.example` to `.env` and set `DATABASE_URL` / API keys as needed.

3. Initialize the database and create a sample project:

```bash
python scripts/init_db.py
```

Files of interest:
- `pentestai/core/config.py` — Pydantic settings and YAML loading
- `pentestai/core/database.py` — DB init and session factory
- `pentestai/models/` — SQLAlchemy models and JSON mixin
- `pentestai/tools/` — Base tool API, schemas, registry, and example tool wrappers
- `pentestai/parsers/` — Parsing engine and normalizer/deduplicator
- `pentestai/ai/` — AI client and orchestration skeleton

Next steps: implement remaining tool wrappers, flesh out AI decision prompts, and add CLI/API.

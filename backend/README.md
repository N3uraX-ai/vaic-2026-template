# VAIC 2026 Backend

## Setup
```bash
conda activate vaic2026
uvicorn main:app --reload --port 8000
```

## API Docs
http://localhost:8000/docs

## Structure
```
backend/
├── main.py          # FastAPI app entry point
├── config.py        # Settings & env vars
├── api/
│   ├── routes/      # Add feature routes here
│   └── deps.py      # Shared dependencies
├── services/
│   ├── ai/          # PyTorch models & AI logic
│   └── db/          # Database operations
└── models/          # PyTorch model files (.pt)
```

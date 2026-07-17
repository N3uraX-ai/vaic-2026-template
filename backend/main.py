"""
VAIC 2026 — FastAPI Backend Boilerplate
Track-agnostic: thêm routes vào sau khi biết đề bài
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.routes.ai import router as ai_router


def get_torch_info() -> dict:
    """Return torch metadata when available; never crash the app if PyTorch is absent."""
    try:
        import torch
        return {
            "version": torch.__version__,
            "cuda": torch.cuda.is_available(),
            "available": True,
        }
    except Exception as exc:  # pragma: no cover - defensive fallback
        return {
            "version": "not-installed",
            "cuda": False,
            "available": False,
            "error": str(exc),
        }


# ─── Startup / Shutdown ───────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load models on startup if available."""
    info = get_torch_info()
    print(f"[STARTUP] PyTorch version: {info['version']}")
    print(f"[STARTUP] CUDA available: {info['cuda']}")
    # TODO: Load your PyTorch model here after choosing track
    # app.state.model = load_model()
    yield
    print("[SHUTDOWN] Cleaning up...")


# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="VAIC 2026 API",
    description="AI-Native backend — VAIC 2026",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS — allow Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/")
async def root():
    info = get_torch_info()
    return {
        "status": "ok",
        "team": "NeuraX.ai",
        "competition": "VAIC 2026",
        "pytorch": info["version"],
        "cuda": info["cuda"],
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

# ─── Feature routers ───────────────────────────────────────────────────────
app.include_router(ai_router, prefix="/api/ai")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

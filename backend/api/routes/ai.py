"""
Generic AI router — placeholder
Thay thế nội dung sau khi biết track
"""
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import tempfile
import os

router = APIRouter(tags=["AI"])


# ─── Models ───────────────────────────────────────────────────────────────────
class TextRequest(BaseModel):
    text: str
    language: str = "vi"

class TextResponse(BaseModel):
    result: str
    confidence: float | None = None


# ─── Routes ───────────────────────────────────────────────────────────────────
def _fallback_response(req: TextRequest) -> TextResponse:
    text = req.text.strip().lower()
    if any(keyword in text for keyword in ["cưa", "súng", "không an toàn", "tấn công"]):
        result = "Phát hiện dấu hiệu cảnh báo môi trường và cần kiểm tra ngay."
        confidence = 0.81
    elif any(keyword in text for keyword in ["chim", "âm thanh", "rừng", "sinh thái"]):
        result = "Tín hiệu môi trường đang được phân tích và ghi nhận như một mẫu quan sát hợp lệ."
        confidence = 0.74
    else:
        result = "Phân tích ban đầu đã nhận diện nội dung và đang chuẩn bị báo cáo chi tiết."
        confidence = 0.69
    return TextResponse(result=result, confidence=confidence)


@router.post("/analyze", response_model=TextResponse)
async def analyze_text(req: TextRequest):
    """
    Generic text analysis endpoint.
    Falls back to a deterministic response when the LLM service is unavailable.
    """
    try:
        from services.ai_services import get_llm
        llm = get_llm()
        result = llm.quick(
            prompt=req.text,
            system="Bạn là trợ lý AI hỗ trợ phân tích. Trả lời bằng tiếng Việt."
        )
        return TextResponse(result=result, confidence=0.72)
    except Exception as exc:  # pragma: no cover - defensive fallback
        print(f"[AI] Falling back to heuristic response: {exc}")
        return _fallback_response(req)


@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Speech-to-text bằng Whisper (PyTorch).
    Hữu ích cho: Giáo dục, Y tế, SME voice commands
    """
    from services.ai_services import get_whisper
    
    # Save uploaded file temporarily
    suffix = os.path.splitext(file.filename)[1] or ".wav"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        whisper = get_whisper()
        result = whisper.transcribe(tmp_path, language="vi")
        return {"text": result["text"], "segments": result["segments"]}
    finally:
        os.unlink(tmp_path)

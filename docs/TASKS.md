# VAIC 2026 — Task Board

**Team NeuraX.ai** | Huỳnh Quốc Việt · Lê Nguyễn Gia Hưng · Hồ Minh Hiếu

> Format: `[ ]` todo · `[/]` in progress · `[x]` done

---

## Phase 0 — Preparation (16/07 tối, trước D-Day)

> Mục tiêu: mọi người ngủ với môi trường đã sẵn sàng, không còn setup khi đến venue.

### Việt (AI Lead)

- [ ] `conda activate vaic2026` — verify không lỗi
- [ ] `python -c "import torch; print(torch.__version__)"` — verify PyTorch OK
- [ ] Đăng ký / login **HuggingFace** → `huggingface-cli login` (tránh rate limit khi download model)
- [ ] Xin **Groq API key**: https://console.groq.com → điền vào `backend/.env`
- [ ] Đọc `CLAUDE.md` section 7 — nắm rõ 3 PyTorch components sẵn có
- [ ] Đọc `CLAUDE.md` section 5 — nắm timeline 48h, milestone của mình

### Hưng (AI All-round)

- [ ] `cd frontend && npm install && npm run dev` — verify localhost:3000 OK
- [ ] Tạo **Google Slides** 10 slide blank, đặt tên sections sẵn:
  - Slide 1: Hook · Slide 2: Problem · Slide 3: Solution · Slide 4: Architecture
  - Slide 5: Demo · Slide 6: Business Case · Slide 7: Metrics · Slide 8: Tech Stack
  - Slide 9: Team · Slide 10: Ask / Next Steps
- [ ] Login **Groq Console** — có API key backup
- [ ] Đọc `CLAUDE.md` section 6 — nắm TypeScript conventions

### Hiếu (SE)

- [ ] `conda activate vaic2026 && uvicorn backend/main:app --reload` — verify localhost:8000 OK
- [ ] Login **Railway**: https://railway.app
- [ ] Login **Vercel**: https://vercel.com → connect GitHub account
- [ ] Install **Railway CLI**: `npm install -g @railway/cli && railway login`
- [ ] Install **Vercel CLI**: `npm install -g vercel && vercel login`
- [ ] Install **ngrok** (emergency backup): https://ngrok.com/download
- [ ] Push repo lên GitHub org (remote URL đã được set chưa?)
- [ ] **[CRITICAL]** Deploy backend lên Railway — lấy live URL
- [ ] **[CRITICAL]** Deploy frontend lên Vercel — verify gọi được backend
- [ ] Update `frontend/vercel.json` với Railway URL thật
- [ ] Đọc `CLAUDE.md` section 8 — nắm bước thêm route mới

### Cả team — Họp nhanh 15 phút trước khi ngủ

- [ ] Xác nhận Railway URL + Vercel URL hoạt động
- [ ] Thống nhất: khi biết track, ai làm gì trong 30 phút đầu
- [ ] Review nhanh bảng PyTorch component → track trong `CLAUDE.md` section 7

---

## Phase 1 — Kickoff (17/07 · 08:00–12:00)

> Mục tiêu: chọn track + phân task xong trước 12:00.

### Cả team

- [ ] 08:00 — Check-in tại FPT Tower (deadline 09:30)
- [ ] 11:00 — Nhận đề bài, đọc **tất cả 8 track descriptions**
- [ ] **Chọn track trong 30 phút** theo framework:
  1. PyTorch có thể là CORE không? (không phải decoration)
  2. Demo được bằng live URL sau 36h không?
  3. Business case pitch được trong 2 câu không?
- [ ] Ghi track đã chọn vào `docs/ai_collab_log.md` + `README.md`
- [ ] Tạo đội trên platform: https://hub.aiforvietnam.org/ (deadline 11:00)
- [ ] Nộp Checkpoint 1 (11:00 ngày 18/07): project name + description — **Việt submit**

### Việt — sau khi chọn track

- [ ] Xác định dataset (HuggingFace hoặc synthetic)
- [ ] Chọn PyTorch component sẽ dùng (Whisper / PhoBERT / EfficientNet)
- [ ] Viết `backend/services/[track]_model.py` — inference function đầu tiên

### Hưng — sau khi chọn track

- [ ] Thiết kế system prompt cho LLM layer (Groq)
- [ ] Xác định input/output flow: user nhập gì → AI trả về gì → UI hiển thị gì
- [ ] Bắt đầu UI layout cho `frontend/src/app/page.tsx`

### Hiếu — sau khi chọn track

- [ ] Tạo `backend/api/routes/[track].py` — skeleton với request/response models
- [ ] Đăng ký route trong `backend/main.py`
- [ ] Verify deploy pipeline vẫn hoạt động sau khi thêm route mới

---

## Phase 2 — Core Build (17/07 12:00 → 18/07 11:00)

> Mục tiêu: có working product, dù chưa đẹp.

### Việt

- [ ] PyTorch model chạy inference được (T+3, ~14:00)
- [ ] Kết nối model vào Hiếu's API endpoint (T+6, ~17:00)
- [ ] Confidence score được trả về đúng format (T+8)
- [ ] Đăng ký **Mentor Room 1** (kiến trúc kỹ thuật) nếu cần — slot 20 phút

### Hưng

- [ ] Groq LLM pipeline trả về response (T+3, ~14:00)
- [ ] UI gọi được API, hiển thị result cơ bản (T+6, ~17:00)
- [ ] Loading state + error handling hoạt động (T+8)
- [ ] Update `docs/ai_collab_log.md` mỗi khi dùng AI tool

### Hiếu

- [ ] `/api/[track]/predict` endpoint nhận request, trả response (T+3)
- [ ] Integration test: frontend → backend → model → response (T+6)
- [ ] **[CRITICAL]** Checkpoint 2 (23:00 ngày 18/07): submit live URL + GitHub link
- [ ] Verify live URL stable, không crash

---

## Phase 3 — Polish (18/07 23:00 → 19/07 07:00)

> Mục tiêu: product đủ tốt để demo trước giám khảo.

### Việt

- [ ] Cải thiện model accuracy / confidence calibration
- [ ] Thêm uncertainty estimation nếu có thể
- [ ] Review toàn bộ PyTorch code — đảm bảo đủ "depth" cho Best PyTorch Award

### Hưng

- [ ] UI/UX polish — không phải đẹp nhất, nhưng demo được mượt
- [ ] Demo flow script: biết chính xác sẽ click gì, nhập gì, show gì
- [ ] Bắt đầu **presentation slides** (fill content vào template đã tạo)
- [ ] Đăng ký **Mentor Room 2** (UX, kinh doanh) nếu cần

### Hiếu

- [ ] Deploy stable, không có cold start lag quá 3 giây
- [ ] Test live URL từ 3 device khác nhau
- [ ] Chuẩn bị backup: `ngrok http 8000` sẵn sàng nếu Railway có vấn đề

---

## Phase 4 — Final (19/07 07:00 → 11:00)

> Mục tiêu: nộp đủ 5 deliverables trước 11:00.

### Hưng

- [ ] Hoàn thiện **presentation slides** (10 slides)
- [ ] Record **demo video ≤ 5 phút** (screen recording + voiceover)
- [ ] Upload video lên YouTube/Drive, lấy link

### Việt

- [ ] Review slides — đảm bảo phần kỹ thuật chính xác
- [ ] Chuẩn bị trả lời câu hỏi kỹ thuật từ giám khảo

### Hiếu

- [ ] Verify **GitHub repo public** (không phải private)
- [ ] Verify **live URL** còn hoạt động
- [ ] Final check `docs/ai_collab_log.md` — đủ entries chưa

### Cả team — Nộp bài (trước 11:00)

- [ ] Presentation slides ← Hưng
- [ ] Demo video ≤ 5 phút ← Hưng
- [ ] GitHub repository (public) ← Hiếu verify
- [ ] Live deployed URL ← Hiếu
- [ ] AI Collaboration Log ← Cả team

---

## Deliverables Status

| # | Item | Status | Link |
|---|------|--------|------|
| 1 | Presentation slides | `[ ]` | - |
| 2 | Demo video ≤ 5 min | `[ ]` | - |
| 3 | GitHub repo (public) | `[ ]` | - |
| 4 | Live deployed URL | `[ ]` | - |
| 5 | AI Collaboration Log | `[ ]` | [docs/ai_collab_log.md](./ai_collab_log.md) |

---

*Update file này liên tục — thay `[ ]` → `[/]` → `[x]` theo progress.*

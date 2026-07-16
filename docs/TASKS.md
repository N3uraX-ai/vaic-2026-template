# VAIC 2026 — Task Board

**Team NeuraX.ai** | Huỳnh Quốc Việt · Lê Nguyễn Gia Hưng · Hồ Minh Hiếu  
**Source:** Lịch trình chính thức từ Hackers Guideline (trang 32–34/35)

> Format: `[ ]` todo · `[/]` in progress · `[x]` done

---

## Phase 0 — Preparation (Tối 16/07 — trước khi đi ngủ)

> Mục tiêu: sáng mai check-in với môi trường đã sẵn sàng.

### ⚠️ Còn hôm nay: Đăng ký Mentor Room 1

> **Mentor Room 1 (kiến trúc kỹ thuật) yêu cầu đăng ký slot 20 phút TRƯỚC NGÀY 16/07** — tức là phải làm NGAY TỐI NAY hoặc đã trễ.

- [ ] **[URGENT - HÔM NAY]** Đăng ký slot Mentor Room 1 trên platform — Việt/Hiếu làm ngay

### Việt (AI Lead)

- [ ] `conda activate vaic2026` → không lỗi
- [ ] `python -c "import torch; print(torch.__version__)"` → verify OK
- [ ] Login HuggingFace → `huggingface-cli login` (tránh rate limit khi download model)
- [ ] Lấy **Groq API key**: https://console.groq.com → điền vào `backend/.env`
- [ ] Đọc `CLAUDE.md` section 7 — nắm 3 PyTorch components + bảng track → component

### Hưng (AI All-round)

- [x] `cd frontend && npm install && npm run dev` → localhost:3000 OK
- [ ] Tạo **Google Slides** 10 slide blank, đặt tên sections sẵn:
  - Slide 1: Hook · Slide 2: Problem · Slide 3: Solution · Slide 4: Architecture
  - Slide 5: Demo · Slide 6: Business Case · Slide 7: Metrics · Slide 8: Tech Stack
  - Slide 9: Team · Slide 10: Ask / Next Steps
- [ ] Login Groq Console — có API key backup

### Hiếu (SE)

- [ ] `conda activate vaic2026 && uvicorn backend/main:app --reload` → localhost:8000 OK
- [ ] Login Railway + Vercel, kết nối GitHub account
- [ ] Install Railway CLI: `npm install -g @railway/cli && railway login`
- [ ] Install ngrok (emergency backup): https://ngrok.com/download
- [ ] **[CRITICAL]** Deploy backend lên Railway — có live URL
- [ ] **[CRITICAL]** Deploy frontend lên Vercel — gọi được backend
- [ ] Update `frontend/vercel.json` với Railway URL thật
- [ ] Push repo lên GitHub org (đặt public)

### Cả team — Họp 15 phút trước khi ngủ

- [ ] Xác nhận Railway URL + Vercel URL hoạt động
- [ ] Thống nhất: khi biết track, ai làm gì trong 30 phút đầu

---

## Phase 1 — Thứ Sáu 17/07 · Đón tiếp & Khai mạc

> Lịch chính thức từ BTC:

| Giờ (chính thức) | Sự kiện |
|---|---|
| **08:00 – 09:30** | Check-in và tham dự sự kiện |
| **09:00 – 10:30** | Lễ khai mạc |
| **11:00** | 🔴 **CÔNG BỐ 08 TRACK** trên màn hình chính |
| **12:00** | Genius Station chính thức mở cửa (15–20 chuyên gia hỗ trợ 24/7) |
| **16:00 – 17:30** | Workshop từ nhà tài trợ: Meta, FPT, SHB, AI Singapore, Điện Máy Xanh (diễn ra song song) |
| **18:00 – 19:30** | Ăn tối |
| **22:00 – 23:00** | Ask-Me-Anything Session 1 |

### Cả team — 11:00 (nhận đề bài)

- [ ] Đọc tất cả 08 track descriptions
- [ ] **Chọn track trong 30 phút** theo 3 câu hỏi:
  1. PyTorch có thể là CORE không? (không phải decoration)
  2. Demo được bằng live URL sau 36h không?
  3. Business case pitch được trong 2 câu không?
- [ ] Ghi track đã chọn vào `docs/ai_collab_log.md` + `README.md`
- [ ] Tạo đội trên hub.aiforvietnam.org (nếu chưa làm) — deadline 11:00

### Việt — 11:30 trở đi

- [ ] Xác định dataset phù hợp (HuggingFace hoặc synthetic bằng LLM)
- [ ] Chọn PyTorch component (Whisper / PhoBERT / EfficientNet)
- [ ] Viết inference function đầu tiên trong `backend/services/[track]_model.py`
- [ ] **Target 17:00:** model chạy được, trả về output (dù accuracy chưa tốt)

### Hưng — 11:30 trở đi

- [ ] Thiết kế system prompt cho LLM layer (Groq)
- [ ] Xác định user flow: input → AI processing → output
- [ ] Bắt đầu UI layout cho `frontend/src/app/page.tsx`
- [ ] **Target 17:00:** UI có form input + gọi được API

### Hiếu — 11:30 trở đi

- [ ] Tạo `backend/api/routes/[track].py` với request/response models
- [ ] Đăng ký route trong `backend/main.py`
- [ ] **Target 17:00:** `/api/[track]/predict` endpoint hoạt động (mock data OK)

### 16:00 – 17:30 (tùy chọn)

- [ ] Ai đang bí kỹ thuật → tham dự workshop Meta/FPT
- [ ] Ai đang code tốt → tiếp tục build, bỏ qua workshop

### 22:00 – 23:00

- [ ] Tham dự AMA Session 1 nếu có câu hỏi về kiến trúc hoặc strategy
- [ ] Không có câu hỏi → tiếp tục code

---

## Phase 2 — Thứ Bảy 18/07 · Hackathon chính

> Lịch chính thức từ BTC:

| Giờ (chính thức) | Sự kiện |
|---|---|
| **07:00 – 09:00** | Ăn sáng linh hoạt |
| **09:00 – 16:00** | Mentor Room 1: kiến trúc kỹ thuật (slot 20 phút, đã đăng ký từ trước) |
| **09:00 – 16:00** | Mentor Room 2: UX, thiết kế và kinh doanh |
| **11:00** | 🔴 **CHECKPOINT 1** — Nộp: project name, track, mô tả giải pháp |
| **18:00 – 19:30** | Ăn tối |
| **23:00** | 🔴 **CHECKPOINT 2** — Nộp: live deployed URL + GitHub repository public |
| **23:00 – 24:00** | Ask-Me-Anything Session 2 |

### 11:00 — CHECKPOINT 1 (Việt submit)

- [ ] Nộp trên platform: project name + track đã chọn + mô tả giải pháp + hướng tiếp cận ban đầu

### Mentor Rooms (09:00 – 16:00)

- [ ] **Mentor Room 1** — Việt tham dự (kiến trúc PyTorch, AI architecture) — slot đã đăng ký từ 16/07
- [ ] **Mentor Room 2** — Hưng tham dự (UX, business model, pitch) — đăng ký tại venue

### Việt — Cả ngày

- [ ] Cải thiện accuracy / fine-tune nhẹ nếu có data
- [ ] Thêm confidence score vào mọi response
- [ ] Review: PyTorch có thực sự là CORE không? (để đủ điều kiện Best PyTorch Award)
- [ ] **Target 21:00:** model ổn định, inference < 3 giây

### Hưng — Cả ngày

- [ ] UI/UX hoàn chỉnh — loading state, error handling
- [ ] Demo flow script: biết chính xác click gì, nhập gì, show gì
- [ ] Bắt đầu fill content vào Google Slides

### Hiếu — Cả ngày

- [ ] Integration test: frontend → backend → model → response
- [ ] Deploy stable, test từ 3 device khác nhau
- [ ] **Target 22:00:** live URL stable, không crash

### 23:00 — CHECKPOINT 2 (Hiếu submit)

- [ ] Nộp trên platform: **live deployed URL** + **GitHub repository link** (public)
- [ ] Verify GitHub repo public trước khi submit

---

## Phase 3 — Đêm 18/07 → Sáng 19/07 · Polish

> Không có lịch chính thức từ BTC cho giai đoạn này.

### ~01:00 – 07:00

- [ ] **Ngủ theo ca** — không cần cả team thức cùng lúc
- [ ] Người nào cần fix gấp thì thức, còn lại ngủ 4-5 tiếng

### 07:00 – 11:00 (ngày 19/07)

- [ ] Việt: final review PyTorch code, chuẩn bị trả lời câu hỏi kỹ thuật
- [ ] Hưng: hoàn thiện slides (10 slides) + record demo video ≤ 5 phút
- [ ] Hiếu: verify live URL còn chạy, GitHub repo public, chuẩn bị nộp bài

---

## Phase 4 — Chủ Nhật 19/07 · Nộp bài & Demo Day

> Lịch ngày 19/07 chưa được BTC công bố chi tiết trong guideline.  
> Dựa trên cấu trúc event: Final submission → Presentation vòng → Trao giải.

### 11:00 — DEADLINE NỘP BÀI (cả team)

- [ ] **1.** Presentation slides ← Hưng upload
- [ ] **2.** Demo video ≤ 5 phút ← Hưng upload link
- [ ] **3.** GitHub repository (public) ← Hiếu verify public
- [ ] **4.** Live deployed URL ← Hiếu verify còn chạy
- [ ] **5.** AI Collaboration Log ← verify `docs/ai_collab_log.md` đầy đủ entries

### Demo Day (giờ cụ thể theo BTC thông báo tại venue)

- [ ] Demo live URL trước giám khảo (không dùng video)
- [ ] Việt: trả lời câu hỏi kỹ thuật về PyTorch
- [ ] Hưng: dẫn dắt pitch, business case
- [ ] Hiếu: backup technical questions về deploy/architecture

---

## Deliverables Status

| # | Item | Owner | Status | Link |
|---|------|-------|--------|------|
| 1 | Presentation slides | Hưng | `[ ]` | - |
| 2 | Demo video ≤ 5 min | Hưng | `[ ]` | - |
| 3 | GitHub repo (public) | Hiếu | `[ ]` | - |
| 4 | Live deployed URL | Hiếu | `[ ]` | - |
| 5 | AI Collaboration Log | Cả team | `[ ]` | [docs/ai_collab_log.md](./ai_collab_log.md) |

---

*Update liên tục — thay `[ ]` → `[/]` → `[x]` theo progress.*  
*Source lịch trình: Hackers Guideline trang 32–34/35*

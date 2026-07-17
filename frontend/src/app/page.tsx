"use client";

import { useState } from "react";
import api from "@/lib/api";

export default function Home() {
  const [input, setInput] = useState("Tôi ghi nhận tiếng cưa gỗ trong khu rừng");
  const [loading, setLoading] = useState(false);
  const [health, setHealth] = useState("Checking backend...");
  const [result, setResult] = useState<{ result: string; confidence?: number } | null>(null);
  const [error, setError] = useState("");

  const runCheck = async () => {
    setLoading(true);
    setError("");
    try {
      const healthData = await api.health();
      setHealth(healthData.status);
      const analysis = await api.analyzeText(input);
      setResult(analysis);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unable to reach the backend");
      setHealth("offline");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-zinc-50 px-6 py-16 text-zinc-900 dark:bg-black dark:text-zinc-50">
      <div className="mx-auto flex max-w-3xl flex-col gap-6 rounded-2xl border border-zinc-200 bg-white p-8 shadow-sm dark:border-zinc-800 dark:bg-zinc-950">
        <div className="space-y-2">
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-emerald-600">BioListen VN</p>
          <h1 className="text-3xl font-semibold">Cảnh báo sinh thái thời gian thực</h1>
          <p className="text-sm text-zinc-600 dark:text-zinc-400">
            Mẫu UI demo cho việc kết nối frontend với FastAPI backend khi deploy lên Vercel + Railway.
          </p>
        </div>

        <div className="rounded-xl bg-zinc-100 p-4 dark:bg-zinc-900">
          <p className="text-sm text-zinc-500">Backend status</p>
          <p className="text-lg font-medium">{health}</p>
        </div>

        <textarea
          value={input}
          onChange={(event) => setInput(event.target.value)}
          className="min-h-24 rounded-xl border border-zinc-300 bg-white px-4 py-3 text-sm outline-none ring-0 dark:border-zinc-700 dark:bg-zinc-950"
          placeholder="Nhập tín hiệu giám sát..."
        />

        <button
          onClick={runCheck}
          disabled={loading}
          className="rounded-full bg-emerald-600 px-5 py-3 text-sm font-semibold text-white transition hover:bg-emerald-500 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? "Đang kiểm tra..." : "Gửi phân tích"}
        </button>

        {error ? <p className="text-sm text-red-500">{error}</p> : null}

        {result ? (
          <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-4 dark:border-emerald-900 dark:bg-emerald-950/30">
            <p className="text-sm font-semibold text-emerald-700 dark:text-emerald-300">Kết quả</p>
            <p className="mt-2 text-base">{result.result}</p>
            {result.confidence ? (
              <p className="mt-2 text-sm text-zinc-600 dark:text-zinc-400">
                Confidence: {(result.confidence * 100).toFixed(0)}%
              </p>
            ) : null}
          </div>
        ) : null}
      </div>
    </main>
  );
}

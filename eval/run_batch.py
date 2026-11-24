import argparse
import csv
import json
import time
from pathlib import Path
import requests

WEBHOOK_URL = "http://localhost:5678/webhook/ask"


def main():
    parser = argparse.ArgumentParser(description="Run batch evaluation against FlowPulse webhook")
    parser.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    parser.add_argument("--input", default="eval/questions.csv")
    parser.add_argument("--output", default=None)
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests to respect Gemini rate limits")
    args = parser.parse_args()

    out_path = Path(args.output or f"eval/results_{args.split}.jsonl")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(args.input, mode="r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    if args.split != "all":
        rows = [r for r in rows if r.get("split", "").strip().lower() == args.split]

    print(f"Running {len(rows)} questions for split='{args.split}' -> {out_path}")

    with open(out_path, mode="w", encoding="utf-8") as out_f:
        for idx, row in enumerate(rows, start=1):
            qid = row.get("id", f"q_{idx}")
            session_id = row.get("session_id") or f"eval_{args.split}_{qid}"
            question = row["question"]

            payload = {
                "session_id": session_id,
                "message": question,
                "test_mode": True,
            }

            t0 = time.time()
            try:
                resp = requests.post(WEBHOOK_URL, json=payload, timeout=60)
                resp.raise_for_status()
                data = resp.json()
            except Exception as exc:
                data = {
                    "session_id": session_id,
                    "route": "http_error",
                    "reason": str(exc),
                    "reply": "",
                    "sources": [],
                    "top_score": None,
                    "latency_ms": int((time.time() - t0) * 1000),
                }

            record = {
                **row,
                "predicted_route": data.get("route"),
                "predicted_reason": data.get("reason"),
                "reply": data.get("reply", ""),
                "sources": data.get("sources", []),
                "top_score": data.get("top_score"),
                "latency_ms": data.get("latency_ms"),
            }
            out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
            out_f.flush()

            print(
                f"[{idx}/{len(rows)}] {qid} | expected={row.get('expected_route')} "
                f"got={record['predicted_route']} | score={record['top_score']} | {record['latency_ms']}ms"
            )

            if idx < len(rows) and args.delay > 0:
                time.sleep(args.delay)

    print(f"\nSaved {len(rows)} results to {out_path}")


if __name__ == "__main__":
    main()
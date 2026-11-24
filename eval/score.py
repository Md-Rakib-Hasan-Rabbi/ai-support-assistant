import argparse
import json
from collections import Counter


def percentile(values, pct):
    if not values:
        return 0
    s = sorted(values)
    k = int(round((pct / 100.0) * (len(s) - 1)))
    return s[k]


def main():
    parser = argparse.ArgumentParser(description="Score FlowPulse evaluation results")
    parser.add_argument("--results", default="eval/results_dev.jsonl")
    args = parser.parse_args()

    with open(args.results, mode="r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    total = len(records)
    if total == 0:
        print("No records found.")
        return

    route_correct = 0
    confusion = Counter()
    answerable_total = 0
    answerable_answered = 0
    citation_hits = 0

    trap_total = 0
    trap_defended = 0  # non-answerable properly refused or escalated (not answered)

    answered_scores = []
    non_answerable_scores = []
    latencies = []

    for r in records:
        exp_route = (r.get("expected_route") or "").strip().lower()
        pred_route = (r.get("predicted_route") or "").strip().lower()
        exp_source = (r.get("expected_source") or "").strip().lower()
        category = (r.get("category") or "").strip().lower()

        if r.get("latency_ms") is not None:
            latencies.append(float(r["latency_ms"]))

        confusion[(exp_route, pred_route)] += 1
        if exp_route == pred_route:
            route_correct += 1

        score = r.get("top_score")

        if exp_route == "answered":
            answerable_total += 1
            if score is not None:
                answered_scores.append(float(score))
            if pred_route == "answered":
                answerable_answered += 1
                urls = [
                    (s.get("url") or s.get("title") or "").lower()
                    for s in (r.get("sources") or [])
                ]
                if not exp_source or any(exp_source in u for u in urls):
                    citation_hits += 1
        else:
            trap_total += 1
            if score is not None:
                non_answerable_scores.append(float(score))
            if pred_route != "answered":
                trap_defended += 1

    print("=" * 55)
    print(f"EVALUATION REPORT: {args.results} (N={total})")
    print("=" * 55)
    print(f"Overall Route Accuracy : {route_correct}/{total} ({route_correct / total:.1%})")
    if answerable_total:
        print(f"Answerable Recall      : {answerable_answered}/{answerable_total} ({answerable_answered / answerable_total:.1%})")
        print(f"Citation Match Rate    : {citation_hits}/{answerable_total} ({citation_hits / answerable_total:.1%})")
    if trap_total:
        print(f"Trap Defense Rate      : {trap_defended}/{trap_total} ({trap_defended / trap_total:.1%})")

    if answered_scores:
        print(f"Avg Top Score (Ans)    : {sum(answered_scores)/len(answered_scores):.3f} (min={min(answered_scores):.3f})")
    if non_answerable_scores:
        print(f"Avg Top Score (Trap)   : {sum(non_answerable_scores)/len(non_answerable_scores):.3f} (max={max(non_answerable_scores):.3f})")

    if latencies:
        print(f"Latency p50 / p95      : {percentile(latencies, 50):.0f} ms / {percentile(latencies, 95):.0f} ms")

    print("\nConfusion Matrix (Expected -> Predicted):")
    for (exp, pred), count in sorted(confusion.items()):
        marker = "OK" if exp == pred else "MISS"
        print(f"  {exp:12s} -> {pred:12s} : {count:3d}  [{marker}]")

    print("\nMismatches:")
    for r in records:
        exp = (r.get("expected_route") or "").strip().lower()
        pred = (r.get("predicted_route") or "").strip().lower()
        if exp != pred:
            print(
                f"  - [{r.get('id')}] ({r.get('category')}) exp={exp} got={pred} "
                f"score={r.get('top_score')} reason={r.get('predicted_reason')} | Q: {r.get('question')[:75]}"
            )


if __name__ == "__main__":
    main()
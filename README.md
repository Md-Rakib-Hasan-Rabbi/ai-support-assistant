# FlowPulse AI Support Assistant (RAG + Agentic Triage Pipeline)

An end-to-end, production-style customer support automation system built with **n8n**, **PostgreSQL (`pgvector`)**, **Ollama (`nomic-embed-text`)**, and **Google Gemini 2.5 Flash**, complete with deterministic rule guards, citation verification, automated ticket escalation, and a quantitative evaluation harness.

## Architecture Overview
1. **Input Validation & Session Memory:** Validates incoming webhook payloads and loads/persists rolling 6-turn conversation history in PostgreSQL.
2. **Deterministic Rule Triage & LLM Query Rewriting:** Screens prompt injections and explicit account/billing triggers via regex rules before classifying intent (`answerable`, `account_action`, `billing_dispute`, `bug_report`, `out_of_scope`, `injection`) and rewriting context-dependent queries using Gemini 2.5 Flash.
3. **Hybrid Retrieval Gate (`pgvector` + Ollama):** Generates query embeddings locally via `nomic-embed-text`, queries top-k knowledge base chunks in PostgreSQL using cosine similarity, and enforces a similarity threshold gate before generation.
4. **Grounded Generation & Citation Auditing:** Prompts Gemini to answer strictly from retrieved context passages and validates that every cited `used_sources` ID matches a retrieved chunk ID.
5. **Routing, Escalation & Observability:**
   - `answered`: Returns grounded response with source URLs.
   - `refused`: Blocks out-of-scope or prompt-injection attempts.
   - `escalated` / `system_error`: Creates a support ticket in PostgreSQL, triggers a Gmail alert (suppressed when `test_mode: true`), and logs token usage, latency, and routing decisions to `execution_log` and `error_log`.

## Project Structure
- `workflows/` — Exported n8n workflow definitions (`support_assistant.json`, `error_handler.json`)
- `db/` — PostgreSQL schema (`pgvector` tables for KB chunks, sessions, tickets, and logs) and KB ingestion scripts
- `eval/` — Batch evaluation runner (`run_batch.py`), scoring suite (`score.py`), and labeled dataset (`questions.csv`)
- `docker-compose.yml` — Multi-container setup for n8n and PostgreSQL with `pgvector`

## Quick Start
1. Copy `.env.example` to `.env` and fill in your credentials.
2. Start services: `docker compose up -d`
3. Ensure Ollama is running (`OLLAMA_HOST=0.0.0.0:11434`) with `nomic-embed-text` pulled.
4. Import `workflows/support_assistant.json` and `workflows/error_handler.json` into n8n, attach credentials, and activate.
5. Run evaluation:
   ```bash
   python eval/run_batch.py --split dev --delay 5
   python eval/score.py --results eval/results_dev.jsonl


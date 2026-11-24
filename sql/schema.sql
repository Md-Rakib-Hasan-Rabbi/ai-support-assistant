CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE kb_chunks (
  id SERIAL PRIMARY KEY,
  doc_id TEXT,
  title TEXT,
  section TEXT,
  source_url TEXT,
  chunk_index INT,
  content TEXT,
  content_hash TEXT UNIQUE,
  embedding vector(768),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  session_id TEXT,
  role TEXT,
  content TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE tickets (
  ticket_id SERIAL PRIMARY KEY,
  session_id TEXT,
  question TEXT,
  conversation JSONB,
  reason TEXT,
  retrieved_sources JSONB,
  draft_answer TEXT,
  status TEXT DEFAULT 'open',
  created_at TIMESTAMPTZ DEFAULT now(),
  resolved_at TIMESTAMPTZ,
  resolution TEXT
);

CREATE TABLE retrieval_log (
  id SERIAL PRIMARY KEY,
  execution_id TEXT,
  query TEXT,
  chunk_ids JSONB,
  scores JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE execution_log (
  execution_id TEXT,
  session_id TEXT,
  timestamp TIMESTAMPTZ DEFAULT now(),
  route TEXT,
  reason TEXT,
  top_score FLOAT,
  tokens_in INT,
  tokens_out INT,
  cost_usd FLOAT,
  latency_ms INT,
  feedback TEXT
);

CREATE TABLE error_log (
  timestamp TIMESTAMPTZ DEFAULT now(),
  workflow TEXT,
  failed_node TEXT,
  error_message TEXT,
  payload JSONB
);
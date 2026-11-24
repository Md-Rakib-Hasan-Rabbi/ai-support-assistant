import hashlib
import os
import re
import sys
from pathlib import Path

import psycopg2
import requests
import yaml

# --- Configuration ---
KB_DIR = Path("kb")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/embed")
EMBED_MODEL = "nomic-embed-text"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "support",
    "user": "support",
    "password": "support",
}


def parse_markdown_file(filepath: Path):
    """Extract YAML front matter and body from a Markdown file."""
    raw = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.DOTALL)
    if not match:
        raise ValueError(f"Missing or invalid YAML front matter in {filepath.name}")
    meta = yaml.safe_load(match.group(1))
    body = match.group(2).strip()
    return meta, body


def chunks_from_markdown(md_body: str, max_chars: int = 1000, overlap: int = 120):
    """Split Markdown by headings, then slice oversized sections with overlap."""
    sections = re.split(r"\n(?=#{1,3} )", md_body)
    out = []
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        lines = sec.split("\n", 1)
        heading = lines[0].lstrip("# ").strip()
        start = 0
        while start < len(sec):
            chunk_text = sec[start : start + max_chars].strip()
            if chunk_text:
                out.append((heading, chunk_text))
            if start + max_chars >= len(sec):
                break
            start += max_chars - overlap
    return out


def embed_text(text: str, prefix: str = "search_document: ") -> list[float]:
    """Call local Ollama /api/embed endpoint and return a 768-dim vector."""
    resp = requests.post(
        OLLAMA_URL,
        json={"model": EMBED_MODEL, "input": f"{prefix}{text}"},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["embeddings"][0]


def to_vector_literal(vec: list[float]) -> str:
    return "[" + ",".join(str(x) for x in vec) + "]"


def ingest_all():
    md_files = sorted(KB_DIR.glob("*.md"))
    if not md_files:
        print("No .md files found in kb/. Run generate_kb.py first.")
        return

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    inserted = 0
    skipped = 0

    try:
        for filepath in md_files:
            meta, body = parse_markdown_file(filepath)
            doc_id = meta["doc_id"]
            title = meta["title"]
            source_url = meta["source_url"]

            chunks = chunks_from_markdown(body)
            for idx, (section_heading, chunk_text) in enumerate(chunks):
                # Include title & section context in embedded text for stronger retrieval
                contextualized = f"{title} — {section_heading}\n{chunk_text}"
                content_hash = hashlib.sha256(contextualized.encode("utf-8")).hexdigest()

                cur.execute(
                    "SELECT 1 FROM kb_chunks WHERE content_hash = %s;",
                    (content_hash,),
                )
                if cur.fetchone():
                    skipped += 1
                    continue

                vec = embed_text(contextualized, prefix="search_document: ")
                vec_str = to_vector_literal(vec)

                cur.execute(
                    """
                    INSERT INTO kb_chunks
                        (doc_id, title, section, source_url, chunk_index, content, content_hash, embedding)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s::vector);
                    """,
                    (
                        doc_id,
                        title,
                        section_heading,
                        source_url,
                        idx,
                        chunk_text,
                        content_hash,
                        vec_str,
                    ),
                )
                inserted += 1

        conn.commit()
        print(f"Ingestion complete: {inserted} new chunks inserted, {skipped} unchanged chunks skipped.")
    except Exception as e:
        conn.rollback()
        print(f"Error during ingestion: {e}")
        raise
    finally:
        cur.close()
        conn.close()


def test_retrieval(query: str, top_k: int = 5):
    """Run a sanity-check cosine similarity query against Postgres."""
    print(f"\n--- Testing Query: '{query}' ---")
    q_vec = embed_text(query, prefix="search_query: ")
    q_str = to_vector_literal(q_vec)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id, doc_id, title, section,
               ROUND((1 - (embedding <=> %s::vector))::numeric, 4) AS similarity
        FROM kb_chunks
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
        """,
        (q_str, q_str, top_k),
    )
    rows = cur.fetchall()
    for rank, (cid, doc_id, title, section, sim) in enumerate(rows, start=1):
        print(f"{rank}. [score={sim}] {doc_id} | {title} > {section} (chunk_id={cid})")
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--query":
        q = " ".join(sys.argv[2:]) or "How many days do I have to get a refund on an annual plan?"
        test_retrieval(q)
    else:
        ingest_all()
        test_retrieval("How many days do I have to get a refund on an annual plan?")
        test_retrieval("What happens if I exceed my Pro plan monthly task runs?")
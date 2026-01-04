from rapidfuzz import fuzz
from .loader import load_documents
from .chunking import chunk_text

def retrieve(query: str, top_k: int = 3):
    documents = load_documents()
    candidates = []
    q = query.lower()

    for doc in documents:
        chunks = chunk_text(doc["text"])
        for idx, chunk in enumerate(chunks):
            score = fuzz.partial_ratio(q, chunk.lower())
            candidates.append({
                "score": score,
                "path": doc["path"],
                "chunk_id": idx,
                "chunk": chunk.strip()
            })

    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[:top_k]

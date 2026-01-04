def chunk_text(text: str, chunk_size: int = 600, overlap: int = 120):
    chunks = []
    i = 0
    while i < len(text):
        chunk = text[i : i + chunk_size]
        chunks.append(chunk)
        i += max(1, chunk_size - overlap)
    return chunks

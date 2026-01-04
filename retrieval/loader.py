from pathlib import Path

DOCS_DIR = Path("docs")
ALLOWED_SUFFIXES = {".md", ".txt"}

def load_documents():
    docs = []
    for path in DOCS_DIR.rglob("*"):
        if path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            docs.append({"path": str(path), "text": text})
    return docs

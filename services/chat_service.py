from retrieval.fuzzy import retrieve

def build_reply(query: str):
    hits = retrieve(query)

    if not hits or hits[0]["score"] < 35:
        return {
            "reply": "No relevant content found in the docs folder.",
            "sources": []
        }

    reply_lines = ["Here are the most relevant excerpts I found:\n"]
    sources = []

    for h in hits:
        citation = f"{h['path']}#chunk{h['chunk_id']}"
        reply_lines.append(
            f"— ({citation}, score {h['score']})\n{h['chunk']}\n"
        )
        sources.append({"citation": citation, "score": h["score"]})

    return {
        "reply": "\n".join(reply_lines).strip(),
        "sources": sources
    }

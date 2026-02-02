from sentence_transformers import SentenceTransformer
from endee import Endee

model = SentenceTransformer("all-MiniLM-L6-v2")

client = Endee()
index = client.get_index("rag_index")

with open("data/documents/sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = [c.strip() for c in text.split(".") if c.strip()]

for i, chunk in enumerate(chunks):
    emb = model.encode(chunk).tolist()

    index.upsert([
        {
            "id": f"doc_{i}",
            "vector": emb,
            "meta": {"text": chunk}
        }
    ])

print("✅ Data ingested using LOCAL embeddings")

from sentence_transformers import SentenceTransformer
from endee import Endee

model = SentenceTransformer("all-MiniLM-L6-v2")

client = Endee()
index = client.get_index("rag_index")

def semantic_search(query, top_k=3):
    query_embedding = model.encode(query).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=top_k
    )

    return [r["meta"]["text"] for r in results]

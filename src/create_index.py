from endee import Endee, Precision

client = Endee()

client.create_index(
    name="rag_index",
    dimension=384,          # 🔥 MATCH MiniLM
    space_type="cosine",
    precision=Precision.INT8D
)

print("✅ Index created with dimension 384")

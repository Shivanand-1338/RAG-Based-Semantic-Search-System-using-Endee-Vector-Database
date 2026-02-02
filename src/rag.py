from src.search import semantic_search

def generate_answer(query):
    context_chunks = semantic_search(query)

    if not context_chunks:
        return "No relevant information found."

    answer = "Based on the documents, here is the answer:\n\n"
    answer += " ".join(context_chunks)

    return answer

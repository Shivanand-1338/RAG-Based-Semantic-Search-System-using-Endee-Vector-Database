from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

res = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Say hello in one sentence"
)

print(res.text)
# from google import genai

# client = genai.Client(api_key="AIzaSyAtpEj0mn0UhgG7Jh_TEVnINjnz2EpJzAk")

# models = client.models.list()

# for model in models:
#     print(model.name, "-> supports generateContent:", "generateContent" in model.supported_actions)


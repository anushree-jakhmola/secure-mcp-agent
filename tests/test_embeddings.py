from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Model loaded successfully.")

embedding = model.encode(
    "Prompt injection is a security threat."
)

print("Embedding dimension:", len(embedding))
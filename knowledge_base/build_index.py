from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


DOCS_DIR = Path("knowledge_base/docs")
INDEX_DIR = Path("knowledge_base/vectorstore")

INDEX_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []
filenames = []

for file_path in DOCS_DIR.glob("*.txt"):

    text = file_path.read_text(
        encoding="utf-8"
    )

    documents.append(text)

    filenames.append(
        file_path.name
    )

print(
    f"Loaded {len(documents)} documents."
)

embeddings = model.encode(
    documents
)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    str(
        INDEX_DIR / "security_index.faiss"
    )
)

with open(
    INDEX_DIR / "documents.txt",
    "w",
    encoding="utf-8"
) as file:

    for name in filenames:
        file.write(name + "\n")

print(
    "FAISS index created successfully."
)
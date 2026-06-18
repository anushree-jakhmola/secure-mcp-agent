from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


INDEX_DIR = Path(
    "knowledge_base/vectorstore"
)

DOCS_DIR = Path(
    "knowledge_base/docs"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    str(
        INDEX_DIR / "security_index.faiss"
    )
)

with open(
    INDEX_DIR / "documents.txt",
    "r",
    encoding="utf-8"
) as file:

    document_names = [
        line.strip()
        for line in file
    ]


def search_knowledge_base(
    query: str,
    top_k: int = 1,
):
    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        filename = document_names[idx]

        text = (
            DOCS_DIR / filename
        ).read_text(
            encoding="utf-8"
        )

        results.append(
            {
                "document": filename,
                "content": text,
            }
        )

    return results
import faiss
import pickle
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent
VECTORSTORE_DIR = BASE_DIR / "data" / "vectorstore"

INDEX_PATH = VECTORSTORE_DIR / "faiss_index.bin"
META_PATH = VECTORSTORE_DIR / "metadata.pkl"

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(str(INDEX_PATH))

# Load metadata
with open(META_PATH, "rb") as f:
    metadata = pickle.load(f)


def semantic_search(query: str, k: int = 5):
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, k)

    results = []
    for i, idx in enumerate(indices[0]):
        row = metadata[idx]
        results.append({
            "rank": i + 1,
            "distance": float(distances[0][i]),
            "nco_2015_code": row["nco_2015_code"],
            "title": row["title"],
            "nco_2004_code": row["nco_2004_code"]
        })

    return results


def exact_search(query: str):
    query = query.lower().strip()
    results = []

    for row in metadata:
        if query in row["title"].lower():
            results.append(row)

    return results[:20]

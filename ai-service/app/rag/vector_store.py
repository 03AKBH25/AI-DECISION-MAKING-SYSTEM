from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge base
with open("app/rag/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

# Prepare data
texts = [item["rule"] for item in knowledge_base]

# Convert to embeddings
embeddings = model.encode(texts)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search(query, top_k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for i in indices[0]:
        results.append(knowledge_base[i])

    return results
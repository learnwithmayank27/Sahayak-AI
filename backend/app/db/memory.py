import uuid
from app.db.redis_client import redis_client
from app.db.qdrant_client import qdrant, COLLECTION_NAME
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------- SHORT TERM (REDIS) ----------

def save_chat(session_id: str, message: str):
    redis_client.rpush(session_id, message)

def get_chat_history(session_id: str):
    return redis_client.lrange(session_id, 0, -1)

# ---------- LONG TERM (QDRANT) ----------

def store_memory(text: str):
    vector = model.encode(text).tolist()
    
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            {
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": {"text": text},
            }
        ],
    )

def search_memory(query: str):
    vector = model.encode(query).tolist()

    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=3
    )

    return [point.payload["text"] for point in results.points]    
    return [r.payload["text"] for r in results]

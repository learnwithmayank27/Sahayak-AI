from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import time


# ✅ CREATE CLIENT (THIS WAS MISSING)
qdrant = QdrantClient(host="qdrant", port=6333)

COLLECTION_NAME = "shayak_memory"

def init_collection():
    for _ in range(5):
        try:
            collections = qdrant.get_collections().collections
            names = [c.name for c in collections]

            if COLLECTION_NAME not in names:
                qdrant.create_collection(
                    collection_name=COLLECTION_NAME,
                    vectors_config=VectorParams(
                        size=384,
                        distance=Distance.COSINE
                    ),
                )
            return
        except Exception as e:
            print("Retrying Qdrant...", e)
            time.sleep(2)

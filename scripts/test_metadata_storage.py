# scripts/test_metadata_storage.py

from backend.app.services.vector_store import collection

results = collection.get()

print(results["metadatas"][0])
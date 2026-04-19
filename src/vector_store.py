from typing import List, Dict
import chromadb

from src.config import CHROMA_PERSIST_DIR, COLLECTION_NAME


def get_chroma_client():
    return chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)


def get_or_create_collection():
    client = get_chroma_client()
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return collection


def reset_collection():
    client = get_chroma_client()
    try:
        client.delete_collection(name=COLLECTION_NAME)
    except Exception:
        pass
    return client.get_or_create_collection(name=COLLECTION_NAME)


def index_documents(documents: List[Dict], embeddings: List[List[float]]) -> None:
    collection = get_or_create_collection()

    ids = [doc["chunk_id"] for doc in documents]
    texts = [doc["text"] for doc in documents]
    metadatas = [
        {
            "source": doc["source"],
            "page": doc["page"],
        }
        for doc in documents
    ]

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )


def query_collection(query_embedding: List[float], n_results: int = 5) -> Dict:
    collection = get_or_create_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )
    return results
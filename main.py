from src.ingestion import load_all_pdfs, save_documents_to_json
from src.chunking import chunk_documents
from src.embeddings import EmbeddingModel
from src.vector_store import reset_collection, index_documents, query_collection
from src.retrieval import format_retrieval_results


def main():
    docs = load_all_pdfs("data/raw")
    print(f"\nTotal pages: {len(docs)}")

    chunked_docs = chunk_documents(docs)
    print(f"Total chunks: {len(chunked_docs)}")

    save_documents_to_json(chunked_docs, "data/processed/chunked_documents.json")

    embedding_model = EmbeddingModel()
    chunk_texts = [doc["text"] for doc in chunked_docs]
    embeddings = embedding_model.embed_texts(chunk_texts)

    print(f"Generated embeddings for {len(embeddings)} chunks.")

    reset_collection()
    index_documents(chunked_docs, embeddings)
    print("Chunks indexed in Chroma.")

    query = "Quelles sont les caractéristiques d'une intelligence artificielle digne de confiance ?"
    query_embedding = embedding_model.embed_query(query)

    results = query_collection(query_embedding, n_results=5)
    formatted_results = format_retrieval_results(results)

    print("\n--- QUERY ---")
    print(query)

    print("\n--- TOP RESULTS ---")
    for i, result in enumerate(formatted_results, start=1):
        print(f"\nResult {i}")
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Source: {result['source']}")
        print(f"Page: {result['page']}")
        print(f"Distance: {result['distance']}")
        print(f"Text preview: {result['text'][:300]}")


if __name__ == "__main__":
    main()
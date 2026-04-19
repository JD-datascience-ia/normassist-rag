from src.ingestion import load_all_pdfs, save_documents_to_json
from src.chunking import chunk_documents


def main():
    docs = load_all_pdfs("data/raw")

    print(f"\nTotal pages: {len(docs)}")

    chunked_docs = chunk_documents(docs)

    print(f"Total chunks: {len(chunked_docs)}")

    if chunked_docs:
        sample = chunked_docs[0]
        print("\n--- SAMPLE CHUNK ---")
        print(sample["chunk_id"])
        print(sample["text"][:300])

    save_documents_to_json(chunked_docs, "data/processed/chunked_documents.json")


if __name__ == "__main__":
    main()
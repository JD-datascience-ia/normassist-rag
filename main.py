from src.ingestion import load_all_pdfs, save_documents_to_json


def main():
    docs = load_all_pdfs("data/raw")

    print(f"\nTotal extracted pages: {len(docs)}")

    if docs:
        sample = docs[0]
        print("\n--- SAMPLE DOCUMENT ---")
        print(f"Source: {sample['source']}")
        print(f"Page: {sample['page']}")
        print(f"Text preview:\n{sample['text'][:500]}")

        text_lengths = [len(doc["text"]) for doc in docs]
        avg_length = sum(text_lengths) / len(text_lengths)

        print("\n--- EXTRACTION STATS ---")
        print(f"Average characters per page: {avg_length:.2f}")
        print(f"Shortest page length: {min(text_lengths)}")
        print(f"Longest page length: {max(text_lengths)}")

    save_documents_to_json(docs, "data/processed/extracted_documents.json")


if __name__ == "__main__":
    main()
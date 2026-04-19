from typing import List, Dict


def format_retrieval_results(results: Dict) -> List[Dict]:
    formatted_results = []

    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for chunk_id, text, metadata, distance in zip(ids, documents, metadatas, distances):
        formatted_results.append(
            {
                "chunk_id": chunk_id,
                "text": text,
                "source": metadata.get("source"),
                "page": metadata.get("page"),
                "distance": distance,
            }
        )

    return formatted_results
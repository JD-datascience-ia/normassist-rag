from typing import List, Dict


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """
    Split le texte en chuncks avec retour en arrière de 100 caractères.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks



def chunk_documents(documents: List[Dict], chunk_size: int = 500, overlap: int = 100) -> List[Dict]:
    """
    Convertit les pages des documents en chunks.
    """
    chunked_docs = []

    for doc in documents:
        chunks = chunk_text(doc["text"], chunk_size, overlap)

        for i, chunk in enumerate(chunks):
            chunked_docs.append({
                "chunk_id": f"{doc['source']}_p{doc['page']}_c{i}",
                "source": doc["source"],
                "page": doc["page"],
                "text": chunk,
            })

    return chunked_docs


from src.ingestion import load_all_pdfs
from src.chunking import chunk_documents
from src.embeddings import EmbeddingModel
from src.vector_store import reset_collection, index_documents, query_collection
from src.retrieval import format_retrieval_results
from src.rag import generate_rag_answer, extract_sources


def build_vector_store(data_dir: str = "data/raw"):
    docs = load_all_pdfs(data_dir)
    chunked_docs = chunk_documents(docs)

    embedding_model = EmbeddingModel()
    chunk_texts = [doc["text"] for doc in chunked_docs]
    embeddings = embedding_model.embed_texts(chunk_texts)

    reset_collection()
    index_documents(chunked_docs, embeddings)

    return embedding_model, chunked_docs


def answer_question(question: str, embedding_model, n_results: int = 5, selected_source: str = "Tous"):
    query_embedding = embedding_model.embed_query(question)
    results = query_collection(query_embedding, n_results=10)
    retrieved_chunks = format_retrieval_results(results)

    if selected_source != "Tous":
        retrieved_chunks = [
            chunk for chunk in retrieved_chunks
            if chunk["source"] == selected_source
        ]

    retrieved_chunks = retrieved_chunks[:n_results]

    if not retrieved_chunks:
        return {
            "answer": "Aucun extrait pertinent n'a été trouvé pour ce filtre ou cette question.",
            "sources": [],
            "retrieved_chunks": [],
        }

    answer = generate_rag_answer(question, retrieved_chunks)
    sources = extract_sources(retrieved_chunks)

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": retrieved_chunks,
    }
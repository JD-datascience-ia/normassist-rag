import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.pipeline import build_vector_store, answer_question


st.set_page_config(page_title="NormAssist-RAG", layout="wide")

st.title("NormAssist-RAG")
st.write("Assistant RAG pour interroger des documents réglementaires et techniques.")

st.markdown("---")

@st.cache_resource
def load_pipeline():
    embedding_model, chunked_docs = build_vector_store("data/raw")
    return embedding_model, chunked_docs


with st.spinner("Initialisation du pipeline et indexation des documents..."):
    embedding_model, chunked_docs = load_pipeline()

st.success(f"Pipeline prêt. {len(chunked_docs)} chunks indexés.")

question = st.text_area(
    "Pose ta question",
    placeholder="Exemple : Quelles sont les caractéristiques d'une intelligence artificielle digne de confiance ?",
    height=100
)

if st.button("Lancer l'analyse"):
    if not question.strip():
        st.warning("Merci de saisir une question.")
    else:
        with st.spinner("Recherche des extraits pertinents et génération de la réponse..."):
            result = answer_question(question, embedding_model, n_results=5)

        st.subheader("Réponse")
        st.write(result["answer"])

        st.subheader("Sources")
        for source in result["sources"]:
            st.write(f"- {source}")

        with st.expander("Voir les extraits récupérés"):
            for i, chunk in enumerate(result["retrieved_chunks"], start=1):
                st.markdown(f"**Extrait {i}**")
                st.write(f"Source : {chunk['source']}")
                st.write(f"Page : {chunk['page']}")
                st.write(f"Distance : {chunk['distance']}")
                st.write(chunk["text"])
                st.markdown("---")
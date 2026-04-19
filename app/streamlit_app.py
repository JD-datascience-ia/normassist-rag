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

available_sources = sorted({doc["source"] for doc in chunked_docs})

st.success(f"Pipeline prêt. {len(chunked_docs)} chunks indexés.")

col1, col2 = st.columns([3, 1])

with col1:
    question = st.text_area(
        "Pose ta question",
        placeholder="Exemple : Quelles sont les caractéristiques d'une intelligence artificielle digne de confiance ?",
        height=120,
    )

with col2:
    selected_source = st.selectbox(
        "Filtrer par document",
        options=["Tous"] + available_sources
    )

st.markdown("### Exemples de questions")
st.markdown(
    """
- Quelles sont les caractéristiques d'une intelligence artificielle digne de confiance ?
- Que recommande la CNIL concernant les données personnelles dans l’IA ?
- Que dit le NIST sur la gestion du risque lié à l’IA ?
- Que dit l’AI Act sur une IA axée sur l’humain ?
"""
)

if st.button("Lancer l'analyse", use_container_width=True):
    if not question.strip():
        st.warning("Merci de saisir une question.")
    else:
        try:
            with st.spinner("Recherche des extraits pertinents et génération de la réponse..."):
                result = answer_question(
                    question,
                    embedding_model,
                    n_results=5,
                    selected_source=selected_source,
                )

            st.subheader("Réponse")
            st.write(result["answer"])

            st.subheader("Sources utilisées")
            for source in result["sources"]:
                st.markdown(f"- **{source['source']}** — page {source['page']}")

            with st.expander("Voir les extraits récupérés"):
                for i, chunk in enumerate(result["retrieved_chunks"], start=1):
                    st.markdown(f"### Extrait {i}")
                    st.markdown(f"**Source :** {chunk['source']}")
                    st.markdown(f"**Page :** {chunk['page']}")
                    st.markdown(f"**Distance :** {chunk['distance']:.4f}")
                    st.code(chunk["text"], language=None)
                    st.markdown("---")

        except Exception as e:
            st.error("Une erreur est survenue pendant l'analyse.")
            st.exception(e)
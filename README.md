# NormAssist-RAG

NormAssist-RAG est un assistant de question-réponse permettant d’interroger des documents techniques et réglementaires (PDF) à l’aide d’un système de Retrieval-Augmented Generation (RAG).

---

##  Objectif du projet

Ce projet vise à faciliter l’exploration de documents longs et complexes (normes, réglementations, guides techniques) grâce à :

- l’extraction de texte depuis des PDF
- le découpage en segments (chunking)
- la recherche sémantique
- la génération de réponses basées sur le contexte
- la citation des sources utilisées

---

##  Cas d’usage cible

L’assistant est conçu pour traiter des documents tels que :

- textes réglementaires (ex : AI Act, RGPD)
- recommandations d’organismes (CNIL, NIST)
- documents techniques structurés
- contenus proches des normes

---

##  Fonctionnalités principales

- ingestion de documents PDF
- extraction et nettoyage du texte
- génération de chunks
- création d’embeddings
- indexation dans une base vectorielle (Chroma)
- recherche sémantique
- génération de réponses avec citations des sources
- interface utilisateur via Streamlit

---

##  Architecture du projet

- `src/ingestion.py` : lecture et extraction des PDF
- `src/preprocessing.py` : nettoyage du texte
- `src/chunking.py` : découpage en segments
- `src/embeddings.py` : génération des embeddings
- `src/vector_store.py` : indexation dans Chroma
- `src/retrieval.py` : recherche des passages pertinents
- `src/rag.py` : génération des réponses
- `app/streamlit_app.py` : interface utilisateur

---

##  Structure du projet

normassist-rag/
├── app/
├── data/
├── notebooks/
├── src/
├── tests/
├── main.py
├── requirements.txt
├── README.md

---

##  État du projet

Projet en cours de développement (POC).

---

##  Étapes suivantes

1. Lecture et extraction des PDF
2. Structuration du texte
3. Création des chunks
4. Indexation dans la base vectorielle
5. Implémentation du moteur de recherche
6. Génération de réponses (RAG)
7. Développement de l’interface utilisateur

---

##  Perspectives d’amélioration

- amélioration de la qualité des réponses
- gestion avancée des sources
- optimisation des performances
- ajout d’une API (FastAPI)
- déploiement du projet

---

##  Technologies utilisées

- Python
- ChromaDB
- sentence-transformers
- OpenAI API (pour la génération)
- Streamlit

---
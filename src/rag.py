from typing import List, Dict
from openai import OpenAI

from src.config import OPENAI_API_KEY, LLM_MODEL
from src.prompt import build_rag_prompt


def build_context(retrieved_chunks: List[Dict]) -> str:
    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"""[Extrait {i}]
Source: {chunk['source']}
Page: {chunk['page']}
Texte:
{chunk['text']}
"""
        )

    return "\n\n".join(context_parts)


def extract_sources(retrieved_chunks: List[Dict]) -> List[Dict]:
    unique_sources = []
    seen = set()

    for chunk in retrieved_chunks:
        key = (chunk["source"], chunk["page"])
        if key not in seen:
            seen.add(key)
            unique_sources.append(
                {
                    "source": chunk["source"],
                    "page": chunk["page"],
                }
            )

    return unique_sources


def generate_rag_answer(question: str, retrieved_chunks: List[Dict]) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)

    context = build_context(retrieved_chunks)
    prompt = build_rag_prompt(question, context)

    response = client.responses.create(
        model=LLM_MODEL,
        input=prompt,
    )

    return response.output_text
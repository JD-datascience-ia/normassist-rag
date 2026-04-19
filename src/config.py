from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "paraphrase-multilingual-MiniLM-L12-v2")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", ".chroma")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "normassist_docs")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4.1-mini")
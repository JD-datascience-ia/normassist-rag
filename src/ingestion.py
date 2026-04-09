import fitz
import json
from pathlib import Path
from typing import List, Dict
import json
from src.preprocessing import clean_text

def load_pdf(file_path: str) -> List[Dict]:
    """
    Charge un pdf et extrait page par page.

    Returns:
        une lsite de dictionnaire avec:
        - source: nom du dossier pDF
        - page: numéro de page
        - text: texte extrait de la page
    """
    doc = fitz.open(file_path)
    documents = []

    for page_num, page in enumerate(doc):
        raw_text = page.get_text()
        text = clean_text(raw_text)

        if text:
            documents.append(
                {
                    "source": Path(file_path).name,
                    "page": page_num + 1,
                    "text": text,
                }
            )

    return documents


def load_all_pdfs(data_dir: str) -> List[Dict]:
    """
    Charge tout les pdf a partir d'un dossier et aggrege toutes les pages.
    """
    data_path = Path(data_dir)
    all_docs = []

    for pdf_file in data_path.glob("*.pdf"):
        print(f"Loading {pdf_file.name}...")
        docs = load_pdf(str(pdf_file))
        all_docs.extend(docs)

    return all_docs


def save_documents_to_json(documents: List[Dict], output_path: str) -> None:
    """
    Sauvegarde les documents extrait sous format JSON.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print(f"Saved extracted documents to {output_file}")
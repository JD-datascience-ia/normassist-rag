import re


def clean_text(text: str) -> str:
    """
    Nettoyage texte basique:
    - Suppression d'espaces répété
    - normaliser les sauts de ligne
    - Supprimer les espaces de début et de fin
    """
    text = re.sub(r"\r\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()
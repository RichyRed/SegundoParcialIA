# analysis.py

from fastapi import APIRouter
from datetime import datetime
from transformers import pipeline
import spacy

router = APIRouter()

# Importa el modelo preentrenado para análisis de sentimientos
sentiment_analyzer = pipeline("sentiment-analysis")
nlp = spacy.load("es_core_news_md")

@router.post("/analysis")
def detailed_analysis(text: str):
    """
    Endpoint para inferencia de análisis sintáctico y de sentimiento.
    """
    try:
        # Tu lógica actual de análisis sintáctico y de sentimientos
        doc = nlp(text)
        result = sentiment_analyzer(text)

        # Detecta y lista los verbos en el párrafo
        verbs = [token.text for token in doc if token.pos_ == "VERB"]

        # Detecta y lista los nombres de personas en el texto
        persons = [ent.text for ent in doc.ents if ent.label_ == "PER"]

        # Redondea el score de sentimiento a 2 decimales
        sentiment_score = round(result[0]["score"], 2)

        # Ajusta el formato del score según el sentimiento
        if result[0]["label"].lower() == "negative":
            sentiment_score *= -1

        # Agrega POS tagging
        pos_tags = [(token.text, token.pos_) for token in doc]

        # Agrega Named Entity Recognition (NER)
        ner_entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Agrega Embedding
        embedding = [token.vector.tolist() for token in doc]

        return {
            "analysis": {
                "syntax": {
                    "verbs": verbs,
                },
                "entities": {
                    "persons": persons,
                },
                "sentiment": {
                    "label": result[0]["label"],
                    "score": sentiment_score,
                },
                "pos_tags": pos_tags,
                "ner_entities": ner_entities,
                "embedding": embedding,
            }
        }

    except Exception as e:
        return {"error": str(e)}

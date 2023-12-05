from fastapi import APIRouter
from datetime import datetime
from transformers import pipeline
import spacy
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download('wordnet')

router = APIRouter()

sentiment_analyzer = pipeline("sentiment-analysis")
nlp = spacy.load("es_core_news_md")

@router.post("/analysis")
def detailed_analysis(text: str):
    """
    Aqui veremos inferencia de análisis sintáctico y de sentimiento.
    """
    try:
        doc = nlp(text)
        result = sentiment_analyzer(text)

        result_keywords = ["ganaron", "victoria", "triunfo", "gano", "triunfaron", "derrotaron", "vencieron"]
        lost_keywords = ["perdieron", "derrota", "perdedor", "perdio", "cayeron", "no", "cayo"]

        result_keywords += get_synonyms(result_keywords)
        lost_keywords += get_synonyms(lost_keywords)

        result_detection = any(keyword in text.lower() for keyword in result_keywords)
        lost_detection = any(keyword in text.lower() for keyword in lost_keywords)

        if result_detection:
            match_result = "GANARON"
        elif lost_detection:
            match_result = "PERDIERON"
        else:
            match_result = "EMPATE"

        verbs = [token.text for token in doc if token.pos_ == "VERB"]

        persons = [ent.text for ent in doc.ents if ent.label_ == "PER"]

        sentiment_score = round(result[0]["score"], 2)

        if result[0]["label"].lower() == "negative":
            sentiment_score *= -1

        # POS tagging
        pos_tags = [(token.text, token.pos_) for token in doc]

        # Named Entity Recognition (NER)
        ner_entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Embedding
        embedding = [token.vector.tolist() for token in doc]

        return {
            "analysis": {
                "match_result": match_result,
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

def get_synonyms(keywords):
    synonyms = []
    for keyword in keywords:
        for syn in wordnet.synsets(keyword):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name().lower())
    return synonyms

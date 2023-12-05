from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from src.config import get_settings
from datetime import datetime
from transformers import pipeline
import spacy

_SETTINGS = get_settings()

app = FastAPI(
    title=_SETTINGS.service_name,
    version=_SETTINGS.k_revision
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importa el modelo preentrenado para análisis de sentimientos
sentiment_analyzer = pipeline("sentiment-analysis")
nlp = spacy.load("es_core_news_md")

# Endpoint para lectura de status del servicio
@app.get("/status", response_model=str)
def get_status():
    """
    Analisis de Partidos Futlocos

    Analizaremos a fondo, nuestros textos futbolisticos favoritos para ver si nuestro equipo gano o perdio el partido :)
    """
    # Formatea la información deseada como una cadena de texto
    return f"Service Name: {_SETTINGS.service_name}, Model Name: Analisis de partidos, Your Name: Richard Rojas, Version: {_SETTINGS.k_revision}"


# Endpoint para inferencia de análisis de sentimiento
@app.post("/sentiment")
def sentiment_analysis(text: str):
    """
    Endpoint para inferencia de análisis de sentimiento.
    """
    try:
        # Registro de tiempo de inicio
        start_time = datetime.now()

        # Realiza la inferencia de sentimiento utilizando la biblioteca Transformers
        result = sentiment_analyzer(text)

        # Registro de tiempo de finalización
        end_time = datetime.now()
        execution_time = end_time - start_time

        # Obtén el sentimiento y la puntuación
        sentiment_label = result[0]["label"]
        sentiment_score = round(result[0]["score"], 2)

        # Ajusta el formato de la puntuación según el sentimiento
        if sentiment_label.lower() == "negative":
            sentiment_score *= -1

        # Formatea la información de la predicción y ejecución
        prediction_info = {
            "sentiment_label": sentiment_label,
            "sentiment_score": sentiment_score,
        }

        execution_info = {
            "execution_time": str(execution_time),
            "other_information": "Otra información relevante sobre la ejecución",
        }

        # Devuelve la información de la predicción y ejecución
        return {"prediction": prediction_info, "execution": execution_info}

    except Exception as e:
        # Captura y muestra cualquier excepción que pueda ocurrir
        return {"error": str(e)}

# Nuevo endpoint para análisis más detallado
@app.post("/analysis")
def detailed_analysis(text: str):
    """
    Endpoint para inferencia de análisis sintáctico y de sentimiento.
    """
    try:
        # Registro de tiempo de inicio
        start_time = datetime.now()

        # Realiza la inferencia de análisis sintáctico utilizando spaCy
        doc = nlp(text)

        # Contar sujetos, nombres de personas y verbos
        subjects = [token.text for token in doc if token.dep_ == "nsubj"]
        persons = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        verbs = [token.text for token in doc if token.pos_ == "VERB"]

        # Buscar palabras clave para determinar si el equipo ganó o perdió
        result_keywords = ["ganó", "ganaron", "victoria", "victorioso", "triunfo"]
        lost_keywords = ["perdió", "perdieron", "derrota", "derrotado", "perdedor"]

        # Verificar si el equipo ganó o perdió
        result_detection = any(keyword in text.lower() for keyword in result_keywords)
        lost_detection = any(keyword in text.lower() for keyword in lost_keywords)

        # Realiza la inferencia de sentimiento utilizando la biblioteca Transformers
        result_sentiment = sentiment_analyzer(text)

        # Registro de tiempo de finalización
        end_time = datetime.now()
        execution_time = end_time - start_time

        # Obtén el sentimiento y la puntuación
        sentiment_label = result_sentiment[0]["label"]
        sentiment_score = round(result_sentiment[0]["score"], 2)

        # Formatea la información de la predicción y ejecución
        prediction_info = {
            "sentiment_label": sentiment_label,
            "sentiment_score": sentiment_score,
            "result_detection": "Gano" if result_detection else "Perdio" if lost_detection else "No se detecta resultado",
        }

        execution_info = {
            "execution_time": str(execution_time),
            "subjects": subjects,
            "persons": persons,
            "verbs": verbs,
        }

        # Devuelve la información de la predicción y ejecución
        return {"prediction": prediction_info, "execution": execution_info}

    except Exception as e:
        # Captura y muestra cualquier excepción que pueda ocurrir
        return {"error": str(e)}
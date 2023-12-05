# main.py

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from src.config import get_settings
from transformers import pipeline
from datetime import datetime

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

# Importa las rutas y funciones de análisis desde otro archivo
from src.analysis import router as analysis_router

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

        # Calcula el número de caracteres y palabras analizadas
        num_characters = len(text)
        num_words = len(text.split())

        # Formatea la información de la predicción y ejecución
        prediction_info = {
            "sentiment_label": sentiment_label,
            "sentiment_score": sentiment_score,
        }

        execution_info = {
            "execution_time": str(execution_time),
            "num_characters": num_characters,
            "num_words": num_words,
        }

        # Devuelve la información de la predicción y ejecución
        return {"prediction": prediction_info, "execution": execution_info}

    except Exception as e:
        # Captura y muestra cualquier excepción que pueda ocurrir
        return {"error": str(e)}

app.include_router(analysis_router)

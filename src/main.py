from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from src.config import get_settings
from transformers import pipeline
from datetime import datetime
from src.reports import router as reports_router 

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

sentiment_analyzer = pipeline("sentiment-analysis")

from src.analysis import router as analysis_router

# Get Status
@app.get("/status", response_model=str)
def get_status():
    """
    Analisis de Partidos Fuchibol

    Analizaremos a fondo, nuestros textos futbolisticos favoritos para ver si nuestro equipo gano o perdio el partido :)
    """
    return f"Service Name: {_SETTINGS.service_name}, Model Name: Analisis de partidos, Your Name: Richard Rojas, Version: {_SETTINGS.k_revision}"

# Sentimiento
@app.post("/sentiment")
def sentiment_analysis(text: str):
    """
    Endpoint para inferencia de análisis de sentimiento.
    """
    try:
        start_time = datetime.now()

        result = sentiment_analyzer(text)

        end_time = datetime.now()
        execution_time = end_time - start_time

        sentiment_label = result[0]["label"]
        sentiment_score = round(result[0]["score"], 2)

        if sentiment_label.lower() == "negative":
            sentiment_score *= -1

        num_characters = len(text)
        num_words = len(text.split())

        prediction_info = {
            "sentiment_label": sentiment_label,
            "sentiment_score": sentiment_score,
        }

        execution_info = {
            "execution_time": str(execution_time),
            "num_characters": num_characters,
            "num_words": num_words,
        }

        return {"prediction": prediction_info, "execution": execution_info}

    except Exception as e:
        return {"error": str(e)}

app.include_router(analysis_router)

app.include_router(reports_router)
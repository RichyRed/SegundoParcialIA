FROM python:3.11-slim

ARG OPENAI_KEY
ENV OPENAI_KEY=$OPENAI_KEY
ENV PORT 8000

# Instala spaCy y las dependencias necesarias
RUN pip install -U spacy
RUN python -m spacy download es_core_news_md

# Instala las dependencias de PyTorch y TensorFlow
RUN pip install tensorflow

# Instala otras dependencias desde requirements.txt
COPY requirements.txt /
RUN pip install -r requirements.txt

COPY ./src /src

CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT}

# AnalizadorFuchibol
## Descripción
AnalizadorFuchibol es una API construida con FastAPI que proporciona funcionalidades para el análisis sintáctico, análisis de sentimientos y generación de informes de inferencia relacionados con partidos de fútbol. La aplicación utiliza modelos preentrenados para realizar análisis sintáctico y de sentimientos.

## Funcionalidades
La API proporciona los siguientes endpoints:

* /status (GET)
Endpoint que devuelve información sobre el estado del servicio, incluyendo el nombre del servicio, el nombre del modelo utilizado y la versión actual.

* /sentiment (POST)
Endpoint para realizar análisis de sentimientos en un texto proporcionado. Devuelve la etiqueta de sentimiento (positivo, negativo o neutro) y la puntuación asociada.

* /analysis (POST)
Endpoint para realizar análisis sintáctico y de sentimientos en un texto proporcionado. Proporciona información detallada sobre sujetos, verbos, nombres de personas y el sentimiento del texto. Además, detecta si el texto indica que el equipo ganó, perdió o empató.

* /reports (GET)
Endpoint para generar informes de inferencia en formato CSV. El informe incluye detalles sobre la predicción, como el nombre del archivo, etiqueta de sentimiento, puntuación de sentimiento, resultado del partido, tiempo de ejecución y modelo utilizado.

## Uso
Todo lo que debe hacer para poder realizar el analisis de su partido favorito, es poniendo el texto que desea analizar en el post de Analysis, y despues podra ver los satisfactorios resultados de esta aplicacion.

## Autor
Nombre: Richard Rojas
Codigo> 55077

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
La AnalizadorFuchibol API proporciona un servicio eficiente para el análisis de textos vinculados a partidos de fútbol. Al hacer solicitudes POST con tus textos específicos, la API realizará análisis sintácticos y de sentimientos, brindándote información valiosa sobre los sujetos, verbos, nombres de personas, sentimientos y la deducción de los resultados del partido (ganó, perdió o empató). Además, puedes utilizar el endpoint /sentiment para obtener una evaluación más general del sentimiento en tus textos. El endpoint /reports te permite generar informes detallados en formato CSV, proporcionando datos esenciales sobre el nombre del archivo, la etiqueta de sentimiento, la puntuación de sentimiento, el resultado del partido, el tiempo de ejecución y el modelo utilizado. ¡Integra AnalizadorFuchibol API y aprovecha estas poderosas capacidades de análisis de texto para tus textos futbolísticos favoritos!

## Recuerda
Podemos usar cualquier tipo de texto o articulo deportivo para ver el funcionamiento de la aplicacion, puedes poner el que tu prefieras. Los ejemplos que estan dentro del src, son solo textos cortos para no perder mucho tiempo en la ejecución.

Nombre: Richard Rojas
Codigo: 55077

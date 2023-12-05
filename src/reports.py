import csv
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from src.analysis import detailed_analysis

router = APIRouter()

filename = "ReportesFuchibol.csv"

@router.get("/reports")
def generate_report():
    try:
        analysis_result = detailed_analysis("Texto de ejemplo para la predicción")
        prediction_info = analysis_result.get("analysis", {})
        sentiment_label = prediction_info.get("sentiment", {}).get("label", "")
        sentiment_score = prediction_info.get("sentiment", {}).get("score", "")
        match_result = prediction_info.get("match_result", "")
        execution_time = analysis_result.get("execution", {}).get("execution_time", "")
        model_used = "DistilBERT" 

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Agregar una nueva fila al archivo CSV
            writer.writerow([current_datetime, sentiment_label, sentiment_score, 
                             match_result, execution_time, model_used])

        return {"message": f"Report updated successfully in {filename}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

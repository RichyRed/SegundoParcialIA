from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Your Service Name",
    version="your_revision"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_llm_service():
    # Puedes proporcionar una implementación para esta función si es necesario
    pass

@app.post("/generate")
def generate_project(params: dict, service: dict = Depends(get_llm_service)) -> dict:
    # Puedes proporcionar una implementación para esta función si es necesario
    pass

@app.get("/")
def root():
    return {"status": "OK"}

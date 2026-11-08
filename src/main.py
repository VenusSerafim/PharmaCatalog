from fastapi import FastAPI

app = FastAPI(
    title="PharmaCatalog API",
    description=(
        "API para gerenciamento e padronização "
        "de informações farmacêuticas."
    ),
    version="0.1.0",
)


@app.get("/", tags=["Geral"])
def read_root():
    return {
        "message": "Bem-vindo à API PharmaCatalog",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health", tags=["Geral"])
def health_check():
    return {
        "status": "healthy",
        "application": "PharmaCatalog",
    }

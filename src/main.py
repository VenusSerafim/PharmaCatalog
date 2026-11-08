from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routes.medications import router as medications_router

from src.database.connection import (
    connect_to_mongo,
    close_mongo_connection,
    get_database
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_to_mongo()
    yield
    close_mongo_connection()


app = FastAPI(
    title="PharmaCatalog API",
    description="API para gerenciamento e padronização de informações farmacêuticas.",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(medications_router)

@app.get("/", tags=["Geral"])
def read_root():
    return {
        "message": "Bem-vindo à API PharmaCatalog",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/health", tags=["Geral"])
def health_check():
    return {
        "status": "healthy",
        "application": "PharmaCatalog"
    }


@app.get("/health/database", tags=["Banco de Dados"])
def database_health():
    db = get_database()

    return {
        "database": db.name,
        "status": "connected",
        "collections": db.list_collection_names()
    }

    print("ROTAS REGISTRADAS:", [route.path for route in app.routes])
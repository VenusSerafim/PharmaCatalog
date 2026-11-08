
import pytest
from bson import Decimal128, ObjectId
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.routes import medications


# Aplicação isolada para os testes, sem iniciar o MongoDB real.
app = FastAPI()
app.include_router(medications.router)

client = TestClient(app)


class FakeCollection:
    def __init__(self):
        self.documents = [
            {
                "_id": ObjectId(),
                "nome_generico": "Meropenem",
                "nome_comercial": "Meronem",
                "categoria": "Antimicrobiano",
                "concentracao": "1 g",
                "apresentacao": "Frasco-ampola",
                "preco_aquisicao": Decimal128("28.90"),
                "moeda": "BRL",
                "status": "ativo"
            },
            {
                "_id": ObjectId(),
                "nome_generico": "Vancomicina",
                "nome_comercial": None,
                "categoria": "Antimicrobiano",
                "concentracao": "500 mg",
                "apresentacao": "Frasco-ampola",
                "preco_aquisicao": Decimal128("15.00"),
                "moeda": "BRL",
                "status": "inativo"
            }
        ]

    def find(self, filtro=None):
        filtro = filtro or {}

        if "status" in filtro:
            return [
                item for item in self.documents
                if item["status"] == filtro["status"]
            ]

        return self.documents


class FakeDatabase:
    def __init__(self):
        self.collection = FakeCollection()

    def __getitem__(self, name):
        return self.collection


@pytest.fixture
def fake_database(monkeypatch):
    database = FakeDatabase()

    monkeypatch.setattr(
        medications,
        "get_database",
        lambda: database
    )

    return database


def test_listar_medicamentos_ativos(fake_database):
    response = client.get("/medicamentos/?status=ativo")

    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert response.json()["medicamentos"][0]["status"] == "ativo"


def test_listar_medicamentos_inativos(fake_database):
    response = client.get("/medicamentos/?status=inativo")

    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert response.json()["medicamentos"][0]["status"] == "inativo"


def test_listar_todos_os_medicamentos(fake_database):
    response = client.get("/medicamentos/?status=todos")

    assert response.status_code == 200
    assert response.json()["total"] == 2


def test_rejeitar_status_invalido(fake_database):
    response = client.get("/medicamentos/?status=qualquer")

    assert response.status_code == 422

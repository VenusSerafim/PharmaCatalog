
import re
from datetime import datetime, timezone

from bson import Decimal128, ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, Query, status

from src.database.connection import get_database
from src.schemas.medication import MedicationCreate


router = APIRouter(
    prefix="/medicamentos",
    tags=["Medicamentos"]
)


# =====================================================
# CADASTRAR MEDICAMENTO
# =====================================================

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medication(medication: MedicationCreate):

    db = get_database()

    if db is None:
        raise HTTPException(
            status_code=503,
            detail="Banco de dados indisponível."
        )

    data = medication.model_dump()

    data["preco_aquisicao"] = Decimal128(
        str(data["preco_aquisicao"])
    )

    data["status"] = "ativo"
    data["created_at"] = datetime.now(timezone.utc)
    data["updated_at"] = datetime.now(timezone.utc)

    result = db["medicamentos"].insert_one(data)

    return {
        "id": str(result.inserted_id),
        "nome_generico": medication.nome_generico,
        "nome_comercial": medication.nome_comercial,
        "categoria": medication.categoria,
        "concentracao": medication.concentracao,
        "apresentacao": medication.apresentacao,
        "preco_aquisicao": str(medication.preco_aquisicao),
        "moeda": medication.moeda,
        "status": "ativo",
        "message": "Medicamento cadastrado com sucesso."
    }


# =====================================================
# LISTAR MEDICAMENTOS
# GET /medicamentos/
# =====================================================

@router.get("/")
def list_medications(
    status: str = Query(
        default="ativo",
        pattern="^(ativo|inativo|todos)$"
    )
):

    db = get_database()

    if db is None:
        raise HTTPException(
            status_code=503,
            detail="Banco de dados indisponível."
        )

    filtro = {} if status == "todos" else {"status": status}

    medications = []

    for item in db["medicamentos"].find(filtro):

        medications.append({
            "id": str(item["_id"]),
            "nome_generico": item["nome_generico"],
            "nome_comercial": item.get("nome_comercial"),
            "categoria": item["categoria"],
            "concentracao": item["concentracao"],
            "apresentacao": item["apresentacao"],
            "preco_aquisicao": str(
                item["preco_aquisicao"].to_decimal()
            ),
            "moeda": item["moeda"],
            "status": item["status"]
        })

    return {
        "total": len(medications),
        "status_consultado": status,
        "medicamentos": medications
    }


# =====================================================
# PESQUISAR MEDICAMENTO POR NOME
# =====================================================

@router.get("/buscar")
def search_medications(
    nome: str = Query(..., min_length=2)
):

    db = get_database()

    if db is None:
        raise HTTPException(
            status_code=503,
            detail="Banco de dados indisponível."
        )

    termo = re.escape(nome)

    filtro = {
        "$or": [
            {
                "nome_generico": {
                    "$regex": termo,
                    "$options": "i"
                }
            },
            {
                "nome_comercial": {
                    "$regex": termo,
                    "$options": "i"
                }
            }
        ]
    }

    resultados = []

    for item in db["medicamentos"].find(filtro):

        resultados.append({
            "id": str(item["_id"]),
            "nome_generico": item["nome_generico"],
            "nome_comercial": item.get("nome_comercial"),
            "categoria": item["categoria"],
            "concentracao": item["concentracao"],
            "apresentacao": item["apresentacao"],
            "preco_aquisicao": str(
                item["preco_aquisicao"].to_decimal()
            ),
            "moeda": item["moeda"],
            "status": item["status"]
        })

    return {
        "termo_pesquisado": nome,
        "total": len(resultados),
        "medicamentos": resultados
    }


# =====================================================
# CONSULTAR MEDICAMENTO POR ID
# =====================================================

@router.get("/{medication_id}")
def get_medication(medication_id: str):

    db = get_database()

    if db is None:
        raise HTTPException(
            status_code=503,
            detail="Banco de dados indisponível."
        )

    try:
        object_id = ObjectId(medication_id)

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="ID de medicamento inválido."
        )

    item = db["medicamentos"].find_one({
        "_id": object_id
    })

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Medicamento não encontrado."
        )

    return {
        "id": str(item["_id"]),
        "nome_generico": item["nome_generico"],
        "nome_comercial": item.get("nome_comercial"),
        "categoria": item["categoria"],
        "concentracao": item["concentracao"],
        "apresentacao": item["apresentacao"],
        "preco_aquisicao": str(
            item["preco_aquisicao"].to_decimal()
        ),
        "moeda": item["moeda"],
        "status": item["status"]
    }


# =====================================================
# ATUALIZAR MEDICAMENTO
# =====================================================

@router.put("/{medication_id}")
def update_medication(
    medication_id: str,
    medication: MedicationCreate
):

    db = get_database()

    if db is None:
        raise HTTPException(
            status_code=503,
            detail="Banco de dados indisponível."
        )

    try:
        object_id = ObjectId(medication_id)

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="ID de medicamento inválido."
        )

    data = medication.model_dump()

    data["preco_aquisicao"] = Decimal128(
        str(data["preco_aquisicao"])
    )

    data["updated_at"] = datetime.now(timezone.utc)

    result = db["medicamentos"].update_one(
        {"_id": object_id},
        {"$set": data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Medicamento não encontrado."
        )

    return {
        "id": medication_id,
        "message": "Medicamento atualizado com sucesso."
    }


# =====================================================
# INATIVAR MEDICAMENTO
# =====================================================

@router.patch("/{medication_id}/inativar")
def deactivate_medication(medication_id: str):

    db = get_database()

    if db is None:
        raise HTTPException(
            status_code=503,
            detail="Banco de dados indisponível."
        )

    try:
        object_id = ObjectId(medication_id)

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="ID de medicamento inválido."
        )

    result = db["medicamentos"].update_one(
        {
            "_id": object_id,
            "status": "ativo"
        },
        {
            "$set": {
                "status": "inativo",
                "updated_at": datetime.now(timezone.utc)
            }
        }
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Medicamento não encontrado ou já inativo."
        )

    return {
        "id": medication_id,
        "status": "inativo",
        "message": "Medicamento inativado com sucesso."
    }

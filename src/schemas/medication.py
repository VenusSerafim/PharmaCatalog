from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal


class MedicationCreate(BaseModel):
    nome_generico: str = Field(..., min_length=2)
    nome_comercial: Optional[str] = None
    categoria: str = "Antimicrobiano"
    concentracao: str
    apresentacao: str
    preco_aquisicao: Decimal = Field(..., ge=0)
    moeda: str = "BRL"
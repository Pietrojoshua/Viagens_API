from pydantic import BaseModel
from typing import Optional


class PassageiroBase(BaseModel):
    id_usuario: int
    nome_passageiro: str
    media_avaliacao: Optional[float]


class PassageiroResponse(PassageiroBase):
    id_passageiro: int

    class Config:
        from_attributes = True
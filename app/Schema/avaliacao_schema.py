from pydantic import BaseModel
from datetime import datetime

class AvaliacaoBase(BaseModel):
    nota_passageiro: float
    nota_motorista: float
    datahora_limite: datetime


class AvaliacaoResponse(AvaliacaoBase):
    id_avaliacao: int

    class Config:
        from_attributes = True
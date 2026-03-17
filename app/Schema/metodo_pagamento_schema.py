from pydantic import BaseModel

class MetodoPagamentoBase(BaseModel):
    descricao: str
    nome_financeira: str


class MetodoPagamentoResponse(MetodoPagamentoBase):
    id_metodo_pagamento: int

    class Config:
        from_attributes = True
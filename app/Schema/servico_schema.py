from pydantic import BaseModel

class ServicoBase(BaseModel):
    nome_servico: str
    id_classe_minima: int


class ServicoResponse(ServicoBase):
    id_servico: int

    class Config:
        from_attributes = True
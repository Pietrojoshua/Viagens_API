from pydantic import BaseModel


class TipoCombustivelBase(BaseModel):
    descricao: str
    fator_carbono: float

#Essa é uma tabela de domínio, então os dados são pré-cadastrados no banco e 
# não precisam ser inseridos pelo usuário, ou seja, nao precisa do Create

class TipoCombustivelResponse(TipoCombustivelBase):
    id_tipo_combustivel: int

    class Config:
        from_attributes = True
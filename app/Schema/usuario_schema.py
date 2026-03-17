from pydantic import BaseModel
from datetime import date


class UsuarioBase(BaseModel): # Tudo que o usuário precisa ter para criar um usuário
    nome: str
    cpf: str
    data_nascimento: date
    email: str
    username: str


class UsuarioCreate(UsuarioBase): # Oq o usuário precisar criar para gerar o usuário junto com as informações da base
    senha: str # A senha é tranformada em hash e salva no banco 


class UsuarioResponse(UsuarioBase): # Oq a API vai retornar para mim quando o usuário for criado
    id_usuario: int
    # Não retorna a senha por motivos de segurança

    class Config: #Isso permite que o FastAPI pegue dados direto do banco e coverta para Json
        from_attributes = True
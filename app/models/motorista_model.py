from sqlalchemy import Column, BigInteger, ForeignKey, String,DECIMAL
from app.database import Base


class Motorista(Base):
    __tablename__ = "motorista"

    id_motorista = Column(BigInteger, primary_key=True)
    nome_motorista= Column(String(255))
    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario"))
    media_avaliacao = Column(DECIMAL(3,2))
    cnh = Column(BigInteger)
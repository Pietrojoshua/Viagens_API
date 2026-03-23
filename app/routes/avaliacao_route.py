from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao_model import Avaliacao
from app.Schema.avaliacao_schema import AvaliacaoBase, AvaliacaoResponse

router = APIRouter(prefix="/avaliacoes", tags=["avaliacoes"])

# Criar
@router.post("/", response_model=AvaliacaoResponse)
def criar(dados: AvaliacaoBase, db: Session = Depends(get_db)):
    novo = Avaliacao(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Listar
@router.get("/", response_model=list[AvaliacaoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Avaliacao).all()

# Buscar por ID
@router.get("/{id}", response_model=AvaliacaoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == id).first()
    
    if not avaliacao:
        raise HTTPException(404, "Não encontrado")

    return avaliacao

# Atualizar
@router.put("/{id}", response_model=AvaliacaoResponse)
def atualizar(id: int, dados: AvaliacaoBase, db: Session = Depends(get_db)):
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == id).first()

    if not avaliacao:
        raise HTTPException(404, "Não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(avaliacao, campo, valor)

    db.commit()
    db.refresh(avaliacao)
    return avaliacao

# Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == id).first()

    if not avaliacao:
        raise HTTPException(404, "Não encontrado")

    db.delete(avaliacao)
    db.commit()
    return {"msg": "Deletado"}
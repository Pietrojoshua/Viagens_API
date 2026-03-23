from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamento_model import Pagamento
from app.Schema.pagamento_schema import PagamentoBase, PagamentoResponse

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])

# Criar
@router.post("/", response_model=PagamentoResponse)
def criar(dados: PagamentoBase, db: Session = Depends(get_db)):
    novo = Pagamento(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Listar
@router.get("/", response_model=list[PagamentoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Pagamento).all()

# Buscar por ID
@router.get("/{id}", response_model=PagamentoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()
    
    if not pagamento:
        raise HTTPException(404, "Não encontrado")

    return pagamento

# Atualizar
@router.put("/{id}", response_model=PagamentoResponse)
def atualizar(id: int, dados: PagamentoBase, db: Session = Depends(get_db)):
    pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()

    if not pagamento:
        raise HTTPException(404, "Não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(pagamento, campo, valor)

    db.commit()
    db.refresh(pagamento)
    return pagamento

# Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()

    if not pagamento:
        raise HTTPException(404, "Não encontrado")

    db.delete(pagamento)
    db.commit()
    return {"msg": "Deletado"}
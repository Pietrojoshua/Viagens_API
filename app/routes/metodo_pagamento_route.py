from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.metodo_pagamento_model import MetodoPagamento
from app.Schema.metodo_pagamento_schema import MetodoPagamentoBase, MetodoPagamentoResponse

router = APIRouter(prefix="/metodos_pagamento", tags=["metodos_pagamento"])

# Criar
@router.post("/", response_model=MetodoPagamentoResponse)
def criar(dados: MetodoPagamentoBase, db: Session = Depends(get_db)):
    novo = MetodoPagamento(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Listar
@router.get("/", response_model=list[MetodoPagamentoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(MetodoPagamento).all()

# Buscar por ID
@router.get("/{id}", response_model=MetodoPagamentoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()
    
    if not metodo:
        raise HTTPException(404, "Não encontrado")

    return metodo

# Atualizar
@router.put("/{id}", response_model=MetodoPagamentoResponse)
def atualizar(id: int, dados: MetodoPagamentoBase, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()

    if not metodo:
        raise HTTPException(404, "Não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(metodo, campo, valor)

    db.commit()
    db.refresh(metodo)
    return metodo

# Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()

    if not metodo:
        raise HTTPException(404, "Não encontrado")

    db.delete(metodo)
    db.commit()
    return {"msg": "Deletado"}
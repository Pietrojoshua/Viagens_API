from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_combustivel_model import TipoCombustivel
from app.Schema.tipo_combustivel_schema import TipoCombustivelBase, TipoCombustivelResponse

router = APIRouter(prefix="/tipos_combustivel", tags=["tipos_combustivel"])

# Criar
@router.post("/", response_model=TipoCombustivelResponse)
def criar(dados: TipoCombustivelBase, db: Session = Depends(get_db)):
    novo = TipoCombustivel(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Listar
@router.get("/", response_model=list[TipoCombustivelResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(TipoCombustivel).all()

# Buscar por ID
@router.get("/{id}", response_model=TipoCombustivelResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoCombustivel).filter(TipoCombustivel.id_tipo_combustivel == id).first()
    
    if not tipo:
        raise HTTPException(404, "Não encontrado")

    return tipo

# Atualizar
@router.put("/{id}", response_model=TipoCombustivelResponse)
def atualizar(id: int, dados: TipoCombustivelBase, db: Session = Depends(get_db)):
    tipo = db.query(TipoCombustivel).filter(TipoCombustivel.id_tipo_combustivel == id).first()

    if not tipo:
        raise HTTPException(404, "Não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(tipo, campo, valor)

    db.commit()
    db.refresh(tipo)
    return tipo

# Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoCombustivel).filter(TipoCombustivel.id_tipo_combustivel == id).first()

    if not tipo:
        raise HTTPException(404, "Não encontrado")

    db.delete(tipo)
    db.commit()
    return {"msg": "Deletado"}
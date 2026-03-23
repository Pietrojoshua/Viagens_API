from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe_veiculo_model import ClasseVeiculo
from app.Schema.classe_veiculo_schema import ClasseVeiculoBase, ClasseVeiculoResponse

router = APIRouter(prefix="/classes_veiculo", tags=["classes_veiculo"])

# Criar
@router.post("/", response_model=ClasseVeiculoResponse)
def criar(dados: ClasseVeiculoBase, db: Session = Depends(get_db)):
    novo = ClasseVeiculo(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# Listar
@router.get("/", response_model=list[ClasseVeiculoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(ClasseVeiculo).all()

# Buscar por ID
@router.get("/{id}", response_model=ClasseVeiculoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseVeiculo).filter(ClasseVeiculo.id_classe_veiculo == id).first()
    
    if not classe:
        raise HTTPException(404, "Não encontrado")

    return classe

# Atualizar
@router.put("/{id}", response_model=ClasseVeiculoResponse)
def atualizar(id: int, dados: ClasseVeiculoBase, db: Session = Depends(get_db)):
    classe = db.query(ClasseVeiculo).filter(ClasseVeiculo.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(404, "Não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(classe, campo, valor)

    db.commit()
    db.refresh(classe)
    return classe

# Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseVeiculo).filter(ClasseVeiculo.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(404, "Não encontrado")

    db.delete(classe)
    db.commit()
    return {"msg": "Deletado"}
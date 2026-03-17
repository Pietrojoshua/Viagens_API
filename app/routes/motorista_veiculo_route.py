from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_veiculo_model import MotoristaVeiculo
from app.Schema.motorista_veiculo_schema import MotoristaVeiculoBase, MotoristaVeiculoResponse

router = APIRouter(prefix="/Motorista Veiculos", tags=["Motorista Veiculos"])

#Criar
@router.post("/", response_model=MotoristaVeiculoResponse)
def criar(dados: MotoristaVeiculoBase, db: Session = Depends(get_db)):
    novo = MotoristaVeiculo(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar
@router.get("/", response_model=list[MotoristaVeiculoResponse])
def buscar(id: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculo).filter(MotoristaVeiculo.id_motoristaVeiculo == id).first()
    if not motorista_veiculo:
        raise HTTPException(404, "Não encontrado")
    return motorista_veiculo

# Atualizar Veiculo
@router.put("/{id}", response_model=MotoristaVeiculoBase)
def atualizar(id: int, dados: MotoristaVeiculoBase, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculo).filter(MotoristaVeiculo.id_motoristaVeiculo == id).first()
    if not motorista_veiculo:
        raise HTTPException(404, "Não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(motorista_veiculo, campo, valor)

    db.commit()
    db.refresh(motorista_veiculo)
    return motorista_veiculo

# Deletar Motorista_Veículo
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculo).filter(MotoristaVeiculo.id_motoristaVeiculo == id).first()

    if not motorista_veiculo:
        raise HTTPException(404, "Não encontrado")

    db.delete(motorista_veiculo)
    db.commit()
    return {"msg": "Deletado"}

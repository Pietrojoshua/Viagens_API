from fastapi import FastAPI
from app.routes import motorista_route, usuario_route, passageiro_route, motorista_route, motorista_veiculo_route, veiculo_route, tipo_combustivel_route, servico_route, pagamento_route, metodo_pagamento_route, modelo_veiculo 

from app.database import engine, Base
from app.models import veiculo_model   

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_route.router)
app.include_router(passageiro_route.router)
app.include_router(motorista_route.router)
app.include_router(motorista_veiculo_route.router)
app.include_router(veiculo_route.router)
app.include_router(tipo_combustivel_route.router)
app.include_router(servico_route.router)
app.include_router(motorista_route.router)
app.include_router(pagamento_route.router)
app.include_router(modelo_veiculo.router)
app.include_router(metodo_pagamento_route.router)
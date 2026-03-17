from fastapi import FastAPI
from app.routes import motorista_route, usuario_route, passageiro_route, motorista_route, motorista_veiculo_route

from app.database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(usuario_route.router)
app.include_router(passageiro_route.router)
app.include_router(motorista_route.router)
app.include_router(motorista_veiculo_route.router)

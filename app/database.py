from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# =========================
# 🔹 1. CRIAR BANCO (se não existir)
# =========================

SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()

# =========================
# 🔹 2. CONECTAR NO BANCO
# =========================

DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

engine = create_engine(
    DATABASE_URL,
    echo=True  # mostra SQL no terminal (ótimo pra debug)
)

# =========================
# 🔹 3. SESSÃO DO BANCO
# =========================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =========================
# 🔹 4. BASE DOS MODELS
# =========================

Base = declarative_base()

# =========================
# 🔹 5. DEPENDÊNCIA (FastAPI)
# =========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
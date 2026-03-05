from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurado para localhost sem senha (root)
URL_BANCO = "mysql+mysqlconnector://root@localhost:3306/studymanager_db"

motor = create_engine(URL_BANCO)
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)
Base = declarative_base()

def obter_db():
    """Gera uma sessão de banco de dados para cada requisição da API."""
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.config.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    # Atualizado para o novo padrão de UTC do Python
    criado_em = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relação 1:N usando strings evita importações circulares
    matriculas = relationship("Matricula", back_populates="usuario", cascade="all, delete-orphan")
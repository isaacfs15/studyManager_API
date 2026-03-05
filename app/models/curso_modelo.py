from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255))
    carga_horaria = Column(Integer, nullable=False)

    matriculas = relationship("Matricula", back_populates="curso", cascade="all, delete-orphan")
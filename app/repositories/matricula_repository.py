from sqlalchemy.orm import Session
from app.models.matricula_modelo import Matricula


class MatriculaRepository:
    """Isola todas as consultas (queries) relacionadas à tabela de Matrículas."""

    @staticmethod
    def buscar_por_usuario_e_curso(db: Session, usuario_id: int, curso_id: int):
        # Usado para validar a regra de "não permitir matrícula duplicada"
        return db.query(Matricula).filter(
            Matricula.usuario_id == usuario_id,
            Matricula.curso_id == curso_id
        ).first()

    @staticmethod
    def salvar(db: Session, matricula: Matricula):
        db.add(matricula)
        db.commit()
        db.refresh(matricula)
        return matricula
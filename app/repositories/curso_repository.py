from sqlalchemy.orm import Session
from app.models.curso_modelo import Curso


class CursoRepository:
    """Isola todas as consultas (queries) relacionadas à tabela de Cursos."""

    @staticmethod
    def buscar_por_id(db: Session, curso_id: int):
        return db.query(Curso).filter(Curso.id == curso_id).first()

    @staticmethod
    def listar_todos(db: Session):
        return db.query(Curso).all()

    @staticmethod
    def salvar(db: Session, curso: Curso):
        db.add(curso)
        db.commit()
        db.refresh(curso)
        return curso

    @staticmethod
    def deletar(db: Session, curso: Curso):
        db.delete(curso)
        db.commit()
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.curso_modelo import Curso
from app.repositories.curso_repository import CursoRepository
from app.schemas.curso_schema import CursoCriar, CursoBase


class CursoService:
    """Gerencia as regras de negócio para Cursos."""

    @staticmethod
    def criar_curso(db: Session, dados: CursoCriar):
        novo_curso = Curso(**dados.model_dump())
        return CursoRepository.salvar(db, novo_curso)

    @staticmethod
    def listar_cursos(db: Session):
        return CursoRepository.listar_todos(db)

    @staticmethod
    def obter_curso(db: Session, curso_id: int):
        curso = CursoRepository.buscar_por_id(db, curso_id)
        if not curso:
            raise HTTPException(status_code=404, detail="Curso não encontrado")
        return curso

    @staticmethod
    def atualizar_curso(db: Session, curso_id: int, dados: CursoBase):
        curso = CursoService.obter_curso(db, curso_id)
        for chave, valor in dados.model_dump().items():
            setattr(curso, chave, valor)
        return CursoRepository.salvar(db, curso)

    @staticmethod
    def deletar_curso(db: Session, curso_id: int):
        curso = CursoService.obter_curso(db, curso_id)
        CursoRepository.deletar(db, curso)
        return True
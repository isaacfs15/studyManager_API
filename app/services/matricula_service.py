from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.matricula_modelo import Matricula
from app.repositories.matricula_repository import MatriculaRepository
from app.repositories.usuario_repository import UsuarioRepository
from app.repositories.curso_repository import CursoRepository
from app.schemas.matricula_schema import MatriculaCriar


class MatriculaService:
    """Gerencia as complexas regras de negócio para Matrículas."""

    @staticmethod
    def realizar_matricula(db: Session, dados: MatriculaCriar):
        # 1. Validar se usuário existe na base
        if not UsuarioRepository.buscar_por_id(db, dados.usuario_id):
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        # 2. Validar se curso existe na base
        if not CursoRepository.buscar_por_id(db, dados.curso_id):
            raise HTTPException(status_code=404, detail="Curso não encontrado")

        # 3. Validar duplicidade (aluno não pode cursar o mesmo curso duas vezes)
        if MatriculaRepository.buscar_por_usuario_e_curso(db, dados.usuario_id, dados.curso_id):
            raise HTTPException(status_code=400, detail="Usuário já matriculado neste curso")

        nova_matricula = Matricula(**dados.model_dump())
        return MatriculaRepository.salvar(db, nova_matricula)
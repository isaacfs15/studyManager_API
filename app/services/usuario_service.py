from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.usuario_modelo import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario_schema import UsuarioCriar, UsuarioBase


class UsuarioService:
    """Gerencia as regras de negócio para Usuários."""

    @staticmethod
    def criar_usuario(db: Session, dados: UsuarioCriar):
        # Regra 1: E-mail deve ser único
        if UsuarioRepository.buscar_por_email(db, dados.email):
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

        # .model_dump() converte o Pydantic em dicionário para o SQLAlchemy
        novo_usuario = Usuario(**dados.model_dump())
        return UsuarioRepository.salvar(db, novo_usuario)

    @staticmethod
    def listar_usuarios(db: Session):
        return UsuarioRepository.listar_todos(db)

    @staticmethod
    def obter_usuario(db: Session, usuario_id: int):
        usuario = UsuarioRepository.buscar_por_id(db, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario

    @staticmethod
    def atualizar_usuario(db: Session, usuario_id: int, dados: UsuarioBase):
        usuario = UsuarioService.obter_usuario(db, usuario_id)  # Valida se existe

        # Regra 2: Verifica se o novo e-mail já pertence a outro usuário
        email_existente = UsuarioRepository.buscar_por_email(db, dados.email)
        if email_existente and email_existente.id != usuario_id:
            raise HTTPException(status_code=400, detail="Este e-mail já está em uso.")

        # Atualiza apenas os campos permitidos
        for chave, valor in dados.model_dump().items():
            setattr(usuario, chave, valor)

        return UsuarioRepository.salvar(db, usuario)

    @staticmethod
    def deletar_usuario(db: Session, usuario_id: int):
        usuario = UsuarioService.obter_usuario(db, usuario_id)
        UsuarioRepository.deletar(db, usuario)
        return True
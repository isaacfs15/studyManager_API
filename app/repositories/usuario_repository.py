from sqlalchemy.orm import Session
from app.models.usuario_modelo import Usuario


class UsuarioRepository:
    """Isola todas as consultas (queries) relacionadas à tabela de Usuários."""

    @staticmethod
    def buscar_por_email(db: Session, email: str):
        return db.query(Usuario).filter(Usuario.email == email).first()

    @staticmethod
    def buscar_por_id(db: Session, usuario_id: int):
        return db.query(Usuario).filter(Usuario.id == usuario_id).first()

    @staticmethod
    def listar_todos(db: Session):
        return db.query(Usuario).all()

    @staticmethod
    def salvar(db: Session, usuario: Usuario):
        db.add(usuario)
        db.commit()
        db.refresh(usuario)  # Atualiza o objeto com o ID gerado pelo banco
        return usuario

    @staticmethod
    def deletar(db: Session, usuario: Usuario):
        db.delete(usuario)
        db.commit()
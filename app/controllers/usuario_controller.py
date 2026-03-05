from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import obter_db
from app.services.usuario_service import UsuarioService
from app.schemas.usuario_schema import UsuarioCriar, UsuarioResposta, UsuarioBase
from app.schemas.resposta_schema import RespostaPadrao

# O prefixo organiza a URL (ex: http://localhost:8000/usuarios)
roteador = APIRouter(prefix="/usuarios", tags=["Usuários"])

@roteador.post("/", status_code=201, response_model=RespostaPadrao)
def criar_usuario(usuario: UsuarioCriar, db: Session = Depends(obter_db)):
    dados_banco = UsuarioService.criar_usuario(db, usuario)
    # Tradução do objeto do banco para JSON do Pydantic
    dados_json = UsuarioResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Usuário criado com sucesso", "data": dados_json}

@roteador.get("/", response_model=RespostaPadrao)
def listar_usuarios(db: Session = Depends(obter_db)):
    dados_banco = UsuarioService.listar_usuarios(db)
    # Traduz uma lista inteira de objetos para JSON
    dados_json = [UsuarioResposta.model_validate(u).model_dump() for u in dados_banco]
    return {"success": True, "message": "Usuários listados com sucesso", "data": dados_json}

@roteador.get("/{usuario_id}", response_model=RespostaPadrao)
def obter_usuario(usuario_id: int, db: Session = Depends(obter_db)):
    dados_banco = UsuarioService.obter_usuario(db, usuario_id)
    dados_json = UsuarioResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Usuário recuperado com sucesso", "data": dados_json}

@roteador.put("/{usuario_id}", response_model=RespostaPadrao)
def atualizar_usuario(usuario_id: int, usuario: UsuarioBase, db: Session = Depends(obter_db)):
    dados_banco = UsuarioService.atualizar_usuario(db, usuario_id, usuario)
    dados_json = UsuarioResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Usuário atualizado com sucesso", "data": dados_json}

@roteador.delete("/{usuario_id}", response_model=RespostaPadrao)
def deletar_usuario(usuario_id: int, db: Session = Depends(obter_db)):
    UsuarioService.deletar_usuario(db, usuario_id)
    return {"success": True, "message": "Usuário deletado com sucesso", "data": None}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import obter_db
from app.services.curso_service import CursoService
from app.schemas.curso_schema import CursoCriar, CursoResposta, CursoBase
from app.schemas.resposta_schema import RespostaPadrao

roteador = APIRouter(prefix="/cursos", tags=["Cursos"])

@roteador.post("/", status_code=201, response_model=RespostaPadrao)
def criar_curso(curso: CursoCriar, db: Session = Depends(obter_db)):
    dados_banco = CursoService.criar_curso(db, curso)
    dados_json = CursoResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Curso criado com sucesso", "data": dados_json}

@roteador.get("/", response_model=RespostaPadrao)
def listar_cursos(db: Session = Depends(obter_db)):
    dados_banco = CursoService.listar_cursos(db)
    dados_json = [CursoResposta.model_validate(c).model_dump() for c in dados_banco]
    return {"success": True, "message": "Cursos listados com sucesso", "data": dados_json}

@roteador.get("/{curso_id}", response_model=RespostaPadrao)
def obter_curso(curso_id: int, db: Session = Depends(obter_db)):
    dados_banco = CursoService.obter_curso(db, curso_id)
    dados_json = CursoResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Curso recuperado com sucesso", "data": dados_json}

@roteador.put("/{curso_id}", response_model=RespostaPadrao)
def atualizar_curso(curso_id: int, curso: CursoBase, db: Session = Depends(obter_db)):
    dados_banco = CursoService.atualizar_curso(db, curso_id, curso)
    dados_json = CursoResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Curso atualizado com sucesso", "data": dados_json}

@roteador.delete("/{curso_id}", response_model=RespostaPadrao)
def deletar_curso(curso_id: int, db: Session = Depends(obter_db)):
    CursoService.deletar_curso(db, curso_id)
    return {"success": True, "message": "Curso deletado com sucesso", "data": None}
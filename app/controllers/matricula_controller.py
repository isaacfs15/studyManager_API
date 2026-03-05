from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import obter_db
from app.services.matricula_service import MatriculaService
from app.schemas.matricula_schema import MatriculaCriar, MatriculaResposta
from app.schemas.resposta_schema import RespostaPadrao

roteador = APIRouter(prefix="/matriculas", tags=["Matrículas"])

@roteador.post("/", status_code=201, response_model=RespostaPadrao)
def criar_matricula(matricula: MatriculaCriar, db: Session = Depends(obter_db)):
    dados_banco = MatriculaService.realizar_matricula(db, matricula)
    dados_json = MatriculaResposta.model_validate(dados_banco).model_dump()
    return {"success": True, "message": "Matrícula realizada com sucesso", "data": dados_json}
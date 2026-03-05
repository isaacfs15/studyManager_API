from pydantic import BaseModel
from datetime import datetime


class MatriculaCriar(BaseModel):
    usuario_id: int
    curso_id: int


class MatriculaResposta(MatriculaCriar):
    id: int
    matriculado_em: datetime

    class Config: from_attributes = True
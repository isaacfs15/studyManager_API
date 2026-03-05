from pydantic import BaseModel

class CursoBase(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int

class CursoCriar(CursoBase):
    pass

class CursoResposta(CursoBase):
    id: int
    class Config: from_attributes = True
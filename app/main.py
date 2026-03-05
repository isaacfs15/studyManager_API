from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import motor, Base
# Importa todos os modelos de uma vez para que o SQLAlchemy consiga criar as tabelas
from app.models import * # Importa os roteadores separados
from app.controllers import usuario_controller, curso_controller, matricula_controller

# Inicializa as tabelas no MySQL
Base.metadata.create_all(bind=motor)

app = FastAPI(title="StudyManager API")

# Permite acesso ao localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tratamento Global de Erros para manter o padrão RespostaPadrao
@app.exception_handler(Exception)
async def tratamento_global_erros(_request: Request, exc: Exception):
    status = getattr(exc, "status_code", 500)
    detalhe = getattr(exc, "detail", "Erro interno no servidor")
    return JSONResponse(
        status_code=status,
        content={"success": False, "message": detalhe, "data": None}
    )

# Registra todos os controladores divididos
app.include_router(usuario_controller.roteador)
app.include_router(curso_controller.roteador)
app.include_router(matricula_controller.roteador)
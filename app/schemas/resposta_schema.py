from pydantic import BaseModel
from typing import Optional, Any

class RespostaPadrao(BaseModel):
    """Padronização rigorosa do JSON de saída."""
    success: bool
    message: str
    data: Optional[Any] = None
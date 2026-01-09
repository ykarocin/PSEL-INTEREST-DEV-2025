from pydantic import BaseModel, Field
from typing import Optional

# Schema para criação de usuário (não inclui id, pois é gerado)
class UserCreate(BaseModel):
    name: str = Field(max_length=100)  # Adiciona validação de comprimento

# Schema para resposta/leitura (inclui id)
class UserRead(BaseModel):
    id: int
    name: str

# Schema para atualização (campos opcionais)
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
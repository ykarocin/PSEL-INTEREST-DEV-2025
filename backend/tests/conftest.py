import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from typing import Generator

from app.core.config import settings
from app.core.db import init_db, get_session as original_get_session
from app.main import app

# Usar SQLite em memória para testes (mais rápido e isolado)
TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

def get_test_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

@pytest.fixture(name="session")
def session_fixture():
    # Criar tabelas
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        init_db(session)  # Se necessário
        yield session
    # Limpar após teste
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session: Session):
    # Sobrescrever a dependência get_session para usar o banco de teste
    app.dependency_overrides[original_get_session] = get_test_session
    with TestClient(app) as client:
        yield client
    # Limpar override após teste
    app.dependency_overrides.clear()
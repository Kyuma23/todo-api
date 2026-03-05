from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
import pytest
from sqlalchemy.pool import StaticPool
from src.db import Tarefa
from src.main import app
from src.routers.todo import get_session

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_criar_tarefa(client: TestClient):
    payload_completo = {
    "titulo": "Dominar o Pytest",
    "descricao": "Escrever testes unitários com SQLModel e motor SQLite em memória",
    "concluida": False
}
    response = client.post("/tarefas/", json=payload_completo)
    
    data = response.json()

    assert response.status_code == 200
    
    assert isinstance(data, dict)
    
    assert data["titulo"] == payload_completo["titulo"]
    assert data["descricao"] == payload_completo["descricao"]
    assert data["concluida"] == payload_completo["concluida"]
    
    assert "id" in data
    assert data["id"] is not None

def test_get_tarefas(client: TestClient):
    response = client.get("/tarefas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
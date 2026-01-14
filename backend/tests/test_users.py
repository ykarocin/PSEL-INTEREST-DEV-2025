from fastapi.testclient import TestClient

def test_create_user(client: TestClient):
    response = client.post("/api/v1/users/", json={"name": "João Silva"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "João Silva"
    assert "id" in data

def test_create_user_without_name(client):
    response = client.post("/api/v1/users/",json={"name": ""})
    assert response.status_code == 400
    assert response.json()["error_code"] == "USER_NAME_REQUIRED"

def test_list_users(client: TestClient):
    # Criar um usuário primeiro
    client.post("/api/v1/users/", json={"name": "Maria"})
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert any(user["name"] == "Maria" for user in data)

def test_get_user(client: TestClient):
    # Criar usuário
    create_response = client.post("/api/v1/users/", json={"name": "Carlos"})
    user_id = create_response.json()["id"]
    
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == "Carlos"

def test_get_user_not_found(client: TestClient):
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "USER_NOT_FOUND"

def test_update_user(client: TestClient):
    # Criar usuário
    create_response = client.post("/api/v1/users/", json={"name": "Ana"})
    user_id = create_response.json()["id"]
    
    # Atualizar
    response = client.put(f"/api/v1/users/{user_id}", json={"name": "Ana Santos"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == "Ana Santos"

def test_update_user_not_found(client: TestClient):
    response = client.put("/api/v1/users/999", json={"name": "Novo Nome"})
    assert response.status_code == 404
    assert response.json()["error_code"] == "USER_NOT_FOUND"

def test_delete_user(client: TestClient):
    # Criar usuário
    create_response = client.post("/api/v1/users/", json={"name": "Pedro"})
    user_id = create_response.json()["id"]
    
    # Deletar
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"
    
    # Verificar se foi deletado
    get_response = client.get(f"/api/v1/users/{user_id}")
    assert get_response.status_code == 404
    assert get_response.json()["error_code"] == "USER_NOT_FOUND"

def test_delete_user_not_found(client: TestClient):
    response = client.delete("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "USER_NOT_FOUND"
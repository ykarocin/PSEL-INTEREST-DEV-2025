from fastapi.testclient import TestClient

def test_create_team(client: TestClient):
    # Criar usuário líder primeiro
    user_response = client.post("/api/v1/users/", json={"name": "João Líder"})
    leader_id = user_response.json()["id"]
    
    response = client.post("/api/v1/teams/", json={"name": "Equipe A", "leader_id": leader_id})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Equipe A"
    assert data["leader_id"] == leader_id

def test_create_team_leader_not_found(client: TestClient):
    response = client.post("/api/v1/teams/", json={"name": "Equipe B", "leader_id": 999})
    assert response.status_code == 404
    assert response.json()["error_code"] == "LEADER_NOT_FOUND"

def test_create_team_leader_belongs_to_a_team(client: TestClient):
    # Criar usuário
    user1 = client.post("/api/v1/users/", json={"name": "User1"}).json()
    
    # Criar primeira equipe
    client.post("/api/v1/teams/", json={"name": "Equipe1", "leader_id": user1["id"]})
    
    # Tentar criar segunda equipe com mesmo líder
    response = client.post("/api/v1/teams/", json={"name": "Equipe2", "leader_id": user1["id"]})
    assert response.status_code == 400
    assert response.json()["error_code"] == "USER_ALREADY_BELONGS_TO_A_TEAM"

def test_list_teams(client: TestClient):
    # Criar usuário e equipe
    user = client.post("/api/v1/users/", json={"name": "Maria"}).json()
    client.post("/api/v1/teams/", json={"name": "Equipe C", "leader_id": user["id"]})
    
    response = client.get("/api/v1/teams/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert any(team["name"] == "Equipe C" for team in data)

def test_get_team(client: TestClient):
    # Criar usuário e equipe
    user = client.post("/api/v1/users/", json={"name": "Carlos"}).json()
    team_response = client.post("/api/v1/teams/", json={"name": "Equipe D", "leader_id": user["id"]})
    team_id = team_response.json()["id"]
    
    response = client.get(f"/api/v1/teams/{team_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == team_id
    assert data["name"] == "Equipe D"
    assert data["leader_id"] == user["id"]

def test_get_team_not_found(client: TestClient):
    response = client.get("/api/v1/teams/999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "TEAM_NOT_FOUND"

def test_update_team(client: TestClient):
    # Criar usuários e equipe
    user1 = client.post("/api/v1/users/", json={"name": "Ana"}).json()
    user2 = client.post("/api/v1/users/", json={"name": "Pedro"}).json()
    team_response = client.post("/api/v1/teams/", json={"name": "Equipe E", "leader_id": user1["id"]})
    team_id = team_response.json()["id"]
    
    # Atualizar nome e líder
    response = client.put(f"/api/v1/teams/{team_id}", json={"name": "Equipe E Updated", "leader_id": user2["id"]})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == team_id
    assert data["name"] == "Equipe E Updated"
    assert data["leader_id"] == user2["id"]

def test_update_team_not_found(client: TestClient):
    response = client.put("/api/v1/teams/999", json={"name": "Novo Nome"})
    assert response.status_code == 404
    assert response.json()["error_code"] == "TEAM_NOT_FOUND"

def test_update_team_leader_not_found(client: TestClient):
    # Criar equipe
    user = client.post("/api/v1/users/", json={"name": "User"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe F", "leader_id": user["id"]}).json()
    
    response = client.put(f"/api/v1/teams/{team['id']}", json={"leader_id": 999})
    assert response.status_code == 404
    assert response.json()["error_code"] == "NEW_LEADER_NOT_FOUND"

def test_update_team_leader_already_leading(client: TestClient):
    # Criar usuários
    user1 = client.post("/api/v1/users/", json={"name": "User1"}).json()
    user2 = client.post("/api/v1/users/", json={"name": "User2"}).json()
    
    # Criar duas equipes
    team1 = client.post("/api/v1/teams/", json={"name": "Equipe1", "leader_id": user1["id"]}).json()
    client.post("/api/v1/teams/", json={"name": "Equipe2", "leader_id": user2["id"]})
    
    # Tentar mudar líder de team1 para user2 (que já lidera team2)
    response = client.put(f"/api/v1/teams/{team1['id']}", json={"leader_id": user2["id"]})
    assert response.status_code == 400
    assert response.json()["error_code"] == "USER_IS_ALREADY_LEADING_ANOTHER_TEAM"

def test_delete_team(client: TestClient):
    # Criar equipe
    user = client.post("/api/v1/users/", json={"name": "User"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe G", "leader_id": user["id"]}).json()
    
    # Deletar
    response = client.delete(f"/api/v1/teams/{team['id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Team deleted successfully"
    
    # Verificar se foi deletada
    get_response = client.get(f"/api/v1/teams/{team['id']}")
    assert get_response.status_code == 404
    assert get_response.json()["error_code"] == "TEAM_NOT_FOUND"

def test_delete_team_not_found(client: TestClient):
    response = client.delete("/api/v1/teams/999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "TEAM_NOT_FOUND"
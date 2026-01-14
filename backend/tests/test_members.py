from fastapi.testclient import TestClient

def test_add_member(client: TestClient):
    # Criar usuário e equipe
    user = client.post("/api/v1/users/", json={"name": "Novo Membro"}).json()
    leader = client.post("/api/v1/users/", json={"name": "Líder"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe Teste", "leader_id": leader["id"]}).json()
    
    response = client.post("/api/v1/members/", json={"team_id": team["id"], "user_id": user["id"]})
    assert response.status_code == 200
    data = response.json()
    assert data["team_id"] == team["id"]
    assert data["user_id"] == user["id"]

def test_add_member_team_not_found(client: TestClient):
    user = client.post("/api/v1/users/", json={"name": "User"}).json()
    response = client.post("/api/v1/members/", json={"team_id": 999, "user_id": user["id"]})
    assert response.status_code == 404
    assert response.json()["error_code"] == "TEAM_NOT_FOUND"

def test_add_member_user_not_found(client: TestClient):
    leader = client.post("/api/v1/users/", json={"name": "Líder"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe", "leader_id": leader["id"]}).json()
    response = client.post("/api/v1/members/", json={"team_id": team["id"], "user_id": 999})
    assert response.status_code == 404
    assert response.json()["error_code"] == "USER_NOT_FOUND"

def test_add_member_user_already_in_team(client: TestClient):
    # Criar usuários e equipes
    user = client.post("/api/v1/users/", json={"name": "User"}).json()
    leader1 = client.post("/api/v1/users/", json={"name": "Líder1"}).json()
    leader2 = client.post("/api/v1/users/", json={"name": "Líder2"}).json()
    team1 = client.post("/api/v1/teams/", json={"name": "Equipe1", "leader_id": leader1["id"]}).json()
    team2 = client.post("/api/v1/teams/", json={"name": "Equipe2", "leader_id": leader2["id"]}).json()
    
    # Adicionar user à team1
    client.post("/api/v1/members/", json={"team_id": team1["id"], "user_id": user["id"]})
    
    # Tentar adicionar à team2
    response = client.post("/api/v1/members/", json={"team_id": team2["id"], "user_id": user["id"]})
    assert response.status_code == 400
    assert response.json()["error_code"] == "USER_ALREADY_BELONGS_TO_A_TEAM"

def test_add_member_user_is_leader(client: TestClient):
    leader = client.post("/api/v1/users/", json={"name": "Líder"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe", "leader_id": leader["id"]}).json()
    
    # Tentar adicionar líder como membro novamente
    response = client.post("/api/v1/members/", json={"team_id": team["id"], "user_id": leader["id"]})
    assert response.status_code == 400
    assert response.json()["error_code"] == "USER_ALREADY_BELONGS_TO_A_TEAM"
    
def test_list_members(client: TestClient):
    # Criar usuário e equipe
    user = client.post("/api/v1/users/", json={"name": "João"}).json()
    leader = client.post("/api/v1/users/", json={"name": "Maria"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Conto", "leader_id": leader["id"]}).json()
    team_id = team["id"]
    
    # Adicionar membro
    client.post("/api/v1/members/", json={"team_id": team_id, "user_id": user["id"]})
    
    response = client.get(f"/api/v1/members/?team_id={team_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["user_id"] == user["id"]
    assert data[1]["user_id"] == leader["id"]
    
def test_list_members_team_not_found(client:TestClient):
    response = client.get("/api/v1/members/?team_id=999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "TEAM_NOT_FOUND"

def test_remove_member(client: TestClient):
    # Criar usuário, equipe e adicionar membro
    user = client.post("/api/v1/users/", json={"name": "Membro"}).json()
    leader = client.post("/api/v1/users/", json={"name": "Líder"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe", "leader_id": leader["id"]}).json()
    client.post("/api/v1/members/", json={"team_id": team["id"], "user_id": user["id"]})
    
    # Remover membro
    response = client.delete(f"/api/v1/members/{team['id']}/{user['id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Member removed successfully"

def test_remove_member_team_not_found(client: TestClient):
    response = client.delete("/api/v1/members/999/1")
    assert response.status_code == 404
    assert response.json()["error_code"] == "TEAM_NOT_FOUND"

def test_remove_member_not_in_team(client: TestClient):
    leader = client.post("/api/v1/users/", json={"name": "Líder"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe", "leader_id": leader["id"]}).json()
    
    response = client.delete(f"/api/v1/members/{team['id']}/{999}")
    assert response.status_code == 404
    assert response.json()["error_code"] == "MEMBER_NOT_FOUND"

def test_remove_member_is_leader(client: TestClient):
    leader = client.post("/api/v1/users/", json={"name": "Líder"}).json()
    team = client.post("/api/v1/teams/", json={"name": "Equipe", "leader_id": leader["id"]}).json()
    
    # Tentar remover líder
    response = client.delete(f"/api/v1/members/{team['id']}/{leader['id']}")
    assert response.status_code == 400
    assert response.json()["error_code"] == "CANNOT_REMOVE_TEAM_LEADER"
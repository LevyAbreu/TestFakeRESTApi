import requests
from config import USERS_ENDPOINT

def test_tc41_list_all_users_success():
    """TC41: Listar todos os Users (GET /Users)"""
    response = requests.get(USERS_ENDPOINT)
    
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), "A resposta deve ser uma lista."
    # Não forçar len(data) > 0, pois o endpoint pode retornar lista vazia.

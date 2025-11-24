import requests
import pytest
from config import USERS_ENDPOINT

NEW_USER_DATA = {
    "id": 101,
    "userName": "user_test_manus",
    "password": "password123"
}

def test_tc43_create_new_user_success():
    """TC43: Criar novo User (POST /Users)"""
    response = requests.post(USERS_ENDPOINT, json=NEW_USER_DATA)
    
    # A API de teste pode retornar 200 ou 201 para criação
    assert response.status_code in [200, 201]
    
    data = response.json()
    assert data["id"] == NEW_USER_DATA["id"]
    assert data["userName"] == NEW_USER_DATA["userName"]
    assert data["password"] == NEW_USER_DATA["password"]

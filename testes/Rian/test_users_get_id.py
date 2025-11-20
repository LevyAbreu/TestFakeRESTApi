import requests
import pytest
from config import USERS_ENDPOINT

EXPECTED_SCHEMA = {
    "id": int,
    "userName": str,
    "password": str
}

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_tc42_get_user_by_id_success(user_id):
    """TC42: Buscar User por ID (GET /Users/{id})"""
    url = f"{USERS_ENDPOINT}/{user_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == user_id
    assert "userName" in data
    assert "password" in data

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_tc45_validate_data_types(user_id):
    """TC45: Validar tipos de dados do retorno (GET /Users/{id})"""
    url = f"{USERS_ENDPOINT}/{user_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    for key, expected_type in EXPECTED_SCHEMA.items():
        assert key in data, f"Campo '{key}' não encontrado."
        assert isinstance(data[key], expected_type), (
            f"Campo '{key}' deveria ser {expected_type}, "
            f"mas veio {type(data[key])}."
        )

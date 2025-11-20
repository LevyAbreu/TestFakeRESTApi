import requests
import pytest
from config import AUTHORS_ENDPOINT

EXPECTED_SCHEMA = {
    "id": int,
    "idBook": int,
    "firstName": str,
    "lastName": str
}

@pytest.mark.parametrize("author_id", [1, 5, 10])
def test_tc32_get_author_by_id_success(author_id):
    """TC32: Buscar Author por ID (GET /Authors/{id})"""
    url = f"{AUTHORS_ENDPOINT}/{author_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == author_id
    assert "idBook" in data
    assert "firstName" in data
    assert "lastName" in data

@pytest.mark.parametrize("author_id", [1, 5, 10])
def test_tc35_validate_data_types(author_id):
    """TC35: Validar tipos de dados do retorno (GET /Authors/{id})"""
    url = f"{AUTHORS_ENDPOINT}/{author_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    for key, expected_type in EXPECTED_SCHEMA.items():
        assert key in data, f"Campo '{key}' não encontrado."
        assert isinstance(data[key], expected_type), (
            f"Campo '{key}' deveria ser {expected_type}, "
            f"mas veio {type(data[key])}."
        )

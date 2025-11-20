import requests
import pytest
from config import USERS_ENDPOINT

USER_TO_DELETE = {
    "id": 999,
    "userName": "user_para_deletar",
    "password": "password_delete"
}

@pytest.fixture(scope="module")
def setup_user_for_deletion():
    """Cria um User antes dos testes e tenta deletá-lo."""
    post_response = requests.post(USERS_ENDPOINT, json=USER_TO_DELETE)
    # A API de teste pode retornar 200 ou 201 para criação
    assert post_response.status_code in [200, 201]
    
    yield USER_TO_DELETE["id"]
    
def test_tc46_delete_user_success(setup_user_for_deletion):
    """TC46: Deletar User por ID (DELETE /Users/{id})"""
    user_id = setup_user_for_deletion
    url = f"{USERS_ENDPOINT}/{user_id}"
    
    delete_response = requests.delete(url)
    
    assert delete_response.status_code == 200
    
    # Tenta buscar para confirmar a deleção (espera-se 404)
    get_response = requests.get(url)
    assert get_response.status_code == 404

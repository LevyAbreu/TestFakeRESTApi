import requests
import pytest
from config import AUTHORS_ENDPOINT

AUTHOR_ID_TO_UPDATE = 1 
UPDATED_FIRST_NAME = "Primeiro Nome Atualizado"

def test_tc34_update_author_success():
    """TC34: Atualizar Author (PUT /Authors/{id})"""
    url = f"{AUTHORS_ENDPOINT}/{AUTHOR_ID_TO_UPDATE}"
    
    get_response = requests.get(url)
    assert get_response.status_code == 200
    author_data = get_response.json()
    
    author_data["firstName"] = UPDATED_FIRST_NAME
    
    put_response = requests.put(url, json=author_data)
    
    assert put_response.status_code == 200
    
    updated_data = put_response.json()
    assert updated_data["firstName"] == UPDATED_FIRST_NAME

import requests
import pytest
from config import USERS_ENDPOINT

USER_ID_TO_UPDATE = 1 
UPDATED_USERNAME = "username_atualizado_manus"

def test_tc44_update_user_success():
    """TC44: Atualizar User (PUT /Users/{id})"""
    url = f"{USERS_ENDPOINT}/{USER_ID_TO_UPDATE}"
    
    get_response = requests.get(url)
    assert get_response.status_code == 200
    user_data = get_response.json()
    
    user_data["userName"] = UPDATED_USERNAME
    
    put_response = requests.put(url, json=user_data)
    
    assert put_response.status_code == 200
    
    updated_data = put_response.json()
    assert updated_data["userName"] == UPDATED_USERNAME

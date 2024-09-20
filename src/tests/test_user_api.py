import pytest
from schema import Schema

@pytest.mark.django_db
def test_user_login(api_client, mock_service_user):
    
    response = api_client.post("/users/login", data={"email": "test@test.com"})

    assert response.status_code == 200
    assert Schema(
        {
            "results": {
                "token": str
            }
        }
    ).validate(response.json())

    mock_service_user.assert_called_once_with(email="test@test.com")
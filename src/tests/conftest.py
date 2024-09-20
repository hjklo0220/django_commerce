from unittest.mock import Mock

import pytest

from tests.utils import APIClient
from user.models import ServiceUser

"""
fixture: 테스트 안에서 반복적으로 사용되는 데이터들을 가져다 쓸수잇게 해두는 object
"""
@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture
def mock_service_user(mocker):
    mock = mocker.patch('user.models.ServiceUser.objects.get')
    mock_user = ServiceUser(email="test@test.com")
    mock.return_value = mock_user
    return mock
import pytest
import requests
import data


@pytest.fixture()
def user_for_test():
    create = requests.post(f'{data.BASE_URL}{data.CREATE_USER_ENDPOINT}', data=data.USER)
    yield create
    token = create.json()["accessToken"]
    requests.delete(f'{data.BASE_URL}{data.DELETE_USER_ENDPOINT}', headers={"Authorization": token})

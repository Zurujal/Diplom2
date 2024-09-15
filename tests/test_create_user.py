import allure
import pytest
import data
import requests


class TestCreateUser:
    @allure.title("Проверка успешного создания пользователя")
    def test_create_user(self, user_for_test):
        assert user_for_test.status_code == 200 and user_for_test.json()["success"] is True

    @allure.title("Проверка невозможности создания уже существующего пользователя")
    def test_unable_create_existed_user(self, user_for_test):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_USER_ENDPOINT}', data=data.USER)
        assert result.status_code == 403 and result.json()["success"] is False

    @allure.title("Проверка невозможности создания пользователя если не заполнены все обязательные поля")
    @pytest.mark.parametrize("user_data", (data.USER_ONLY_NAME, data.USER_ONLY_PASSWORD, data.USER_ONLY_EMAIL))
    def test_unable_create_user_without_required_data(self, user_data):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_USER_ENDPOINT}', data=user_data)
        assert result.status_code == 403 and result.json()["success"] is False

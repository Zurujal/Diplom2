import allure
import pytest
import data
import requests


class TestLoginUser:
    @allure.title("Проверка успешного логина")
    def test_login_user(self, user_for_test):
        result = requests.post(f'{data.BASE_URL}{data.LOGIN_USER_ENDPOINT}', data=data.USER)
        assert result.status_code == 200 and result.json()["success"] is True

    @allure.title("Проверка невозможности логина пользователя с некорректными данными")
    @pytest.mark.parametrize("user_data", (data.USER_ONLY_NAME, data.USER_ONLY_PASSWORD, data.USER_ONLY_EMAIL))
    def test_unable_login_user_with_incorrect_data(self, user_data):
        result = requests.post(f'{data.BASE_URL}{data.LOGIN_USER_ENDPOINT}', data=user_data)
        assert result.status_code == 401 and result.json()["success"] is False

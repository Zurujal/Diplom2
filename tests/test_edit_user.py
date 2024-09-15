import allure
import pytest
import data
import requests


class TestEditUser:
    @allure.title("Проверка возможности изменения данных авторизованного пользователя")
    @pytest.mark.parametrize("edit_data", (data.EDIT_USER_NAME, data.EDIT_USER_PASSWORD, data.EDIT_USER_EMAIL))
    def test_edit_authorized_user(self, user_for_test, edit_data):
        token = user_for_test.json()["accessToken"]
        result = requests.patch(f'{data.BASE_URL}{data.EDIT_USER_ENDPOINT}', data=edit_data,
                                headers={"Authorization": token})
        assert result.status_code == 200 and result.json()["success"] is True

    @allure.title("Проверка невозможности изменения данных не авторизованного пользователя")
    @pytest.mark.parametrize("edit_data", (data.EDIT_USER_NAME, data.EDIT_USER_PASSWORD, data.EDIT_USER_EMAIL))
    def test_unable_edit_unauthorized_user(self, user_for_test, edit_data):
        result = requests.patch(f'{data.BASE_URL}{data.EDIT_USER_ENDPOINT}', data=edit_data)
        assert result.status_code == 401 and result.json()["message"] == data.UNAUTHORIZED_USER_ERROR

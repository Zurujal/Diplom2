import allure
import data
import requests


class TestGetOrder:
    @allure.title("Проверка невозможности получения заказа не авторизованным пользователем")
    def test_get_order_unauthorized_user(self):
        result = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}')
        assert result.status_code == 401 and result.json()["success"] is False

    @allure.title("Проверка успешного получения заказа авторизованным пользователем")
    def test_get_order_authorized_user(self, user_for_test):
        token = user_for_test.json()["accessToken"]
        result = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}', headers={"Authorization": token})
        assert result.status_code == 200 and result.json()["success"] is True

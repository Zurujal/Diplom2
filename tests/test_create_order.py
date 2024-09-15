import allure
import data
import requests


class TestCreateOrder:
    @allure.title("Проверка успешного создания заказа не авторизованным пользователем с ингридиентами")
    def test_create_order_unauthorized_user(self):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}', data=data.ORDER)
        assert result.status_code == 200 and result.json()["success"] is True

    @allure.title("Проверка успешного создания заказа авторизованным пользователем с ингридиентами")
    def test_create_order_authorized_user(self, user_for_test):
        token = user_for_test.json()["accessToken"]
        result = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}', data=data.ORDER,
                               headers={"Authorization": token})
        assert result.status_code == 200 and result.json()["success"] is True

    @allure.title("Проверка невозможности создания заказа без ингридиентов")
    def test_unable_create_order_without_ingredients(self):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}', data=data.ORDER_EMPTY_INGREDIENTS)
        assert result.status_code == 400 and result.json()["success"] is False

    @allure.title("Проверка невозможности создания заказа с некорректным хэшэм ингридиентов")
    def test_unable_create_order_incorrect_ingredients_hash(self):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}',
                               data=data.ORDER_INCORRECT_INGREDIENTS_HASH)
        assert result.status_code == 400 and result.json()["success"] is False

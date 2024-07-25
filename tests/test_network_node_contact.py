from rest_framework import status
from rest_framework.test import APITestCase

from users.services import create_user


class NetworkNodeProductAPITestAPICase(APITestCase):
    """Тестирование продуктов элемента сети"""

    def setUp(self):
        """Установка данных"""

        self.user = create_user()

        response = self.client.post("/users/login/", data={"email": "test.testov@mail.ru", "password": "123qwe456rty"})

        token = response.json()["access"]

        self.header = {"Authorization": f"Bearer {token}"}

        self.network_node_data = {
            "name": "Test node",
            "level": 1,
            "supplier": None,
            "contact": {
                "email": "test.testiv@mail.ru",
                "country": "Russia",
                "city": "Moscow",
                "street": "Victory",
                "house_number": 1,
            },
            "products": [
                {"title": "Test", "model": "Test Model", "on_market": "2015-07-15"},
                {"title": "Test1", "model": "Test Model1", "on_market": "2015-07-16"},
            ],
        }

    def test_network_node_contact(self):
        """Тестирование контакта элемента сети"""

        self.client.post("/nodes/", data=self.network_node_data, format="json", headers=self.header)

        response = self.client.get("/nodes/", headers=self.header)

        network_node_list = response.json()

        network_node = network_node_list[0]

        network_node_pk = network_node["id"]

        contact_pk = network_node["contact"]["id"]

        response = self.client.get(f"/nodes/{network_node_pk}/contact/{contact_pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        contact = response.json()

        self.assertEqual(contact["email"], "test.testiv@mail.ru")
        self.assertEqual(contact["country"], "Russia")
        self.assertEqual(contact["city"], "Moscow")

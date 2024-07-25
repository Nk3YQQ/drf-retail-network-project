from rest_framework import status
from rest_framework.test import APITestCase

from users.services import create_user


class NetworkNodeAPITestAPICase(APITestCase):
    """Тестирование элемента сети"""

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

        self.patch_data = {"name": "Test node2"}

    def test_network_node(self):
        """Тестирование элемента сети"""

        response = self.client.post("/nodes/", data=self.network_node_data, format="json", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get("/nodes/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        network_node_list = response.json()

        self.assertEqual(len(network_node_list), 1)

        network_node = network_node_list[0]

        network_node_pk = network_node["id"]

        response = self.client.get(f"/nodes/{network_node_pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        network_node = response.json()

        self.assertEqual(network_node["name"], "Test node")
        self.assertEqual(network_node["level"], 1)
        self.assertEqual(len(network_node["products"]), 2)

        response = self.client.patch(f"/nodes/{network_node_pk}/", data=self.patch_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        network_node = response.json()

        self.assertEqual(network_node["name"], "Test node2")

        response = self.client.delete(f"/nodes/{network_node_pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

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

        self.product_data = {"title": "Test2", "model": "Test Model2", "on_market": "2015-07-17"}

        self.patch_data = {
            "model": "Test Model3",
        }

    def test_network_node_products(self):
        """Тестирование продуктов элемента сети"""

        self.client.post("/nodes/", data=self.network_node_data, format="json", headers=self.header)

        response = self.client.get("/nodes/", headers=self.header)

        network_node_list = response.json()

        network_node = network_node_list[0]

        network_node_pk = network_node["id"]

        response = self.client.post(
            f"/nodes/{network_node_pk}/products/", data=self.product_data, format="json", headers=self.header
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(f"/nodes/{network_node_pk}/products/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_list = response.json()

        self.assertEqual(len(product_list), 3)

        product = product_list[2]

        product_pk = product["id"]

        response = self.client.get(f"/nodes/{network_node_pk}/products/{product_pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product = response.json()

        self.assertEqual(product["title"], "Test2")
        self.assertEqual(product["model"], "Test Model2")
        self.assertEqual(product["on_market"], "2015-07-17")

        response = self.client.patch(
            f"/nodes/{network_node_pk}/products/{product_pk}/", data=self.patch_data, headers=self.header
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product = response.json()

        self.assertEqual(product["model"], "Test Model3")

        response = self.client.delete(f"/nodes/{network_node_pk}/products/{product_pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

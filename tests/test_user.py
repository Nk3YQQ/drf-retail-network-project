from rest_framework import status
from rest_framework.test import APITestCase


class UserAPITestCase(APITestCase):
    """Тестирование пользователей"""

    def setUp(self):
        self.registration_data = {
            "first_name": "Test",
            "last_name": "Testov",
            "email": "test.testov@mail.ru",
            "password": "123qwe456rty",
            "passwordConfirm": "123qwe456rty",
        }

        self.login_data = {"email": "test.testov@mail.ru", "password": "123qwe456rty"}

    def test_users(self):
        """Тестирование пользователей"""

        response = self.client.post("/users/registration/", data=self.registration_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/users/login/", data=self.login_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.json()["access"]

        header = {"Authorization": f"Bearer {token}"}

        response = self.client.get("/users/profile/", headers=header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = response.json()

        self.assertEqual(user["first_name"], "Test")
        self.assertEqual(user["last_name"], "Testov")
        self.assertEqual(user["email"], "test.testov@mail.ru")

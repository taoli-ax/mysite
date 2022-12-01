from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


# Create your tests here.

class AccountTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        # 自定义创建用户方法
        self.user = self.create_user(
            username='admin001',
            email='admin001@gmail.com',
            password='correct password',
        )

    def create_user(self, username, password, email):
        return User.objects.create_user(username, password, email)

    def test_login(self):
        LOGIN_URL = '/accounts/login/'

        response = self.client.post(LOGIN_URL, {
            'username': self.user.username,
            'password': 'wrong password',
        })
        self.assertNotEqual(response.status_code, 302)
        #
        INDEX_PAGE = ''
        response = self.client.get(INDEX_PAGE)
        self.assertNotEqual(response.status_code,200)

        response = self.client.post(LOGIN_URL, {
            'username': self.user.username,
            'password': 'correct password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response, None)


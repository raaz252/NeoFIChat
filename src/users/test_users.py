# tests/test_users.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import MyUser
from rest_framework.authtoken.models import Token

class UserTests(APITestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
    def test_get_user_list(self):
        # Create some test users
        user1 = MyUser.objects.create(username="user1", is_active=True)
        user2 = MyUser.objects.create(username="user2", is_active=True)
        user3 = MyUser.objects.create(username="user3", is_active=False)

        url = reverse('user_list')  # Assuming you've named your URL pattern 'user_list'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user1.username)
        self.assertContains(response, user2.username)
        self.assertNotContains(response, user3.username)

# Add similar test cases for other views and API endpoints.

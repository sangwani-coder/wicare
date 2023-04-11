from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from knox.models import AuthToken
from django.contrib.auth.models import User


class RegisterSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        }
        self.serializer = RegisterSerializer(data=self.user_data)
    
    def test_serializer_validation(self):
        """
        Test that serializer validates data correctly.
        """
        self.assertTrue(self.serializer.is_valid())
        
    def test_serializer_save(self):
        """
        Test that serializer creates a user instance correctly.
        """
        self.serializer.is_valid()
        user = self.serializer.save()
        
        # Ensure that the user instance was created correctly
        self.assertIsInstance(user, get_user_model())
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])


class RegisterAPITest(APITestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        }
        self.serializer = RegisterSerializer(data=self.user_data)
    
    def test_create_user(self):
        """
        Test that a new user can be created.
        """
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        
        # Verify that the user instance was created correctly
        user_id = AuthToken.objects.get(user_id=1).user_id
        print(user_id)
        user = User.objects.get(id=user_id)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])

class LoginAPITest(APITestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.user_data)
    
    def test_login_user(self):
        """
        Test that a user can be logged in.
        """
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        
        # # Verify that the token was created and is associated with the user
        token = AuthToken.objects.get(user_id=1)
        self.assertEqual(token.user, self.user)


# class LogoutAPITestCase(APITestCase):
#     client = APIClient()

#     def setUp(self):
#         self.user = User.objects.create_user(
#             username="testuser", password="testpass123"
#         )
#         self.token = AuthToken.objects.create(user=self.user)
#         print(str(self.token[0]))
#         self.headers = {"Authorization": f"Token {str(self.token[0])}"}

#     def test_logout_valid_user(self):
#         url = "/api/logout/"
#         response = self.client.post(url, **self.headers)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         # Check that the token is invalidated and no longer exists
#         self.assertFalse(AuthToken.objects.filter(key=str(self.token[0])).exists())

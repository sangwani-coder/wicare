from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from knox.models import AuthToken
from django.contrib.auth.models import User


class AuthenticationTest(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.logout_all_url = reverse('logoutall')

    def test_register(self):
        """
        Test that the register reverse URL is correct.
        """
        self.assertEqual(self.register_url, "/api/auth/register/")

    def test_login(self):
        """
        Test that the login reverse URL is correct.
        """
        self.assertEqual(self.login_url, "/api/auth/login/")

    def test_logout(self):
        """
        Test that the logout reverse URL is correct.
        """
        self.assertEqual(self.logout_url, "/api/auth/logout/")

    def test_logout_all(self):
        """
        Test that the logoutall reverse URL is correct.
        """
        self.assertEqual(self.logout_all_url, "/api/auth/logoutall/")

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


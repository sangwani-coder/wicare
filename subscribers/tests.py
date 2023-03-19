from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from subscribers.models import Subscribers
from django.test import Client
from django.contrib.auth.models import User

class SubscribersTest(APITestCase):
   def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='sangwani', email='pit@i.com', password='test')
        self.client.login(username="sangwani", password="test")
        
   def test_post_subscribers(self):
      """
      Ensure we can create a new dubscriber.
      """
      url = reverse('subscribers-list')
      data = {
         'firstname':'mule',
         'lastname':'mwamba',
        'location':'Lusaka',
        'mobile':'096553262',
        'email':'email@example.com',
        'owner': self.user.username
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Subscribers.objects.count(), 1)
      self.assertEqual(Subscribers.objects.get().firstname, 'mule')
      
   def test_get_subscribers(self):
      """
      Ensure we can get an object.
      """
      url = reverse('subscribers-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
  
   
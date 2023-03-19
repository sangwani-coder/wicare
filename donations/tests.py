from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from donations.models import Donations
from django.test import Client
from django.contrib.auth.models import User

class DonationsTest(APITestCase):
   def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='pita', email='pit@i.com', password='test')
        self.client.login(username="pita", password="test")
        
   def test_post_donations_education(self):
      """
      Ensure we can create a new donation to education.
      """
      url = reverse('donations-list')
      data = {
         'sponsor':'zyambo',
         'amount':250,
        'donate_to':'Education',
        'mobile':'096553262',
        'email':'email@example.com'
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Donations.objects.count(), 1)
      self.assertEqual(Donations.objects.get().sponsor, 'zyambo')
    
   def test_post_donations_health(self):
      """
      Ensure we can create a new donation to health.
      """
      url = reverse('donations-list')
      data = {
         'sponsor':'sangwani',
         'amount':250,
        'donate_to':'Health',
        'mobile':'096553262',
        'email':'email@example.com'
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Donations.objects.count(), 1)
      self.assertEqual(Donations.objects.get().sponsor, 'sangwani')
      
   def test_get_donations(self):
      """
      Ensure we can get an object.
      """
      url = reverse('donations-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
  
   
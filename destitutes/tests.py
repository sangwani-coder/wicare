from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from destitutes.models import Education as Education
from django.test import Client
from django.contrib.auth.models import User

class EducationTest(APITestCase):
   def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='pita', email='pit@i.com', password='test')

   def test_post_education(self):
      """
      Ensure we can create a new post
      """
      self.client.login(username="pita", password="test")
      url = reverse('education-list')
      data = {
         'volunteer':'zyambo',
         'familyname':'sangwani',
        'shortstory':'Lack of shoes',
        'problemdescription':'pita is an orphan in grade 5',
        'monthlybudget':89
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Education.objects.count(), 1)
      self.assertEqual(Education.objects.get().volunteer, 'pita')
      
   def test_get_education(self):
      """
      Ensure we can get an object.
      """
      url = reverse('education-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
  
from destitutes.models import Health as Health

class HealthTest(APITestCase):
   def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='pita', email='pit@i.com', password='test')
        self.client.login(username="pita", password="test")
        
   def test_post_health(self):
      """
      Ensure we can create a new post
      """
      url = reverse('health-list')
      data = {
         'patientsnames':'baby walu',
         'patientsage': 4,
         'hospital': 'KTH',
         'medicalcondition':'unknown',
         'requiredfunds':3600,
         'requiredtreatment': "hepatitis B",
         'urgent': True
      }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Health.objects.count(), 1)
      self.assertEqual(Health.objects.get().patientsnames, 'baby walu')
      
   def test_get_health(self):
      """
      Ensure we can get an object.
      """
      url = reverse('health-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
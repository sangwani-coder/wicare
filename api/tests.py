from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Donee
from .serializers import DoneeSerializer
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class DoneeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com',
            password='testpass'
        )
        self.donee = Donee.objects.create(
            user=self.user, 
            full_name='Test Donee', 
            location='Test Location', 
            need='Test need', 
            bio='Test bio'
        )

    def test_donee_model(self):
        self.assertEqual(
            str(self.donee), "Test Donee, Test Location, Test need")


class DoneeSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com',
            password='testpass'
        )
        self.donee_data = {
            'user': self.user,
            'full_name': 'Lusaka Family',
            'location': 'Test location',
            'need': 'Tuition fees',
            'bio': 'I need help paying my tuition fees'
        }
        self.serializer = DoneeSerializer(data=self.donee_data)

    def test_valid_data(self):
        self.assertTrue(self.serializer.is_valid())

    def test_invalid_data(self):
        self.donee_data['full_name'] = ''
        serializer = DoneeSerializer(data=self.donee_data)
        self.assertFalse(serializer.is_valid())


class DoneeListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_donees(self):
        Donee.objects.create(
            full_name='Donee 1', need='Need 1', user=self.user)
        Donee.objects.create(
            full_name='Donee 2', need='Need 2', user=self.user)
        response = self.client.get(reverse('donee_list'))
        donees = Donee.objects.all()
        serializer = DoneeSerializer(donees, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], donees.count())
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.data['results'][0]['full_name'], 'Donee 1')
        self.assertEqual(response.data['results'][0]['need'], 'Need 1')


class DoneeDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.donee = Donee.objects.create(
            full_name='Donee 1', need='Need 1', user=self.user,
            bio='', location=''
            )

    def test_retrieve_donee(self):
        response = self.client.get(
            reverse('donee_detail', kwargs={'pk': self.donee.pk}))
        serializer = DoneeSerializer(self.donee)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class DoneeRetrieveUpdateDestroyAPIView(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        Donee.objects.create(
            user=self.user, full_name='Test Donee',
            location='Test Location', bio='Test Bio'
            )

    def test_get_donee_detail(self):
        donee = Donee.objects.first()
        response = self.client.get(
            reverse('donee_detail', kwargs={'pk': donee.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, DoneeSerializer(donee).data)

    def test_update_donee_detail(self):
        donee = Donee.objects.first()
        data = {
            'full_name': 'New Name',
            'location': 'New Location',
            'bio': 'New Bio',
            'need':'New need'
            }
        response = self.client.put(
            reverse('donee_detail', kwargs={'pk': donee.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        donee.refresh_from_db()
        self.assertEqual(donee.full_name, data['full_name'])
        self.assertEqual(donee.location, data['location'])
        self.assertEqual(donee.bio, data['bio'])

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Donee, Donation, get_default_donee
from .serializers import DoneeSerializer
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .choices import ModelChoices

class DoneeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com',
            password='testpass'
        )
        self.location = ModelChoices.ZAMBIAN_PROVINCE_CHOICES[1]
        self.donee = Donee.objects.create(
            user=self.user, 
            full_name='Test Donee', 
            location=self.location,
            need='Test need', 
            bio='Test bio'
        )

    def test_donee_model(self):
        self.assertEqual(
            str(self.donee), "Test Donee, Central Province, Test need")


class DoneeSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com',
            password='testpass'
        )
        self.donee_data = {
            'user': self.user,
            'full_name': 'Lusaka Family',
            'location': '',
            'need': 'Tuition fees',
            'bio': 'I need help paying my tuition fees',
            'image':''
        }
        self.serializer = DoneeSerializer(data=self.donee_data)

    def test_valid_data(self):
        self.assertTrue(self.serializer.is_valid())

    def test_invalid_data(self):
        self.donee_data['full_name'] = ''
        serializer = DoneeSerializer(data=self.donee_data)
        self.assertFalse(serializer.is_valid())


class DoneeListCreateTestCase(TestCase):
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
            bio='', location='', image='',
            )

    def test_retrieve_donee(self):
        response = self.client.get(
            reverse('donee_detail', kwargs={'pk': self.donee.pk}))
        serializer = DoneeSerializer(self.donee)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class DoneeRetrieveUpdateDestroyTestCase(APITestCase):
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
            location='', need="test need", bio='Test Bio', image='',
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
            'location': '',
            'bio': 'New Bio',
            'need':'New need',
            'image':''
            }
        response = self.client.put(
            reverse('donee_detail', kwargs={'pk': donee.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        donee.refresh_from_db()
        self.assertEqual(donee.full_name, data['full_name'])
        self.assertEqual(donee.bio, data['bio'])

    def test_delete_donee_detail(self):
        donee = Donee.objects.first()
        response = self.client.delete(
            reverse('donee_detail', kwargs={'pk': donee.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DoneeCreateTestCase(APITestCase):
    """
    Test that a Donee can be created with a POST request
    to the donne_list endpoint.
    """
    client = APIClient()
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        
        self.donee_url = reverse('donee_list')
        
        self.user_data = {
            'full_name': 'New Name',
            'location': '',
            'bio': 'New Bio',
            'need':'New need',
            'image':''
        }
    
    def test_create_donee(self):
        """
        Test that a new donee can be created.
        """
        response = self.client.post(
            self.donee_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('full_name', response.data)
        
        # Verify that the user instance was created correctly
        donee = Donee.objects.get(id=1)
        self.assertEqual(donee.full_name, self.user_data['full_name'])
        self.assertEqual(donee.need, self.user_data['need'])


class DonationTestCase(APITestCase):
    """
    Test that donations can be viewed,
    and a new donation can be created.
    """
    client = APIClient()

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.donee = Donee.objects.create(
            user=self.user, full_name='Test Donee',
            location='Test Location', need="test need", bio='Test Bio'
            )

        self.donation_url = reverse('donation')

    def test_get_donation(self):
        Donation.objects.create(
            donee=self.donee,
            donor_full_names='donor names',
            location='Kitwe',
            amount=50,
            comment='Glad to help',
            account_number= '0987537829290'
        )
        response = self.client.get(self.donation_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # verify that a donation was created to the
        # right donee
        donation = Donation.objects.first()
        self.assertEqual(donation.donee.full_name, 'Test Donee')
        self.assertEqual(donation.comment, 'Glad to help')
        # verify that the donation was added to the right user
        self.assertEqual(donation.donee.user.username, 'testuser')

    def test_create_donation(self):
        donee = Donee.objects.first()
        donor_data = {
            'donee': donee.id,
            'donor_full_names':'donor names',
            'location':'Kitwe',
            'amount':50,
            'comment':'Glad to help',
            'account_number':'0987537829290'
        }
        response = self.client.post(self.donation_url, donor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # verify that a donation was created to the
        # right donee
        donation = Donation.objects.first()
        self.assertEqual(donation.donee.full_name, 'Test Donee')
        self.assertEqual(donation.comment, 'Glad to help')
        # verify that the donation was added to the right user
        self.assertEqual(donation.donee.user.username, 'testuser')

    def test_donation_invalid_methods(self):
        donee = Donee.objects.first()
        donor_data = {
            'donee': donee.id,
            'donor_full_names':'donor names',
            'location':'Kitwe',
            'amount':50,
            'comment':'Glad to help',
            'account_number':'0987537829290'
        }
        response = self.client.put(self.donation_url, donor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_default_donee(self):
        """
        test that a default donee object is created.
        """
        donee = get_default_donee()
        self.assertEqual(donee.user.username, 'testuser')
        self.assertEqual(donee.full_name, 'wicare-general')
        self.assertEqual(donee.need, 'Help the needy in society')


    def test_create_default_donation(self):
        """
        Test that a default donee is given the donation
        If not explicitly selected by donor
        """
        donor_data = {
            'donor_full_names':'donor names',
            'location':'Kitwe',
            'amount':50,
            'comment':'Glad to help',
            'account_number':'0987537829290'
        }
        response = self.client.post(self.donation_url, donor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # verify that a donation was created to the
        # right donee
        donation = Donation.objects.first()
        self.assertEqual(donation.donee.full_name, 'wicare-general')
        self.assertEqual(donation.comment, 'Glad to help')
        # verify that the donation was added to the right user
        self.assertEqual(donation.donee.user.username, 'testuser')
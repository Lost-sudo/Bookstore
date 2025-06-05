from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.

class AccountsAPITestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.token_url = reverse('token_obtain_pair')
        self.profile_url = reverse('profile')
        self.user_data = {
            'email': 'test@example.com',
            'full_name': 'Test User',
            'phone_number': '1234567890',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        self.user = User.objects.create_user(
            email="existing@example.com",
            full_name="Existing User",
            phone_number="1234567890",
            password="existingpassword"
        )

    def test_register_success(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)

    def test_register_duplicate_email(self):
        data = self.user_data.copy()
        data['email'] = 'existing@example.com'
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_register_password_mismatch(self):
        data = self.user_data.copy()
        data['password2'] = 'differentpassword'
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_login_success(self):
        response = self.client.post(self.token_url, 
        {
            'email': 'existing@example.com', 'password': 'existingpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.token_url, {
            'email': 'existing@example.com', 'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_profile_unauthorized(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_view_and_update(self):
        self.client.post(self.register_url, self.user_data)
        login = self.client.post(self.token_url, {
            'email': 'test@example.com', 'password': 'testpassword'
        })
        token = login.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        profile_data = {
            'shipping_address': '123 Test St',
            'payment_card': '1234 5678 9012 3456'
        }
        response1 = self.client.post(self.profile_url, profile_data)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

        response2 = self.client.get(self.profile_url)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data['shipping_address'], profile_data['shipping_address'])

        update_data = {
            'shipping_address': '456 New St'
        }
        response3 = self.client.put(self.profile_url, update_data)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.data['shipping_address'], update_data['shipping_address'])

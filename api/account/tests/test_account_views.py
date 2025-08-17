#imports
from model_bakery import baker
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

#consts
USER = get_user_model()

#tests

class RegisterViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('account:register')
        self.data = {
            'name': 'Test User',
            'username': 'testuser',
            'email': 'test@exemple.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword',
            'image': '',
        }
        
    def tearDown(self):
        USER.objects.all().delete()
        
    def test_if_register_view_creates_user(self):
        result = self.client.post(self.url, self.data)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(USER.objects.all().count(),1)
        
    def test_if_register_view_does_not_create_user_with_different_passwords(self):
        self.data['confirm_password'] = 'differentpassword'
        result = self.client.post(self.url, self.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(USER.objects.all().count(),0)
        
    def test_if_register_view_does_not_create_user_with_existing_username(self):
        baker.make(USER, username='testuser')
        result = self.client.post(self.url, self.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(USER.objects.all().count(),1)
        
    def test_if_view_does_not_create_user_with_existing_email(self):
        baker.make(USER,email=self.data.get('email'))
        result = self.client.post(self.url, self.data)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(USER.objects.all().count(),1)
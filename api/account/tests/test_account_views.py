#imports
from model_bakery import baker
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

#consts
USER = get_user_model()

USER_TEST_DATA = {
    'name': 'Test User',
    'username': 'testuser',
    'email': 'test@exemple.com',
    'password': 'testpassword',
    'image': '',
}

#func
def create_test_user(data:dict):
    password = data.pop('password')
    user = USER(**data)
    user.set_password(password)
    user.save()

#tests

class RegisterViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('account:register')
        self.data = USER_TEST_DATA.copy()
        self.data['confirm_password'] = 'testpassword',
        
        
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
        
    def test_if_register_view_returns_register_message(self):
        result = self.client.post(self.url,self.data)
        expected_message = 'Created successfully'
        self.assertEqual(result.data.get('message'), expected_message)
        
    def test_if_view_returns_authentication_tokens(self):
        response = self.client.post(self.url,self.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
    def test_if_view_set_tokens(self):
        response = self.client.post(self.url,self.data)
        self.assertIn('access', response.cookies)
        self.assertIn('refresh', response.cookies)
        
class LoginViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('account:login')
        self.data = {
            "username": "testuser",
            "password": "testpassword",
        }
        
        
        create_test_user(USER_TEST_DATA.copy())
        
    
    def tearDown(self):
        USER.objects.all().delete()
        
    def test_if_view_is_returned_login_message(self):
        response = self.client.post(self.url,self.data)
        expected_message = 'Login successful'
        self.assertEqual(response.data.get('message'), expected_message)
        
    def test_if_view_returns_authentication_tokens(self):
        response = self.client.post(self.url,self.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
    def test_if_view_set_tokens(self):
        response = self.client.post(self.url,self.data)
        self.assertIn('access', response.cookies)
        self.assertIn('refresh', response.cookies)
from re import L
from this import d
from django.test import TestCase , SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageView(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

class SignupPagesTests(TestCase):
    username = 'newuser'
    email =  'newuser@email.com'

    def test_signup_page_status_code(self):
        response =  self.client.get('/users/signup/')
        self.assertEqual(response.status_code,200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response =  self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

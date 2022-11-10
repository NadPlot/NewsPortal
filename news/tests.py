from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Author, Post


class AuthorTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
                username='name',
                email='email@email.ru',
                password='test123'
        )
        
        def test_create_author(self):
            author = Author.objects.create(user=self.user)
            self.assertEqual(author.user.username, 'name')
            self.assertEqual(author.user.email, 'email@email.ru')
            self.assertTrue(author.user.is_active)


class HomepageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


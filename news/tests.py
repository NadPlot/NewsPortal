from django.contrib.auth import get_user_model
from django.test import TestCase
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


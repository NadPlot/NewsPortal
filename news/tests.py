from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import Author, Post
from .views import HomePageView, AboutPageView


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

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Some text')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
                view.func.__name__,
                HomePageView.as_view().__name__
        )

class AboutPagesTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'News Portal')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Some text')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
                view.func.__name__,
                AboutPageView.as_view().__name__
        )


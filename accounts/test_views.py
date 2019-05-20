from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .views import index, login, logout, register
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.core.urlresolvers import reverse

class TestViews(TestCase):
    def test_get_profile_page(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    def test_get_register_page(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed('register.html')
    
    def test_can_register_new_user_object(self):
        response = self.client.post('/accounts/register/', {'username': 'testuser999',
                                                            'email': 'testuser999@test.com',
                                                            'password1': 'Helloworld',
                                                            'password2': 'Helloworld'})
        user = get_object_or_404(User, username="testuser999")

        self.assertEqual(str(user), "testuser999")
        self.assertEqual(response.status_code, 302)
    
    def test_same_username_can_not_be_reused(self):
        self.user = User.objects.create_user(username='testuser999',
                                             email='testuser999@test.com',
                                             password='Helloworld')
        self.user.save()

        response = self.client.post('/accounts/register/', {'username': 'testuser999',
                                                            'email': 'testuser999@test.com',
                                                            'password1': 'Helloworld',
                                                            'password2': 'Helloworld'})

        self.assertIn('A user with that username already exists.',
                      str(response.content))    
    
    def test_get_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')
    
    def test_can_login_with_user_credentials(self):
        # use create_user so that the password is properly hashed
        self.user = User.objects.create_user(username='testuser999',
                                             email='testuser999@test.com',
                                             password='Helloworld')
        self.user.save()
        response = self.client.get('/')
        response2 = self.client.post('/accounts/login/', {'username': self.user.username,
                                                          'password': 'Helloworld'})
        self.assertEqual(response2.status_code, 200)
    
    def test_logout_successfully(self):
        user = UserRegistrationForm({"username":"Ben", "email":"ben@ben.com", "password1":"cornbob", "password2":"cornbob"})
        user.save()
        
        login_successful = self.client.login(username="Ben", password="cornbob")
        self.assertTrue(login_successful)
        
        page = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')
    
    
    
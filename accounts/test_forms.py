from django.test import TestCase
from .views import UserLoginForm, UserRegistrationForm

class TestAccountItemForm(TestCase):
    
    def test_validation_error_for_a_blank_password(self):
        form = UserRegistrationForm({'email':'jim@bob.com', 'username': 'johnboy32', 'password1':'', 'password2': 'mypassword123'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
    
    def test_validation_error_for_non_matching_passwords(self):
        form = UserRegistrationForm({'email':'jim@bob.com', 'username': 'johnboy32', 'password1' : 'newpassword', 'password2': 'mypassword123'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords do not match'])    
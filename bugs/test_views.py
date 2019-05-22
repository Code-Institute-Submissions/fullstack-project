from django.test import TestCase
from .models import Bug, BugComment
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    
    def test_get_bugs_page(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
        
    def test_add_bug_page(self):
        page = self.client.get("/bugs/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_bug.html")   
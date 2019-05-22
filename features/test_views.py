from django.test import TestCase
from .models import Feature, FeatureComment
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    
    def test_get_bugs_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
        
    def test_add_bug_page(self):
        page = self.client.get("/features/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_feature.html")   
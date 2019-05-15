from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Product

class TestViews(TestCase):
    
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
from django.test import TestCase
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()
class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    def test_get_cart_page(self):
        """
        Test to see if correct page is returned when viewing cart
        """
        page = self.client.get("/shopping_cart/view_cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_cart.html")
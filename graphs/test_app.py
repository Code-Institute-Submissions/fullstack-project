from django.apps import apps
from django.test import TestCase
from .apps import GraphsConfig

class TestGraphsConfig(TestCase):
    
    def test_app(self):
        self.assertEqual("graphs", GraphsConfig.name)
        self.assertEqual("graphs", apps.get_app_config("graphs").name)
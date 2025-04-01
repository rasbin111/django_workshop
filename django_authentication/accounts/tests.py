import json
from datetime import time
from django.test import TestCase, Client

from django.contrib.auth import get_user, get_user_model
from django.urls import reverse
from django.utils import timezone

from .views import LoginView

User = get_user_model()


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.user = User.objects.create_user(
                email="rgt@email.com", 
                password="adminadminadmin",
                )
        

    def test_login(self):
        
        email="rgt@email.com"
        password="adminadminadmin"

        response = self.client.post(reverse("account:login"), 
                                content_type="application/json",
                                data = json.dumps({
                                    "email": email,
                                    "password": password
                                    })
                                 )

        jsonData = response.json()
        self.assertIn("access", jsonData, "Token generation failed")




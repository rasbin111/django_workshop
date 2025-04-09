import json
from django.test import TestCase

from django.contrib.auth import get_user_model
from graphene_django.utils.testing import GraphQLTestCase


User = get_user_model()

class LoginTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/graphql/"

    def setUp(self):
        u1 = User.objects.create(
            username="admin",
            email="admin@admin.com",
            is_superuser=True
        )    
        u1.set_password("admin") 
        u1.save()   
    
    def test_login(self):
        response = self.query(
            '''
            mutation login{
                login(username:"admin", password: "admin"){
                    ok
                    token
                }
            }

            '''
        )
        
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)["data"]["login"]
        self.assertTrue(content["ok"])
        self.assertIsNotNone(content["token"])
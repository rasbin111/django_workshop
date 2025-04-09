import json
from django.test import TestCase

from django.contrib.auth import get_user_model
from graphene_django.utils.testing import GraphQLTestCase
from graphql_jwt.shortcuts import get_token

User = get_user_model()

class AuthenticationTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/graphql/"

    def setUp(self):
        self.u1 = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="admin"
        )    
        self.token = get_token(self.u1)
        
    def auth_headers(self):
        return {"AUTHORIZATION": f"BEARER {self.token}"}

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
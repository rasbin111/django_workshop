import json 
from django.contrib.auth import get_user_model
from graphene_django.utils.testing import GraphQLTestCase

from .models import Post

User = get_user_model()

class TestPostView(GraphQLTestCase):
    GRAPHQL_URL = "/graphql/"

    def setUp(self):
        self.user1 = User.objects.create(name="test1", email="test1@test.com", password="admin")
        self.post1 = Post.objects.create(
            owner=self.user1,
            title="Test Title 1",
            content="Test Title 1 Descrtiption",
            published=True,
        )

    def test_post_list_view(self):
        response = self.query(
            '''
            query posts{
                allPosts{    
                    title
                    content
                }
            }
            '''
        )

        self.assertResponseNoErrors(response)
        content = json.loads(response.content)

        self.assertEqual(len(content["data"]["allPosts"]), 1)
import json 
from django.contrib.auth import get_user_model
from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from .models import Post

User = get_user_model()


class TestPostModel(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            name="test1", email="test1@test.com", password="admin"
        )
        self.p1 = Post.objects.create(
            title = "test 1",
            content = "test 1 content",
            published= True,
            owner=self.user1
        )

        self.p2 = Post.objects.create(
            title = "test 2",
            content = "test 2 content",
            published= True,
            owner=self.user1
        )

        self.p3 = Post.objects.create(
            title = "test 3",
            content = "test 3 content",
            published= True,
            owner=self.user1
        )

    def test_all_post_retreival(self):
        posts = Post.objects.all()
        self.assertEqual(len(posts), 3)
    
    def test_create_post(self):
        self.p4 = Post.objects.create(
            title = "test 4",
            content = "test 4 content",
            published= True,
            owner=self.user1
        )
        self.assertEqual(self.p4.title, "test 4")

        
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
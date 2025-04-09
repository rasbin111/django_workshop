import json
from django.test import TestCase

from django.contrib.auth import get_user_model
from graphene_django.utils.testing import GraphQLTestCase

from course.models import Course, Creator

User = get_user_model()

class CoursesListTestCase(GraphQLTestCase):    
    GRAPHQL_URL = "/graphql/"

    def setUp(self):
        c1 = Creator.objects.create(
            name="rgt", 
            info="I dont know much", 
            email="rgt@gmail.com"
        )
        Course.objects.create(
            title="Python in English",
            description="A very boring creator generated an amazing lang",
            price=100,
            currency="NPR",
            creator = c1
        )

        Course.objects.create(
            title="Python in Nepali",
            description="A very boring creator generated an amazing lang",
            price=100,
            currency="NPR",
            creator = c1
        )

    def test_course_list(self):
        response = self.query(
            '''
            query courses{
                courses{
                    id
                    title
                    description  
                }
            }
            '''        )
        content = json.loads(response.content)
        courses = content["data"]["courses"]
        self.assertEqual(len(courses), 2, "len equal to two")
        self.assertResponseNoErrors(response)
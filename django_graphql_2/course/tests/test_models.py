from django.test import TestCase

from course.models import Course, Creator

class CreatorTestCase(TestCase):

    def setUp(self):
        Creator.objects.create(name="rgt", 
                info="I dont know much", 
                email="rgt@gmail.com")
        Creator.objects.create(name="susmita", 
            info="She is good", 
            email="susmitey@gmail.com")

    def test_creator_info(self):
        rgt = Creator.objects.get(name="rgt")
        susmitey = Creator.objects.get(name="susmita")

        self.assertEqual(rgt.email, "rgt@gmail.com")
        self.assertEqual(susmitey.email, "susmitey@gmail.com")


class CourseTestCase(TestCase):

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
    
    def test_course_info(self):
        course1 = Course.objects.get(title="Python in Nepali")
        creator1 = Creator.objects.get(name="rgt")

        self.assertEqual(course1.title, "Python in Nepali")
        self.assertEqual(course1.price, 100)
        self.assertEqual(course1.creator, creator1)
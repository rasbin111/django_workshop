import graphene
from graphene_django import DjangoObjectType

from .models import Course, Creator


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class CreatorType(DjangoObjectType):
    class Meta:
        model = Creator


class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)
    all_creators = graphene.List(CreatorType)
    creator_by_name = graphene.Field(CreatorType, name=graphene.String(required=True))

    def resolve_all_courses(root, info):
        return Course.objects.all()

    def resolve_all_creators(root, info):
        return Creator.objects.all()

    def resolve_creator_by_name(root, info, name):
        try:
            return Creator.objects.get(name=name)
        except Creator.DoesNotExist:
            return None


class CreatorMutation(graphene.Mutation):
    creator = graphene.Field(CreatorType)
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name, email):
        creator = Creator.objects.create(name=name, email=email)
        creator.save()
        return CreatorMutation(creator=creator)

class CourseMutation(graphene.Mutation):
    course = graphene.Field(CourseType)

    class Arguments:
        title = graphene.String(required=True)
        price = graphene.String()
        description = graphene.String()
        currency = graphene.String()
        creator_id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, title, price, description, currency, creator_id):
        try:
            creator = Creator.objects.get(pk=creator_id)
            course = Course.objects.create(
                    title=title,
                    price=price,
                    description=description,
                    currency=currency,
                    creator=creator)
             
            return CourseMutation(course=course) # to return response after creating the course
        except Creator.DoesNotExist:
            raise Exception("Autho with given ID does not exist")

class Mutation(graphene.ObjectType):
    create_creator = CreatorMutation.Field()
    create_course = CourseMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

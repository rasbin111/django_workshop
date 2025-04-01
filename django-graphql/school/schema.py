import graphene
import graphql_jwt
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import Student, Teacher, Course

class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher

class CourseType(DjangoObjectType):
    class Meta:
        model = Course

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    student = graphene.Field(StudentType, id=graphene.Int(required=True))

    all_teachers = graphene.List(TeacherType)

    all_courses = graphene.List(CourseType)
    course = graphene.Field(CourseType, id=graphene.Int(required=True))

    # @login_required
    def resolve_all_students(self, info): # name should be resolve_variable_name
        return Student.objects.all()
    
    # @login_required
    def resolve_all_teachers(self, info):
        return Teacher.objects.all()

    # @login_required
    def resolve_all_courses(self, info):
        return Course.objects.all()

    # @login_required
    def resolve_student(self, info, id):
        try:
            return Student.objects.get(pk=id) 
        except:
            return None

    # @login_required
    def resolve_course(self, info, id):
        try:
            return Course.objects.get(pk=id)
        except:
            return None

schema = graphene.Schema(query=Query)

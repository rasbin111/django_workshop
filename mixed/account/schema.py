import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission
        exclude = ()

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        exclude = ()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("name", "email", "groups")


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_name = graphene.Field(UserType, name=graphene.String(required=True))

    def resolve_users(self, info):
        return User.objects.all()
    
    def resolve_user_by_name(self, info, name):
        try:
            return User.objects.get(name=name)
        except Exception as e:
            return {"message": str(e)}
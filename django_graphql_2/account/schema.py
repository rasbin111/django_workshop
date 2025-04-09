from django.contrib.auth import authenticate

import graphene
import graphql_jwt

from graphql_jwt.decorators import login_required
from graphql_jwt.shortcuts import get_token, create_refresh_token
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    whoami = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_whoami(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication failure: You must be signed in")
        return user

    @login_required
    def resolve_users(self, info):
        users = get_user_model().objects.all()
        return users


class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)
    token = graphene.String()
    ok = graphene.Boolean()

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            token = get_token(user)
            return Login(user=user, token=token, ok=True)
        else:
            return Login(user=None, token=None, ok=False)


class Mutation(graphene.ObjectType):
    token_auth =  graphql_jwt.ObtainJSONWebToken.Field()
    login = Login.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


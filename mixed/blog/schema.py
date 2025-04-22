import graphene
from graphene_django.types import DjangoObjectType
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("title", "content")


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(self, info):
        return Post.objects.filter(published=True)

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()
        owner_id = graphene.Int()
    
    post = graphene.Field(PostType)
    created = graphene.Boolean()

    def mutate(self, info, title, content, owner_id):
        try:
            owner = User.objects.get(id=owner_id)
            post = Post.objects.create(title=title, content=content, owner=owner)
            return CreatePost(post=post, created=True)

        except Exception:
            return CreatePost(post=None, created=False)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

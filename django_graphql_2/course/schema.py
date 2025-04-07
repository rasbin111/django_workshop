import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError


from .models import Course, Creator

class CreatorType(DjangoObjectType):
    class Meta:
        model = Creator
        exclude = ()

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        exclude = ()


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)
    creator_by_name = graphene.Field(CreatorType, name=graphene.String(required=True))

    def resolve_courses(self, info):
        return Course.objects.all()

    def resolve_creator_by_name(self, info, name):
        try:
            creator = Creator.objects.get(name=name)
            return creator

        except Creator.DoesNotExist:
            return None

        except Exception as e:
            return GraphQLError(f"Error: {str(e)}")


class CreatorMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        creator_info = graphene.String()


    ok = graphene.Boolean()
    creator = graphene.Field(CreatorType)

    def mutate(self, info, name, email, creator_info=None):
        try:
            creator = Creator.objects.create(
                name=name,
                email=email,
                info=creator_info
                )
            return CreatorMutation(creator=creator, ok=True)
        except Exception as e:
            return CreatorMutation(creator=None, ok=False)

class UpdateCreatorMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String()
        c_info = graphene.String()

    creator = graphene.Field(CreatorType)

    def mutate(self, info, name, email=None, c_info=None):
        try:
            creator = Creator.objects.get(name=name)
            if email:
                creator.email = email
            if c_info:
                creator.info = c_info
            creator.save()
            return UpdateCreatorMuation(creator=creator)

        except Creator.DoesNotExist:
            return GraphQLError(f"UpdateError: Does not exists ")
        
        except Exception as e:
            return GraphQLError(f"UpdateError: {str(e)}")

class DeleteCreatorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    message = graphene.String()

    def mutate(self, info, id):
        try:
            creator = Creator.objects.get(id=id)
            creator.delete()
            return DeleteCreatorMutation(message=f"Creator with id: {id} deleted")
        except Creator.DoesNotExist:
            return GraphQLError(f"UpdateError: Does not exists ")
        
        except Exception as e:
            return GraphQLError(f"UpdateError: {str(e)}")


class Mutation(graphene.ObjectType):
    create_creator = CreatorMutation.Field()
    update_creator = UpdateCreatorMutation.Field()
    delete_creator = DeleteCreatorMutation.Field()
    








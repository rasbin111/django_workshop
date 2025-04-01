import graphene

import blog.schema
import users.schema


class Query(blog.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

class Mutation(blog.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

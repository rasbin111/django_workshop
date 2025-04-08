import graphene

import course.schema
import account.schema

class Query(
        account.schema.Query,
        course.schema.Query, 
        graphene.ObjectType):
    pass

class Mutation(
        account.schema.Mutation,
        course.schema.Mutation, 
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

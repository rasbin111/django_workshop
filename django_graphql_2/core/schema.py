import graphene

import course.schema

class Query(course.schema.Query, graphene.ObjectType):
    pass

class Mutation(course.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

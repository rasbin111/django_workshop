import graphene
import account.schema
import blog.schema

class Query(account.schema.Query, blog.schema.Query):
    pass

class Mutation(blog.schema.Mutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
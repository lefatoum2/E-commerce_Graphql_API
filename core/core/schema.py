import graphene
import products.schema

class Query(products.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)
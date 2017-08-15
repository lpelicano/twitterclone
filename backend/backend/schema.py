import graphene
import app.schema


class Queries(
	app.schema.Query,
	graphene.ObjectType
):
	dummy = graphene.String()

class Mutation(
	app.schema.Mutation,
	graphene.ObjectType
):
	pass


schema = graphene.Schema(query=Queries, mutation=Mutations)

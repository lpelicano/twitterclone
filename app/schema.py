import graphene 
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id
import json

from .models import Message


class MessageType(DjangoObjectType):
	class Meta:
		model = Message
		interfaces = (graphene.Node, )


class Query(graphene.AbstractType):
	"""
	Query for backend.App
	"""
	all_messages = graphene.List(MessageType)

	def resolve_all_messages(self, args, context, info):
		"""
		Returns a list of all Message objects
		"""
		return Message.objects.all()

	def resolve_message(self, args, context, info):
		"""
		Returns a single Message object
		"""
		rid = from_global_id(args.get('id', ))
		return Message.objects.get(pk=rid[1])


class CreateMessageMutation(graphene.Mutation):
	class Input:
		message = graphene.String()

	status = graphene.Int()
	formErrors = graphene.String()
	message = graphene.Field(MessageType)

	@staticmethod
	def mutate(root, args, context, info):
		if not context.user.is_authenticated():
			return CreateMessageMutation(status=403)
		message = args.get('message', '').strip()
		if not message:
			return CreateMessageMutation(
				status=400,
				formErrors=json.dumps({
						'message': ['Please enter a message.']
					})
				)
		obj = Message.objects.create(
			user=context.user, message=message
		)
		return CreateMessageMutation(status=200, message=obj)


class Mutation(graphene.AbstractType):
	create_message = CreateMessageMutation.Field()



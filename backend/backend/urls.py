from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^gql', csrf_exempt(GraphQLView.as_view(batch=True))),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
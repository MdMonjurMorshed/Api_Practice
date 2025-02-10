from django.urls import path
from graphene_django.views import GraphQLView
from graphql_app.schema import schema
urlpatterns = [
    path('graphql-test',GraphQLView.as_view(schema=schema,graphiql=True))
]
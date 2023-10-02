from django.urls import path
from .views import *
urlpatterns = [
    path('', read_discussion, name="discussion"),
    path('create-discussion', create_discussion, name="create_discussion")
]

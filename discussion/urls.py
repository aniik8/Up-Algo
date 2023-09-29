from django.urls import path
from .views import *
urlpatterns = [
    path('', read_discussion, name="discussion")
]

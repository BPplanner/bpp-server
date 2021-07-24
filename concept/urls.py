from django.urls import path
from .views import *

urlpatterns = [
    path('', concept_list),
]
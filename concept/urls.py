from django.urls import path
from .views import *

urlpatterns = [
    path('', studio_concept_list),
    path('<int:pk>/', studio_concept_detail),
]
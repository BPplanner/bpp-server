from django.urls import path
from .views import *

urlpatterns = [
    path('studios/', studio_concept_list),
    path('studios/<int:pk>/', studio_concept_detail),
    path('beautyshops/<int:pk>/', beautyshop_concept_detail),
]
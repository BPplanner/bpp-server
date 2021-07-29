from django.urls import path
from .views import *

urlpatterns = [
    path('studios/', StudioConceptList.as_view()),
    path('studios/<int:pk>/', StudioConceptDetail.as_view()),
    path('beautyshops/<int:pk>/', BeautyshopConceptDetail.as_view()),
]
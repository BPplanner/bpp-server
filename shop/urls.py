from django.urls import path
from .views import *

urlpatterns = [
    path('studios/', studio_list),
    path('beautyshops/', beautyshop_list),
    path('<int:pk>/', shop_detail),
]
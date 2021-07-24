from django.urls import path
from .views import *

urlpatterns = [
    path('studios/', studio_list),
    path('studios/<int:pk>', shop_detail),
    path('beautyshops/<int:pk>', shop_detail),
    path('beautyshops/', beautyshop_list),
]
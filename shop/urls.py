from django.urls import path
from .views import *

urlpatterns = [
    path('<str:request_shop_type>/', shop_list),
    path('<int:pk>/', shop_detail),
]
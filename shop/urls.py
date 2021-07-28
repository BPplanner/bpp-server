from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', shop_detail),
    path('<str:request_shop_type>/', shop_list),
]
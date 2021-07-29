from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ShopDetail.as_view()),
    path('<str:request_shop_type>/', ShopList.as_view()),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ShopDetail.as_view()),  # 특정 shop 조회
    path('<int:pk>/concepts', ShopDetailConcept.as_view()),  # 특정 shop의 concept들 조회
    path('<int:pk>/like', ShopLike.as_view()),  # 특정 shop에 찜 추가,제거

    # 순서 꼭 맨 뒤어야 인식됨
    path('<str:request_shop_type>/', ShopList.as_view()),  # studio 혹은 beautyshop 전체 목록
]

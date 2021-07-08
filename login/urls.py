from django.urls import path
from .views import KakaoLogin

app_name = 'login'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
]

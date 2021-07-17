from django.urls import path
from .views import KakaoLogin,kakao_login_refresh

app_name = 'login'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('rest-auth/kakao/refresh', kakao_login_refresh, name='kakao_login_refresh'),
]

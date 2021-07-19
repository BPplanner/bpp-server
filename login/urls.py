from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import KakaoLogin,kakao_login_refresh,MyTokenObtainPairView

app_name = 'login'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('rest-auth/kakao/refresh', kakao_login_refresh, name='kakao_login_refresh'),

    # simple jwt
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # access , refresh token 발급
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 재발급 api
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # 유효성검증 api
]

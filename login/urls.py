from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .views import *

app_name = 'login'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('new-tokens/', new_tokens, name='new_tokens'),

    # simple jwt
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # access , refresh token 발급
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 재발급 api
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # 유효성검증 api
]

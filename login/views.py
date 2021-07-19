from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
#from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.registration.views import SocialLoginView
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SocialLoginSerializer,MyTokenObtainPairSerializer,CustomUserDetailsSerializer



class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


'''
    refresh_token으로 jwt 새로발급 + refresh_token 새로발급(얼마 안남았을때만)
'''


@api_view(['POST'])
def kakao_login_refresh(request):

    # request에 있는 refresh_token값
    refresh_token = json.loads(request.body.decode('utf-8')).get('refresh_token')

    # POST이면서 request에 refresh_token이 있을때
    if request.method == 'POST' and refresh_token != None:
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "refresh_token",
            "client_id": "cd05d5f98f33385e0b3f72fc619960ca",
            "refresh_token": refresh_token,
        }

        response_to_dict = json.loads(requests.post(url, data=data).content)
        new_access_token = response_to_dict.get('access_token')  # 새로운 access token
        new_refresh_token = response_to_dict.get('refresh_token')  # 새로운 refresh_token(얼마 안남았을때만)

        # access_token 새로 발급성공했을때
        if new_access_token != None:
            new_body = json.loads(requests.post(
                'http://3.35.146.251:8000/login/rest-auth/kakao/', data={"access_token": new_access_token}).content)
            new_jwt = new_body.get('token')  # 새로운 jwt
            new_data = {'new_jwt': new_jwt}
            if new_refresh_token != None:  # 새로운 refresh_token이 발급됐을때
                new_data['new_refresh_token'] = new_refresh_token
            return Response(json.dumps(new_data))

    # POST아니거나 request에 refresh_token이 없을때 + access token 발급못했을때
    return Response(status=400)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
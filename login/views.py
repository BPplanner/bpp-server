from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.registration.views import SocialLoginView
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

@api_view(['POST'])
def kakao_login_refresh(request):

    #print(request.POST.get("refresh_token"))
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode) #request의 body부분
    print(body['refresh_token'])

    if request.method == 'POST':
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type" : "refresh_token",
            "client_id"  : "cd05d5f98f33385e0b3f72fc619960ca",
            "refresh_token" : body['refresh_token'],
        }
        response = requests.post(url, data=data)
        
        return Response(response)
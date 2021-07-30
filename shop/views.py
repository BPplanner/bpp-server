from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
from rest_framework.response import Response
from .serializers import *
from .models import *



class ShopList(APIView,PageNumberPagination):

    def get(self,request, request_shop_type):
        if request_shop_type == "studios": #studio 전체목록 조회
            shop_type = Shop.STUDIO
        elif request_shop_type == "beautyshops": #beautyshop 전체목록 조회
            shop_type = Shop.BEAUTYSHOP
        else: #url잘못입력
            return Response(status=404)
        
        like = request.query_params.get('like','false') #like parameter 따로 없으면 false로
        if like=='true':
            JWT_authenticator = JWTAuthentication()
            response = JWT_authenticator.authenticate(request)
            if response is not None:
                user_id = response[1].payload['user_id']
                user = get_object_or_404(User,id=user_id) #access_token에서 user가져오기
                shops = user.like_shops.all() #user가 찜한 shop들
        else:
            shops = Shop.objects.all() #찜관련 없이 모든 shop들


        address = request.query_params.get('address','') #request parameter의 address가져오기(없다면 빈문자열로 가져오기)
        if address:
            studios = shops.filter(shop_type = shop_type, address= address).order_by('-like_count') #좋아요수 내림차순으로
        else:
            studios = shops.filter(shop_type = shop_type).order_by('-like_count') #좋아요수 내림차순으로

        self.page_size=20
        result_page = self.paginate_queryset(studios, request, view=self)
        serializer = ShopSerializer(result_page, many=True,context={"request": request})
        return self.get_paginated_response(serializer.data)

class ShopLike(APIView):
    def put(self,request,pk):
        shop = get_object_or_404(Shop, pk=pk) #어떤 shop에 like할지
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user_id = response[1].payload['user_id']
            user = get_object_or_404(User,id=user_id) #access_token에서 user가져오기
            change_to_like = json.loads(request.body.decode('utf-8')).get('change_to_like') #true or false 받기
            
            if change_to_like=="true":
                if LikeShop.objects.filter(shop=shop,user=user): #찜객체 이미 존재하면
                    return Response({"detail": "already like exist"},status=400)

                LikeShop.objects.create(shop=shop,user=user) #찜객체 만들기
                shop.like_count+=1 #shop의 찜수 증가
                return Response({"result":"shop like create"},status=200)

            elif change_to_like=="false":
                like_shop = get_object_or_404(LikeShop,shop=shop,user=user) #찜객체 제거(찜객체 애초에 없으면 404)
                like_shop.delete()
                shop.like_count-=1 #shop의 찜수 감소
                return Response({"result":"shop like delete"},status=200)

            else:
                return Response({"detail": "key should be true or false"}, status=400)
        else:
            print("no token is provided in the header or the header is missing")
    
        return Response(status=400)

class ShopDetail(APIView):
    def get(self,request,pk):
        shop = get_object_or_404(Shop, pk=pk)
        if shop.shop_type == Shop.STUDIO:
            serializer = OneStudioSerializer(shop,context={"request": request})
        else:
            serializer = OneBeautyShopSerializer(shop,context={"request": request})
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)
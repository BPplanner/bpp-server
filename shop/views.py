from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.pagination import PageNumberPagination
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

        address = request.query_params.get('address','') #request parameter의 address가져오기(없다면 빈문자열로 가져오기)
        if address:
            studios = Shop.objects.filter(shop_type = shop_type, address= address).order_by('-like_count') #좋아요수 내림차순으로
        else:
            studios = Shop.objects.filter(shop_type = shop_type).order_by('-like_count') #좋아요수 내림차순으로
            
        self.page_size=20
        result_page = self.paginate_queryset(studios, request, view=self)
        serializer = ShopSerializer(result_page, many=True,context={"request": request})
        return self.get_paginated_response(serializer.data)


class ShopDetail(APIView):
    def get(self,request,pk):
        shop = get_object_or_404(Shop, pk=pk)
        if shop.shop_type == Shop.STUDIO:
            serializer = OneStudioSerializer(shop,context={"request": request})
        else:
            serializer = OneBeautyShopSerializer(shop,context={"request": request})
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)
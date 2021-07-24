from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET'])
def studio_list(request):
    if request.method == 'GET':
        studios = Shop.objects.filter(shop_type = Shop.STUDIO)
        serializer = ShopSerializer(studios, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def beautyshop_list(request):
    if request.method == 'GET':
        beautyshops = Shop.objects.filter(shop_type = Shop.BEAUTYSHOP)
        serializer = ShopSerializer(beautyshops, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def shop_detail(request,pk):
    if request.method == 'GET':
        shop = get_object_or_404(Shop, pk=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)
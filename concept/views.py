from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *
from .models import *



class StudioConceptList(APIView,PageNumberPagination):
    def get(self,request):
        #TODO 컨셉필터링 필요
        request_head_count = request.query_params.getlist('head_count')
        request_gender = request.query_params.getlist('gender')
        request_background = request.query_params.getlist('background')
        request_prop = request.query_params.getlist('prop')
        request_dress = request.query_params.getlist('dress') #request parameter에 있는 리스트
        
        studio_concepts = StudioConcept.objects.all().order_by('-like_count') #좋아요순으로 studio concept 전체 불러오기
        filtered_studio_concepts=[]
        for studio_concept in studio_concepts:
            if request_head_count==[] or request_head_count==[''] or (set(studio_concept.head_count) & set(request_head_count)): #전체 혹은 겹치는게있으면
                if request_gender==[] or request_gender==[''] or (set(studio_concept.gender) & set(request_gender)):
                    if request_background==[]or request_background==['']  or (set(studio_concept.background) & set(request_background)):
                        if request_prop==[]or request_prop==['']  or (set(studio_concept.prop) & set(request_prop)):
                            if request_dress==[]or request_dress==['']  or (set(studio_concept.dress) & set(request_dress)):
                                filtered_studio_concepts.append(studio_concept)
        self.page_size=20
        result_page = self.paginate_queryset(filtered_studio_concepts, request)
        serializer = StudioConceptSerializer(result_page, many=True,context={"request": request})
        return self.get_paginated_response(serializer.data)

class StudioConceptDetail(APIView):
    def get(self, request, pk):
        studio_concept = get_object_or_404(StudioConcept, pk=pk)
        serializer = OneStudioConceptSerializer(studio_concept,context={"request": request})
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)

class BeautyshopConceptDetail(APIView):
    def get(self,request,pk):
        beautyshop_concept = get_object_or_404(BeautyShopConcept, pk=pk)
        serializer = OneBeautyShopConceptSerializer(beautyshop_concept,context={"request": request})
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)
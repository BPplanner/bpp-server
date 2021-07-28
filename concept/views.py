from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *
from .models import *

paginator = PageNumberPagination()
paginator.page_size = 20 #한 page에 들어갈 수

@api_view(['GET'])
def studio_concept_list(request):
    if request.method == 'GET':
        #TODO 컨셉필터링 필요
        request_head_count = request.query_params.getlist('head_count')
        request_gender = request.query_params.getlist('gender')
        request_background = request.query_params.getlist('background')
        request_prop = request.query_params.getlist('prop')
        request_dress = request.query_params.getlist('dress') #request parameter에 있는 리스트
        
        studio_concepts = StudioConcept.objects.all().order_by('-like_count') #좋아요순으로 studio concept 전체 불러오기
        filtered_studio_concepts=[]
        for studio_concept in studio_concepts:
            if request_head_count==[] or (set(studio_concept.head_count) & set(request_head_count)): #전체 혹은 겹치는게있으면
                if request_gender==[] or (set(studio_concept.gender) & set(request_gender)):
                    if request_background==[] or (set(studio_concept.background) & set(request_background)):
                        if request_prop==[] or (set(studio_concept.prop) & set(request_prop)):
                            if request_dress==[] or (set(studio_concept.dress) & set(request_dress)):
                                filtered_studio_concepts.append(studio_concept)

        result_page = paginator.paginate_queryset(filtered_studio_concepts, request)
        serializer = StudioConceptSerializer(result_page, many=True)
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)

@api_view(['GET'])
def studio_concept_detail(request,pk):
    if request.method == 'GET':
        studio_concept = get_object_or_404(StudioConcept, pk=pk)
        serializer = OneStudioConceptSerializer(studio_concept)
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)

@api_view(['GET'])
def beautyshop_concept_detail(request,pk):
    if request.method == 'GET':
        beautyshop_concept = get_object_or_404(BeautyShopConcept, pk=pk)
        serializer = OneBeautyShopConceptSerializer(beautyshop_concept)
        new_dict = {"return_data": serializer.data}
        return Response(new_dict)
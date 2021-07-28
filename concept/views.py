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
        studio_concepts = StudioConcept.objects.all()
        result_page = paginator.paginate_queryset(studio_concepts, request)
        serializer = StudioConceptSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def studio_concept_detail(request,pk):
    if request.method == 'GET':
        studio_concept = get_object_or_404(StudioConcept, pk=pk)
        serializer = OneStudioConceptSerializer(studio_concept)
        return Response(serializer.data)
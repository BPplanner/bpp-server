from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET'])
def studio_concept_list(request):
    if request.method == 'GET':
        studio_concepts = StudioConcept.objects.all()
        serializer = StudioConceptSerializer(studio_concepts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def studio_concept_detail(request,pk):
    if request.method == 'GET':
        studio_concept = get_object_or_404(StudioConcept, pk=pk)
        serializer = StudioConceptSerializer(studio_concept)
        return Response(serializer.data)
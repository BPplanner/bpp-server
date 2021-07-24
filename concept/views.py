from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET'])
def concept_list(request):
    if request.method == 'GET':
        studio_concepts = StudioConcept.objects.all()
        serializer = StudioConceptSerializer(studio_concepts, many=True)
        return Response(serializer.data)
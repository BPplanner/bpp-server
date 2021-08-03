from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
import json
from rest_framework.response import Response
from .serializers import *
from .models import *
from login.views import get_user


class StudioConceptList(APIView, PageNumberPagination):
    def get(self, request):
        request_head_count = request.query_params.getlist('head_count')
        request_gender = request.query_params.getlist('gender')
        request_background = request.query_params.getlist('background')
        request_prop = request.query_params.getlist('prop')
        request_dress = request.query_params.getlist(
            'dress')  # request parameter에 있는 리스트

        user = get_user(request)

        # like parameter 따로 없으면 false로
        like = request.query_params.get('like', 'false')
        if like == 'true':
            studio_concepts = user.like_studio_concepts.all()  # user가 찜한 studio_concept들
        else:
            studio_concepts = StudioConcept.objects.all()  # 찜관련 없이 모든 studio_concept들

        studio_concepts = studio_concepts.order_by(
            '-like_count')  # 좋아요순으로 studio concept 전체 불러오기
        filtered_studio_concepts = []
        for studio_concept in studio_concepts:
            # 전체 혹은 겹치는게있으면
            if request_head_count == [] or request_head_count == [''] or (set(studio_concept.head_count) & set(request_head_count)):
                if request_gender == [] or request_gender == [''] or (set(studio_concept.gender) & set(request_gender)):
                    if request_background == [] or request_background == [''] or (set(studio_concept.background) & set(request_background)):
                        if request_prop == [] or request_prop == [''] or (set(studio_concept.prop) & set(request_prop)):
                            if request_dress == [] or request_dress == [''] or (set(studio_concept.dress) & set(request_dress)):
                                filtered_studio_concepts.append(studio_concept)
        self.page_size = 20
        result_page = self.paginate_queryset(filtered_studio_concepts, request)
        serializer = StudioConceptSerializer(result_page, many=True, context={
                                             "request": request, "user": user})
        return self.get_paginated_response(serializer.data)


class StudioConceptLike(APIView):
    def put(self, request, pk):
        studio_concept = get_object_or_404(
            StudioConcept, pk=pk)  # 어떤 studio_concept에 like할지

        user = get_user(request)

        change_to_like = json.loads(request.body.decode(
            'utf-8')).get('change_to_like')  # true or false 받기

        if change_to_like == True:
            # 찜객체 이미 존재하면
            if LikeStudioConcept.objects.filter(studio_concept=studio_concept, user=user):
                return Response({"detail": "already like exist"}, status=status.HTTP_400_BAD_REQUEST)

            LikeStudioConcept.objects.create(
                studio_concept=studio_concept, user=user)  # 찜객체 만들기
            studio_concept.like_count += 1  # studio_concept의 찜수 증가
            return Response({"result": "studio_concept like create"}, status=status.HTTP_201_CREATED)

        elif change_to_like == False:
            like_studio_concept = get_object_or_404(
                LikeStudioConcept, studio_concept=studio_concept, user=user)  # 찜객체 제거(찜객체 애초에 없으면 404)
            like_studio_concept.delete()
            studio_concept.like_count -= 1  # studio_concept의 찜수 감소
            return Response({"result": "studio_concept like delete"}, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({"detail": "key should be true or false"}, status=status.HTTP_400_BAD_REQUEST)

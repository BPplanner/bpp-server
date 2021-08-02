from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *
import json
from django.db.models import Q
# apiview
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


def getUser(request):
    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)
    if response is not None:
        user, token = response
        return user
    else:
        return Response(status=400, data={ "error": "no token is provided in the header or the header is missing"})


class AddReservation(APIView):
    def post(self, request, pk, format=None):
        shop = get_object_or_404(Shop,id=pk) #해당shop없으면404
        reservation = Reservation(state=Reservation.INQUIRY, reserved_date=None, user=getUser(request), shop= shop)
        reservation.save()
        return Response({"result":"reservation create"},status=201)

class ReservationList(APIView, PageNumberPagination):

    def get(self, request, format=None):
        user = getUser(request)
        params = request.query_params

        if params['inquiry'] == 'true':
            #스튜디오, 뷰티샵 나누고 그안에서 최신순으로
            reservations = user.reservation_set.filter(state = Reservation.INQUIRY).order_by('shop__shop_type','-pk')
        else:
            reservations = user.reservation_set.exclude(state = Reservation.INQUIRY).order_by('shop__shop_type','-pk')

        self.page_size = 10
        page_result = self.paginate_queryset(reservations, request, view=self)
        serializer = ReservationSerializer(page_result, many=True, context={"request" : request})
        return self.get_paginated_response(serializer.data)


class ReservationDetail(APIView):
    #TODO 예약날짜 오늘날짜 이후인지 확인하는 데코레이터
    def patch(self, request, pk, format=None):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.state = Reservation.CONFIRMED
        reservation.reserved_date = json.loads(request.body.decode('utf-8')).get('reserved_date') #예약날짜 저장
        reservation.save()
        return Response(status=204)


    def delete(self, request, pk, format=None):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.delete()
        return Response(status=204)
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *
import json
from django.db.models import Q
import datetime
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

class ReservationList(APIView):

    def get(self, request, format=None):
        user = getUser(request)
        params = request.query_params

        if params['inquiry'] == 'true':
            #스튜디오, 뷰티샵 나누고 그안에서 최신순으로
            reservations = user.reservation_set.filter(state = Reservation.INQUIRY).order_by('shop__shop_type','-pk')
        else:
            reservations = user.reservation_set.exclude(state = Reservation.INQUIRY).order_by('shop__shop_type','-pk')

        
        confirmed_reservations = user.reservation_set.filter(state = Reservation.CONFIRMED).order_by('reserved_date')
        if confirmed_reservations: #예약날짜 젤빠른거
            remaining_days = (confirmed_reservations[0].reserved_date - datetime.date.today()).days
        else:
            remaining_days = None
        serializer = ReservationSerializer(reservations, many=True, context={"request" : request})
        return Response({"remaining_days":remaining_days,"return_data":serializer.data})


class ReservationDetail(APIView):
    #TODO 예약날짜 오늘날짜 이후인지 확인하는 데코레이터
    def patch(self, request, pk, format=None):
        input_date = datetime.datetime.strptime(json.loads(request.body.decode('utf-8')).get('reserved_date'),'%Y-%m-%d')
        if input_date < datetime.datetime.now(): #예약날짜가 오늘 이전일때
            return Response({"detail: reserved_date should be after today"},status=400)
            
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.state = Reservation.CONFIRMED
        reservation.reserved_date = json.loads(request.body.decode('utf-8')).get('reserved_date') #예약날짜 저장
        reservation.save()
        return Response({"detail: reserved_date input success"}, status=200)


    def delete(self, request, pk, format=None):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.delete()
        return Response({"detail: reservation delete success"}, status=200)
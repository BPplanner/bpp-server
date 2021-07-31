from django.shortcuts import render
from .models import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *
import json
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
        return Response(status=400, data={ 'error': "no token is provided in the header or the header is missing"})


class AddReservation(APIView):
    def post(self, request, pk, format=None):
        shop = Shop.objects.get(id=pk)
        reservation = Reservation(state=Reservation.INQUIRY, reserved_date=None, user=getUser(request), shop= shop)
        reservation.save()
        return Response(status=201)

class ReservationList(APIView, PageNumberPagination):
    def get(self, request, format=None):
        print(request.header)
        user = getUser(request)
        reservations = user.reservation_set.all().order_by('-pk')

        self.page_size = 10
        page_result = self.paginate_queryset(reservations, request, view=self)
        serializer = ReservationSerializer(page_result, many=True)
        return Response(serializer.data)


class ReservationDetail(APIView):
    # 특정모델을 찾아주고 없다면 404에러 발생시켜줄 함수
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return  Response(status=400, data= { 'error' : 'wrong parameters'})


    def patch(self, request, pk, format=None):
        reservation = self.get_object(pk)
        serializers = ReservationSerializer(reservation, data = request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(status=201)
        return  Response(status=400, data= { 'error' : 'wrong body'})


    def delete(self, request, pk, format=None):
        reservation = self.get_object(pk)
        reservation.delete()

        return Response(status=204)
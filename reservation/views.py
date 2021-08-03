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
from rest_framework import status
from login.views import get_user


class AddReservation(APIView):
    def post(self, request, pk, format=None):
        shop = get_object_or_404(Shop, id=pk)  # 해당shop없으면404
        reservation = Reservation(state=Reservation.INQUIRY, reserved_date=None, user=get_user(request), shop=shop)
        reservation.save()
        return Response({"result": "reservation create"}, status=status.HTTP_201_CREATED)


class ReservationList(APIView):

    def get(self, request, format=None):
        user = get_user(request)
        params = request.query_params

        if params['inquiry'] == 'true':
            # 스튜디오, 뷰티샵 나누고 그안에서 최신순으로
            reservations = user.reservation_set.filter(state=Reservation.INQUIRY).order_by('shop__shop_type', '-pk')
        else:
            reservations = user.reservation_set.exclude(state=Reservation.INQUIRY).order_by('shop__shop_type', '-pk')

        confirmed_reservations = user.reservation_set.filter(state=Reservation.CONFIRMED).order_by('reserved_date')
        if confirmed_reservations:  # 예약날짜 젤빠른거
            remaining_days = (confirmed_reservations[0].reserved_date - datetime.date.today()).days
        else:
            remaining_days = None
        serializer = ReservationSerializer(reservations, many=True, context={"request": request})
        return Response({"remaining_days": remaining_days, "results": serializer.data})


class ReservationDetail(APIView):
    # TODO 예약날짜 오늘날짜 이후인지 확인하는 데코레이터
    def patch(self, request, pk, format=None):
        user = get_user(request)
        is_match = user.reservation_set.filter(id=pk)  # 해당 예약이 유저의 예약인지 확인 

        if is_match.exists():  # 유저의 예약이 맞다면
            input_date = datetime.datetime.strptime(json.loads(request.body.decode('utf-8')).get('reserved_date'),
                                                    '%Y-%m-%d')
            if input_date < datetime.datetime.now():  # 예약날짜가 오늘 이전일때
                return Response({"detail": "reserved_date should be after today"}, status=status.HTTP_400_BAD_REQUEST)

            reservation = get_object_or_404(Reservation, pk=pk)
            reservation.state = Reservation.CONFIRMED
            reservation.reserved_date = json.loads(request.body.decode('utf-8')).get('reserved_date')  # 예약날짜 저장
            reservation.save()
            return Response({"detail": "reserved_date input success"}, status=status.HTTP_204_NO_CONTENT)

        else:  # 유저의 예약이 아니라면 
            return Response({'detail': 'user has no authority in this reservation'},
                            status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk, format=None):
        user = get_user(request)
        is_match = user.reservation_set.filter(id=pk)  # 해당 예약이 유저의 예약인지 확인 

        if is_match.exists():  # 유저의 예약이 맞다면
            reservation = get_object_or_404(Reservation, pk=pk)
            reservation.delete()
            return Response({"detail": "reservation delete success"}, status=status.HTTP_204_NO_CONTENT)

        else:  # 유저의 예약이 아니라면 
            return Response({'detail': 'user has no authority in this reservation'},
                            status=status.HTTP_401_UNAUTHORIZED)

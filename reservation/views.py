from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
import json
import datetime
# apiview
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login.views import get_user

# 예약전체조회
class ReservationList(APIView):
    def get(self, request):
        user = get_user(request) # access_token에서 user 누군지 꺼내기
        params = request.query_params # requset parameter 가져오기

        if params['inquiry'] == 'true':
            reservations = user.reservation_set.filter(state=Reservation.INQUIRY).order_by('shop__shop_type', '-pk') # 스튜디오, 뷰티샵 나누고 그안에서 최신순으로
        else:
            reservations = user.reservation_set.exclude(state=Reservation.INQUIRY).order_by('shop__shop_type', '-pk') # 스튜디오, 뷰티샵 나누고 그안에서 최신순으로

        confirmed_reservations = user.reservation_set.filter(state=Reservation.CONFIRMED).order_by('reserved_date') #예약확정중 날짜 제일빠른 예약 찾기위해
        if confirmed_reservations:  # 예약날짜 젤빠른 예약
            remaining_days = (confirmed_reservations[0].reserved_date - datetime.date.today()).days #남은일자 계산
        else: #예약확정이 하나도 없을때
            remaining_days = None
        serializer = ReservationSerializer(reservations, many=True, context={"request": request})
        return Response({"remaining_days": remaining_days, "results": serializer.data})

# shop 예약추가
class AddReservation(APIView):
    def post(self, request, pk):
        shop = get_object_or_404(Shop, id=pk)  # 해당 shop 없으면 404
        if Reservation.objects.filter(state=Reservation.INQUIRY,user=get_user(request), shop=shop):
            return Response({"detail": "already reservation exist"}, status=status.HTTP_400_BAD_REQUEST)
        reservation = Reservation(state=Reservation.INQUIRY, reserved_date=None, user=get_user(request), shop=shop) #예약확정날짜는 비우고 문의중으로 추가
        reservation.save()
        return Response({"result": "reservation create"}, status=status.HTTP_201_CREATED)

# reservation 수정, 취소
class ReservationDetail(APIView):
    def patch(self, request, pk):
        user = get_user(request) # access_token에서 user 누군지 꺼내기
        reservation = get_object_or_404(Reservation, pk=pk) # 어떤 예약에 대해서인지

        if reservation.user != user: # 해당 예약이 유저의 예약인지 확인
            return Response({'detail': 'user has no authority in this reservation'},status=status.HTTP_401_UNAUTHORIZED)

        input_date = datetime.datetime.strptime(json.loads(request.body.decode('utf-8')).get('reserved_date'),'%Y-%m-%d')
        if input_date < datetime.datetime.now():  # 예약날짜가 오늘 이전일때
            return Response({"detail": "reserved_date should be after today"}, status=status.HTTP_400_BAD_REQUEST)

        reservation.state = Reservation.CONFIRMED #문의중에서 예약확정으로 상태변경
        reservation.reserved_date = json.loads(request.body.decode('utf-8')).get('reserved_date')  # 예약날짜 저장
        reservation.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        user = get_user(request) # access_token에서 user 누군지 꺼내기
        reservation = get_object_or_404(Reservation, pk=pk) # 어떤 예약에 대해서인지

        if reservation.user != user: # 해당 예약이 유저의 예약인지 확인
            return Response({'detail': 'user has no authority in this reservation'},
                            status=status.HTTP_401_UNAUTHORIZED)
        reservation.delete() #예약 제거
        return Response(status=status.HTTP_204_NO_CONTENT)

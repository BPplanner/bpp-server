from django.urls import path
from .views import *

app_name = 'reservation'

urlpatterns = [
    path('', ReservationList.as_view()),  # 예약전체조회
    path('shops/<int:pk>', AddReservation.as_view()),  # shop 예약추가
    path('<int:pk>', ReservationDetail.as_view())   # reservation 수정, 취소
]
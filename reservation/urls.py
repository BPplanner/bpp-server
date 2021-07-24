from django.urls import path
from .views import *

app_name = 'reservation'

urlpatterns = [
    path('', ReservationList.as_view()),
    path('shops/<int:pk>', ReservationDetail.as_view()),
]
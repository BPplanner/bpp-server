from django.db import *
from login.models import *
from shop.models import *


class Reservation(TimeStampMixin):
    INQUIRY = 0  # 0 대신 RESERVATION.INQUIRY로 접근하기 위해
    CONFIRMED = 1
    EXPIRATION = 2
    STATE_CHOICES = (
        (INQUIRY, 'inquiry'),
        (CONFIRMED, 'confirmed'),
        (EXPIRATION, 'expiration')
    )

    state = models.IntegerField(null=False, blank=False, choices=STATE_CHOICES)  # 0 : 문의중 , 1 : 예약확정, 2 : 예약만료
    reserved_date = models.DateField(null=True, blank=True) #예약확정날짜(문의중일때는 null로)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

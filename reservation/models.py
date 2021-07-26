import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.db import *
from login.models import *
from shop.models import *


class Reservation(TimeStampMixin):
    state = models.IntegerField(null=False, blank=False, default=0) # 0 : 문의중 , 1 : 예약확정, 2 : 예약만료
    reserved_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
from django.db import models
from login.models import *
from shop.models import Shop


class PickShop(TimeStampMixin):
    state = models.IntegerField(null=False, blank=False, default=0) # 0 : 문의중 , 1 : 예약확정, 2 : 예약만료
    reserved_date = models.DateTimeField(null=True, blank=True)
    pick_user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
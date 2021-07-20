from django.db import models
from login.models import User
from shop.models import Shop


class PickShop(models.Model):
    state = models.IntegerField(null=False, blank=False) # 0 : 문의중 , 1 : 예약확정, 2 : 예약만료
    reserved_date = models.DateTimeField(null=True, blank=True)
    pick_user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
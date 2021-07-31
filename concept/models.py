from django.db import models
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField
from shop.models import *
from login.models import *

# CHOICES(https://pypi.org/project/django-multiselectfield/)
HEAD_COUNT_CHOICES = (
    (1, '1인'),
    (2, '2인'),
    (3, '3인이상'),
)
GENDER_CHOICES = (
    ('man','남성'),
    ('woman','여성'),
)
BACKGROUND_CHOICES = (
    ('white','흰색'),
    ('black','검은색'),
    ('chromatic', '유채색'),
    ('etc','기타배경'),
    ('outside','야외'),
)
PROP_CHOICES = (
    ('health','헬스도구'),
    ('mini','소가구'),
    ('etc','기타소품'),
)
DRESS_CHOICES = (
    ('athleisure','애슬레저'),
    ('swimsuit','수영복'),
    ('underwear','언더웨어'),
    ('etc','기타')
)

class StudioConcept(TimeStampMixin):
    profile = models.ImageField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="studio_concepts")
    like_users = models.ManyToManyField(User, through='LikeStudioConcept',related_name="like_studio_concepts", null=True,blank=True)
    like_count = models.IntegerField(default=0)

    head_count = MultiSelectField(choices=HEAD_COUNT_CHOICES)
    gender = MultiSelectField(choices=GENDER_CHOICES)
    background = MultiSelectField(choices=BACKGROUND_CHOICES)
    prop = MultiSelectField(choices=PROP_CHOICES)
    dress = MultiSelectField(choices=DRESS_CHOICES)

class LikeStudioConcept(TimeStampMixin):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    studio_concept = models.ForeignKey(StudioConcept,on_delete=models.CASCADE)

class BeautyShopConcept(TimeStampMixin):
    profile = models.ImageField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="beautyshop_concepts")
    like_users = models.ManyToManyField(User, related_name="like_beautyshop_concepts", null=True,blank=True)
    like_count = models.IntegerField(default=0)
    




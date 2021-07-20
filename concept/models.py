from django.db import models
from multiselectfield import MultiSelectField
from studio.models import *
from login.models import *

class StudioConcept(models.Model):
    profile = models.ImageField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="concepts")
    like_users = models.ManyToManyField(User, related_name="like_concepts")
    
    # 선택사항 
    # head_count_choice =
    # gender_choice =
    # background_choice =
    # dress_choice =
    # prop_choice =
    
    
    # head_count = models.MultiSelectField()
    # gender = models.MultiSelectField()
    # background = models.MultiSelectField()
    # dress = models.MultiSelectField()
    # prop = models.MultiSelectField()
    






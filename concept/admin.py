from django.contrib import admin
from .models import *


@admin.register(StudioConcept)
class StudioConceptAdmin(admin.ModelAdmin):
    list_display = ('id','shop','head_count','gender','background','prop','dress','like_count')
    list_display_links = ('id','shop','head_count','gender','background','prop','dress','like_count')


@admin.register(LikeStudioConcept)
class LikeStudioConceptAdmin(admin.ModelAdmin):
    list_display = ('id','studio_concept','user')
    list_display_links = ('id','studio_concept','user')


@admin.register(BeautyShopConcept)
class BeautyShopConceptAdmin(admin.ModelAdmin):
    list_display = ('id','shop',)
    list_display_links = ('id','shop',)
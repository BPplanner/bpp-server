from django.contrib import admin
from .models import *


@admin.register(StudioConcept)
class CustomUserAdmin(admin.ModelAdmin):
		list_display = (
            'shop',
            'like_count',
            'gender',
            'head_count',
            'background',
            'prop',
            'dress',
				)


		list_display_links = (
            'shop',
            'like_count',
            'gender',
            'head_count',
            'background',
            'prop',
            'dress',
		)



@admin.register(LikeStudioConcept)
class CustomUserAdmin(admin.ModelAdmin):
		list_display = (
            'studio_concept',
            'user'
        
				)


		list_display_links = (
            'studio_concept',
            'user'
		)



admin.site.register(BeautyShopConcept)


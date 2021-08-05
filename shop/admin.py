from django.contrib import admin
from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shop_type', 'address', 'like_count',)
    list_display_links = ('id', 'name', 'shop_type', 'address', 'like_count',)


@admin.register(LikeShop)
class LikeShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shop',)
    list_display_links = ('id', 'user', 'shop',)

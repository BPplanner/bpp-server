from django.contrib import admin
from .models import *


@admin.register(Reservation)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'state',
        'reserved_date',
        'user',
        'shop',
    )

    list_display_links = (
        'id',
        'state',
        'reserved_date',
        'user',
        'shop',
    )

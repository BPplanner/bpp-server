from .models import *
from django.utils import timezone


def reservation_state_change():
    reservations = Reservation.objects.all()
    for reservation in reservations:
        if reservation.reserved_date == Reservation.CONFIRMED and reservation.reserved_date < timezone.now():
            reservation.state = Reservation.EXPIRATION
            reservation.save()
        
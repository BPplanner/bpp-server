from .models import *
import datetime


def reservation_state_change():
    reservations = Reservation.objects.all()
    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d')
    for reservation in reservations:
        if reservation.state == Reservation.CONFIRMED and reservation.reserved_date < today:
            reservation.state = Reservation.EXPIRATION
            reservation.save()


def hello():
    print("hello")

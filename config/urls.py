from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/',include('shop.urls')),
    path('login/', include('login.urls')),
    path('studio-concepts/',include('concept.urls')),
    path('reservations/',include('reservation.urls')),
]



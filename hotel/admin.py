from django.contrib import admin
from .models import city, hotel, managers

admin.site.register(hotel)
admin.site.register(city)
admin.site.register(managers)
from django.db import models
from django.contrib.auth.models import User

#The city model is for the citys api call
class  city(models.Model):
    cityCode    = models.CharField(max_length=5,primary_key=True)
    cityName    = models.CharField(max_length=100)
    updated     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cityCode

#The hotel model is for the hotel api call
class hotel(models.Model):
    cityCode    = models.ForeignKey("city", on_delete=models.CASCADE)
    hotelCode   = models.CharField(max_length=10)
    hotelName   = models.CharField(max_length=200)
    updated     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hotelName

#The manager model links users to a city by having a foreign key to the city table
class managers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cityCode    = models.ForeignKey("city", on_delete=models.CASCADE)
    
    def __int__(self):
        return self.user.id
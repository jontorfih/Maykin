from django.test import SimpleTestCase
from hotel.form import Hotel
from hotel.models import hotel, city, managers
import datetime


class testForm(SimpleTestCase):
    
    def setUp(self):
        self.cityObj = city.objects.create(
            
            cityCode    = 'AMS',
            cityName    = 'Amsterdam',
            updated     = datetime.datetime.now(),
        )    
    def HotelFormIfValid(self):
        form = Hotel(data = {
            'hotelCode' : 'AMS92',
            'hotelName' : 'The hotel with a view',
            })
        self.assertTrue(form.valid)
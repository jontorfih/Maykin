from django.test import TestCase, Client
from django.urls import reverse
from hotel.models import hotel, city, managers
import json
import datetime
from django.contrib.auth.models import User 

"""
Test cases check first the url the see if the view return a correct template
"""


class testViews(TestCase):
    # Test setup 
    def setUp(self):
        self.client = Client()
        self.viewTemp_URL = reverse('view_Template')
        self.viewTempDet_URL = reverse('view_Template_detail',args=['AMS'])
        self.Async_Temp = reverse('Async_Temp')
        self.AsyncCityGet = reverse('city-json')
        self.new_hotel = reverse('new')
        
        self.cityObj = city.objects.create(
            
            cityCode    = 'AMS',
            cityName    = 'Amsterdam',
            updated     = datetime.datetime.now(),
        )
        
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()
    
    
    def CityGET(self):
        #Tests the response
        response = self.client.get(self.viewTemp_URL)
        #See if the response has code 200
        self.assertEqual(response.status_code, 200)
        #Check if the correct template is then used
        self.assertTemplateUsed(response, 'hotel/view_Template.html')
        
    def HotelGET(self):
        response = self.client.get(self.viewTempDet_URL)        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel/view_Template_detail.html')
        
    def Async_Temp(self):
        response = self.client.get(self.Async_Temp)        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel/hotel.html')
        
    def asyncCityGET(self):
        response = self.client.get(self.AsyncCityGet)        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel/hotel.html')
        
    def testLoginn(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('new'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
    

#Began creating tests for the asyncronus functionalty but decided I ran out of time long time ago
# Better to hand it in insted then 
    """
    def testNewHotelInCity(self):
        self.hotel2 = hotel.objects.create(
            cityCode    = self.cityObj,
            hotelCode   = 'AMS92',
            hotelName   = 'The hotel with a view',
            updated     = datetime.datetime.now(),
            
        )
        
        response = self.client.post(self.new_hotel,{            
            'cityCode':self.cityObj,
            'hotelCode':'AMS92',
            'hotelName':'The hotel with a view',
        })
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(self.)
        
    
    
    def delete_hotel(self):
        
        hotel1 = hotel.objects.create(
            cityCode    = self.cityObj,
            hotelCode   = 'AMS92',
            hotelName   = 'The hotel with a view',
            updated     = datetime.datetime.now(),
            
        )
        print(hotel1)
    """
"""
The way I structured the code is first connect to the api with the given information
First import the city data since the hotel data is related to it 
Check if the responce is valid otherwise catch the error code 
use the package pandas to easly do check like the shape has changed for e.x. new column or less columb
The model conains the provided comumbs and an extra one updated the purpose of updated 
is to keep records of old data but only show to user the newsed data at any given time.
Then by looping through all the data either the records is new all then all the lines are added 
if not then only the updated filed is changed to the current time and dates

"""

from django.core.management.base import  BaseCommand, CommandError
from hotel.models import hotel, city
import requests
import pandas as pd
import io
import datetime

def fetch_with_retry(url, num_retires=3):
    auth = ('python-demo','claw30_bumps')
    for retry_num in range(num_retires):
        response = requests.get(url, auth=auth)
        if response.ok:
            return response
    response.raise_for_status()
    raise Exception("something unexpected happend for url=%s" % url)


class Command(BaseCommand):
    def add_command(self,parser):
        parser.add_argument('C_or_H',type=str)
        
    def handle(self, *args, **options):
        
        # The following 3 functions are to import the city data
        # run city is a setup function for the api call
        def run_city(self):
            self.names      = ['code','city']
            city_url        = "http://rachel.maykinmedia.nl/djangocase/city.csv"
            response        = fetch_with_retry(city_url)
            process_city_responses(self, response.text)

        #The function prcesses the data with pandas 
        #then saves the data into the city model
        def process_city_responses(self,data):
            df = pd.read_csv(io.StringIO(data), sep=";", dtype="string", names=self.names)
            
            if city_data_is_ok(df):
                for idx, row in df.iterrows():  
                    find_city = city(cityCode = row["code"], cityName=row["city"])
                    if find_city:
                        find_city.updated = datetime.datetime.utcnow()
                        find_city.save()
                    else:
                        find_city = city(cityCode = row["code"], cityName=row["city"],updated = datetime.datetime.utcnow())
                        find_city.save()
        #The function is ment to checks on the data 
        # right number of comumbs and inclueds data
        def city_data_is_ok(df):
            if df.shape[1] == 2:
                if df.shape[0] != 0:
                    return True
                else:
                    raise Exception('Server provided no data')
            else:
                raise Exception('Unexpected number of columns in data')
        
        
        #The followiung tree functuions do the same just for the hotel api call 
        
        def run_hotel(self):
            self.names  = ['code','numb','hotelName']
            hotel_url   = "http://rachel.maykinmedia.nl/djangocase/hotel.csv"
            response    = fetch_with_retry(hotel_url)
            process_hotel_response(self,response.text)
        
        def process_hotel_response(self, data):
            df = pd.read_csv(io.StringIO(data),sep=';',dtype='string',names= self.names)
            if hotel_data_is_ok(df):
                for idx, row in df.iterrows():
                    findCity = city.objects.get(cityCode = row["code"])
                    hotel_data = hotel.objects.filter(cityCode=findCity,hotelCode=str(row["numb"]),hotelName=str(row["hotelName"]))    
                    if(hotel_data):
                        hotel_data.update(updated = datetime.datetime.now())    
                    else:
                        new_hotel = hotel(cityCode= findCity,hotelCode=str(row["numb"]),hotelName=str(row["hotelName"]),updated = datetime.datetime.now())
                        new_hotel.save()
                        
        def hotel_data_is_ok(df):
            if df.shape[1] == 3:
                if df.shape[0] != 0:
                    return True
                else:
                    raise Exception('Server provided no data')
            else:
                raise Exception('Unexpected number of columns in data')

        #Then the two api's are call and data is gathered
        run_city(self)
        run_hotel(self)
		


from django import forms
from .models import hotel,city

#Form for the manager module
class Hotel(forms.ModelForm):
    class Meta:
        model = hotel
        fields =('hotelCode','hotelName')

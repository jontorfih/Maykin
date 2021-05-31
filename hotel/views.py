from django.shortcuts import render,redirect
from .models import hotel, city, managers
from .form import Hotel
from django.views import View
from django.http import HttpResponse ,JsonResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
import datetime


#View returns the index
def index(request):
    template = 'base.html'
    return render(request,template)

#city_view and get_hotel_data are views for the Views/Template part of the website

#View returns the list of citys to choose from 
def city_view(request):
    qs_val = list(city.objects.values())
    template = 'hotel/view_Template.html'
    return render(request,template,{'data':qs_val})

#based on the city choosen in 'hotel/view_Template.html' a drill down on all hotels in the city
def get_hotel_data(request, *args, **kwargs):
    selected_code = kwargs.get('code')
    template = 'hotel/view_Template_detail.html'    
    qs_val = list(city.objects.filter(cityCode=selected_code).values())
    obj_models = list(hotel.objects.filter(cityCode=selected_code).values())
    return render(request,template,{'data':obj_models,'city':qs_val})

# Async_Temp, get_json_city_data, get_json_hotel_data are all part of the Asynchronous part of the website

#View returns the template for viewing citys and hotels
def Async_Temp(request):
    template = 'hotel/hotel.html'
    return render(request,template)

#The view is used in the main.js file to load city in dropdown list
def get_json_city_data(request):
    qs_val = list(city.objects.values())
    return JsonResponse({'data':qs_val})

#The veiw is used to in the main.js to load hotel data based on city
def get_json_hotel_data(request, *args, **kwargs):
    selected_code = kwargs.get('code')
    #Fiter hotels based on city code
    obj_models = list(hotel.objects.filter(cityCode=selected_code).values())
    return JsonResponse({'data':obj_models})


#The login, Manager_city, new_hotel, update_hotel, delete_hotel are all part of the manager module

#Class view containg both a get and a post functions
class Login(View):
    template = 'hotel/login.html'
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/manage')
        else:
            return render(request, self.template, {'form': form})

 
# After login is complete then the view filters the hotels based on the managers table 
# where each user/manager is given a city code
def Manager_city(request):
    manager = managers.objects.all().filter(user = request.user.id)
    cit  = list(hotel.objects.all().filter(cityCode = manager.get().cityCode).values())
    template = 'hotel/manager_portal.html'    
    return render(request,template,{'data':cit})

#The view creates new hotel in the city of manager
def new_hotel(request):
    upload = Hotel(request.POST)
    if request.method == 'POST':
        if upload.is_valid():
            manager = managers.objects.all().filter(user = request.user.id)
            cityCode = manager.get().cityCode
            fs = upload.save(commit=False)
            fs.cityCode = cityCode
            fs.updated = datetime.datetime.now()
            fs.save()
            return redirect('manage')
        else:
            return HttpResponse("""Error with form, reload on <a href = "manage">reload</a>""")
    else:
        return render(request, 'hotel/manager_edit.html', {'upload_form':upload})
    
#The view updates a current hotel allowing the name to be changed
def update_hotel(request, cityCode):
    try:
        hotelEdit = hotel.objects.get(hotelCode = cityCode)
    except hotel.DoesNotExist:
        return redirect('manage')
    hotelChangeForm = Hotel(request.POST or None, instance = hotelEdit)
    if hotelChangeForm.is_valid():
       hotelChangeForm.save()
       return redirect('manage')
    return render(request, 'hotel/manager_edit.html', {'upload_form':hotelChangeForm})

#The view deletes a choosen hotel
def delete_hotel(request, cityCode):
    try:
        hotelEdit = hotel.objects.get(hotelCode = cityCode)
    except hotel.DoesNotExist:
        return redirect('manage')
    hotelEdit.delete()
    return redirect('manage')
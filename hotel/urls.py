from django.urls import  path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    #Paths for the view/template module
    path('views/', views.city_view , name='view_Template'),    
    path('views/<str:code>/', views.get_hotel_data , name='view_Template_detail'),    
    #Paths for the async module
    path('async/', views.Async_Temp , name='Async_Temp'),    
    path('city-json/', views.get_json_city_data, name='city-json'),
    path('hotel-json/<str:code>/', views.get_json_hotel_data, name='hotel-json'),
    #paths for the manager module
    path('login/', views.Login.as_view(), name='login'),
    path('manage/', views.Manager_city, name='manage'),    
    path('manage/new/',views.new_hotel, name='new'),
    path('manage/update/<str:cityCode>', views.update_hotel, name='update'),
    path('manage/delete/<str:cityCode>', views.delete_hotel, name='delete'),
    
]

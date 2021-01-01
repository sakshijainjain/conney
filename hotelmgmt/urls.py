from django.conf.urls import url
from . import views


urlpatterns = [
   
    url(r'^$',views.hotel,name='front'),
    url(r'^book$',views.roomBook,name='roombook'),
    url(r'^food$',views.foodorder,name='foodOrder'),


    # url(r'^(?P<id>\d+)',views.listing,name='list'),
    # url(r'^search',views.search,name="search"),
    
   

    
] 

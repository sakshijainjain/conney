from django.conf.urls import url
from . import views


urlpatterns = [
   
    url(r'^$',views.index,name='listings'),
    url(r'^(?P<id>\d+)',views.listing,name='list'),
    url(r'^search',views.search,name="search"),
    
   

    
] 

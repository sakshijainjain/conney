from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
   
    
    url(r'^register',views.register_view,name="register"),
    url(r'^login',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout',auth_view.LogoutView.as_view(template_name='listings/listings.html'),name='logout'),
    url(r'^dashboard',views.dashboard,name="dashboard"),


    

    
   

    
] 

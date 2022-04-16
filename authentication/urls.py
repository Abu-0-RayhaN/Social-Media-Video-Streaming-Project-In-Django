import imp
from unicodedata import name
from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.auth_signup,name="authsignup"),
    path('login/',views.authlogin,name="authlogin"),
    path('logout/',views.auth_logout,name="authlogout"),
    path('user/profile/',views.Profile,name="profile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    
    
]

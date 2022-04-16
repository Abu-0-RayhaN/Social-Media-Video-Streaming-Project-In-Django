from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
    path('post/',views.post,name="post"),
    path('liked/<pk>/',views.liked,name="liked"),
    path('unliked/<pk>/',views.Unilked,name="unliked"),
    path('post/detail/<pk>/',views.detail,name="detail"),
    path('<pk>/435agfi+&*/editpost',views.editpost,name="editpost"),
   
]

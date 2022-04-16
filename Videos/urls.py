from django.urls import path
from Videos.views import Uploader,show_video,single_video,liked,Unilked,Editpost

urlpatterns = [
    path('upload/',Uploader,name="upload_video"),
    path('',show_video,name="show_video"),
    path('<int:pk>/<int:cpk>/', single_video,name="singlevideo"),
    path('liked/<int:pk>/<int:cpk>/',liked,name="liked"),
    path('unliked/<int:pk>/<int:cpk>/',Unilked,name="unliked"),
    path('<pk>/AGwinfig*&^&++/editpost/',Editpost,name="Editvideo")
]

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/',include('Videos.urls')),
    path('',include('authentication.urls')),
    path('whatsApp/',include('WhatsApp.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns +=staticfiles_urlpatterns()


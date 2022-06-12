from .views import register

from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'), 
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
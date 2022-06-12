from .views import index,item,detail,create_item,update_item, delete_item

from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'
urlpatterns = [
    path('', index, name='index'), 
    path('<int:item_id>/', detail, name='detail'), 
    path('item/', item, name='item'), 
    path('add/', create_item, name='create_item_url'), 
    path('update/<int:item_id>', update_item, name='update_item_url'),     
    path('delete/<int:item_id>', delete_item, name='delete_item_url'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    
    path('', include('home.urls')),
    path('admins', admin.site.urls ),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
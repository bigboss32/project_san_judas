from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('session/', include('apps.session.urls')),
    path('index/', include('apps.barbary.urls')),
    
 
]
from django.urls import path
from .views import index

urlpatterns = [
   
    path("sesion/",index, name='index'),

]

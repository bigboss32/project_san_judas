from django.urls import path
from .views import iniciar_sesion,registrar_usuario

urlpatterns = [
   
    path("sesion/",iniciar_sesion, name='iniciar_sesion'),
    path("registrar/", registrar_usuario, name='registrar_usuario'),
]

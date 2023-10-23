from django.urls import path
from apps.pigs.views import ViewSales  # Asegúrate de importar correctamente tu vista
from rest_framework import routers

urlpatterns = [
    path('sales/', ViewSales.as_view(), name='pigs'),
   
]


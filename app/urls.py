from django.urls import path
from . import views
urlpatterns = [
    path('',  views.Inicio, name='Inicio'),
    path('productos/',  views.Productos, name='Productos'),
     path('/logout', views.exit, name="exit"),
]
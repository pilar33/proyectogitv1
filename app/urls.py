from django.urls import path
from . import views
from app.views import ClientesListView

urlpatterns = [
    path('',  views.Inicio, name='Inicio'),
    path('productos/',  views.Productos, name='Productos'),
    path('/logout', views.exit, name="exit"),
    # path('clientes/', views.clientes, name="clientes"),
    path('clientes/',  ClientesListView.as_view(), name='Clientes'),

]
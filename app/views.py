from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Clientes
from django.views.generic import ListView

# Create your views here.
def Inicio(request):
    return render(request, "index.html")

@login_required
def Productos(request):
    return render(request, "productos.html")

def exit(request):
    logout(request)
    return redirect('Inicio')

def clientes(request):
    clientesListado = Clientes.objects.all()

    data = {
        'titulo' : 'Gestion de Clientes', 
        'clientes' : clientesListado
    }

    return render(request, "clientes.html", data)


class ClientesListView(ListView):
    model = Clientes
    template_name = 'clientes.html'
    # context_object_name = 'clientes'

    def get_queryset(self):
        return Clientes.objects.filter(idcliente=1) 

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Clientes'
        print(context)
        return context


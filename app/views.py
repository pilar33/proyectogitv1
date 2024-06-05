from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def Inicio(request):
    return render(request, "index.html")

@login_required
def Productos(request):
    return render(request, "productos.html")

def exit(request):
    logout(request)
    return redirect('Inicio')


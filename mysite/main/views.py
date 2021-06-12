from django.shortcuts import render
from .models import Veterinaria
# Create your views here.
def homepage(request):
    return render(request,"main/inicio.html", {"veterinarias": Veterinaria.objects.all})
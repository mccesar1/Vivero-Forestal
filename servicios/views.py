from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
def servicios(request):
    #importar todos los obetos de la clase servicio
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})
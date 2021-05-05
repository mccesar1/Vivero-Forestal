from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda/', views.tienda, name="Tienda"),

]

## ESTO ES PARA QUE MUESTRE LAS IMAGENES EN LA URL QUE MANDA LLAMAR DESDE EL ARCHIVO SETTINGS
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
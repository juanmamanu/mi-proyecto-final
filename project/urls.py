"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from ejemplo.views import (AltaUsuario, 
#index, index_dos , index_tres ,imc, monstrar_familiares , 
#BuscarFamiliar , AltaFamiliar, AltaMascota, BuscarMascota, mostrar_mascota)
from django.conf import settings
from django.conf.urls.static import static

from blog.views import index as blog_index
urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    #path('saludar/', index),
    #path('saludar/<nombre>/<apellido>/', index_dos),
    #path('mostrarnotas/', index_tres), 
    #path('imc/<int:altura>/<int:peso>',imc),
    #path('mi-familia/', monstrar_familiares),
    #path('mi-familia/buscar', BuscarFamiliar.as_view()),
    #path('mi-familia/alta', AltaFamiliar.as_view()),
    #path('alta-nuevo-usuario', AltaUsuario.as_view()),
    #path('panel-familia/', include('panel_familia.urls')),
    #path('mi-mascota/alta', AltaMascota.as_view()),
    #path('mi-mascota/buscar', BuscarMascota.as_view()),
    #path('mi-mascota/', mostrar_mascota), 
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
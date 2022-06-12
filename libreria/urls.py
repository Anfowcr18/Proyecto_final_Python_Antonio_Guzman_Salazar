from urllib import request
from xml.dom.minidom import Document
from django.urls import path 
from . import views 

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns =[
    path('inicio',views.inicio, name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('libros',views.libros,name='libros'),
    path('libros/crear',views.crear,name='crear'),
    path('libros/editar',views.editar,name='editar'),
    path('libros/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('libros/crear/<int:id>',views.editar,name='editar'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios/crear',views.crear,name='crear'),
    path('usuarios/editar',views.editar,name='editar'),
    path('usuarios/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('usuarios/crear/<int:id>',views.editar,name='editar'),
    path('adquisiciones',views.adquisiciones,name='adquisiciones'),
    path('adquisiciones/crear',views.crear,name='crear'),
    path('adquisiciones/editar',views.editar,name='editar'),
    path('adquisiciones/eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('adquisiciones/crear/<int:id>',views.editar,name='editar'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
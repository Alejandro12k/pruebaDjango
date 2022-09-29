from pydoc import pager
from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    # la funcion path recibe como primer parametro lo que el usuario escriba en la url, por ejemplo "nosotros". Luego recibe a donde vamos a acceder, en este caso seria a "views.nosotros" y finalmente el nombre de la funcion o archivo 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
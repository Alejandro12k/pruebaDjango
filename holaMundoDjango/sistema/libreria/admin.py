from django.contrib import admin
from . models import Libro #Estoy importando el modelo de models.py llamado "libro"
# Register your models here.
admin.site.register(Libro)  #como dandole permisos al administrador para que haga lo que quiera con la tabla libro

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(TIdentificacion)
admin.site.register(Persona)
from django.contrib import admin
from .models import Comentarios, LenguajeM, Course

# Register your models here.

admin.site.register(Course)
admin.site.register(Comentarios)
admin.site.register(LenguajeM)

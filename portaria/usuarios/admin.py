from django.contrib import admin

# Register your models here.

from usuarios.models import usuario

admin.site.register(usuario)
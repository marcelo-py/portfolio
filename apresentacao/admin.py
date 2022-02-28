from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensagem')
    list_display_links = ('usuario',)


admin.site.register(Usuario, UsuarioAdmin)


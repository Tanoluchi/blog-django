from django.contrib import admin
from .models import Page

# Configuracion extra para el modelo
class PageAdmin(admin.ModelAdmin):
    # Campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')
    # Implementamos un buscador
    search_fields = ('title', 'content')
    # Menu para filtrar por si esta visible o no
    list_filter = ('visible',)
    # En las columnas se mostrara el titulo, si esta visible y la fecha de creacion
    list_display = ('title', 'visible', 'created_at')
    # Ordenamos por la fecha de creacion, del mas nuevo al mas antiguo
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuracion del panel
title = 'Proyecto con Django'
subtitle = 'Panel de gestion'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle


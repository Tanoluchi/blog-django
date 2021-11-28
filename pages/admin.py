from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# Configuracion del panel
title = 'Proyecto con Django'
subtitle = 'Panel de gestion'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
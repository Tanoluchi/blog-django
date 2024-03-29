from typing import Any
from django.contrib import admin
from .models import Category, Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # Solo lectura
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    # Solo lectura
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user')
    list_display = ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'user__username', 'categories__name')
    
    # Cuando yo guarde mi articulo, comprobamos si el objeto que vamos a guardar le llega el user id
    # si no sucede entonces le asignamos el user_id de la request (del user identificado) 
    # y lo guardamos en obj
    def save_model(self, request, obj, form, change):        
        if not obj.user_id:
            obj.user_id = request.user.id
 
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)


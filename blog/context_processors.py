from .models import Category, Article

def get_categories(request):
    
    # Subconsulta para traer las categorias que estan relacionados con un articulo.
    # Si no se estan utilizando los descartamos.
    categories_in_use = Article.objects.filter(public = True).values_list('categories', flat = True)
    categories = Category.objects.filter(id__in = categories_in_use).values_list('id', 'name')
    
    return {
        'categories': categories,
        'ids': categories_in_use
    }
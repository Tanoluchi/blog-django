from django.shortcuts import render, get_object_or_404
from .models import Category, Article

# Create your views here.
# Traemos todos nuestros articulos y se lo pasamos a nuestro archivo HTML mediante render
def list_articles(request):
    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': articles,
    })

def category(request, category_id):
    # Le pasamos el objeto y luego la condicion, si no se llega a cumplir y no existe el id
    # pues entonces se nos redireccionara a una pagina 404 (ERROR).

    category = get_object_or_404(Category, id = category_id)

    # Filtramos y traemos todos los articulos que tengan el mismo id de categoria
    # que es pasado por parametro
    #articles = Article.objects.filter(categories = category_id)

    return render(request, 'categories/category.html', {
        'category': category,
        #'articles': articles 
    })

def article(request, article_id):
    article = get_object_or_404(Article, id = article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })
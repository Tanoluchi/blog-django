from django.contrib.auth import login
from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.
# Hacemos uso del decorador login_required para asi restringir el acceso a las paginas,
# entonces deben estar registrador y haber iniciado sesion para acceder a las paginas
@login_required(login_url="login")
def page(request, slug):

    page = Page.objects.get(slug = slug)

    return render(request, 'pages/page.html', {
        'page': page
    })
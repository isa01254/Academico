"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', lista_pessoas, name='lista_pessoas'),
    path('cursos/', lista_cursos, name='lista_cursos'),
    path('disciplinas/', lista_disciplinas, name='lista_disciplinas'),
    path('turmas/', lista_turmas, name='lista_turmas'),
    path('matriculas/', lista_matriculas, name='lista_matriculas'),
    path('cidades/', lista_cidades, name='lista_cidades'),
]

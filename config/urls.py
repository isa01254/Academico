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
    path('avaliacoes/', lista_avaliacoes, name='lista_avaliacoes'),
    path('disc_curso/', lista_disciplinas_curso, name='lista_disciplinas_curso'),
    path('frequencia/', lista_frequencias, name='lista_frequencia'),
    path('instituicao/', lista_instituicao, name='lista_instituicao'),
    path('ocorrencias/', lista_ocorrencias, name='lista_ocorrencias'),
    path('tipo_avaliacoe/', lista_tipos_avaliacao, name='lista_tipos_avaliacao'),
]
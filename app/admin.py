from django.contrib import admin
from .models import *

# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

# iv) Cursos e disciplinas
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

# vii) UF e cidades (Neste caso, Cidade já tem FK para UF se você separar os models, 
# mas aqui Cidade contém o campo UF. Se UF fosse uma classe:)
class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 3
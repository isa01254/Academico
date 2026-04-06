from django.contrib import admin
from .models import *


class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline] 

@admin.register(InstituicaoEnsino)
class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline] 

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline] 

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline] 

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline] 

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline]

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline] 


admin.site.register(Cidade)       
admin.site.register(AvaliacaoTipo)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina) 
admin.site.register(Matricula)       
admin.site.register(Avaliacao)       
admin.site.register(Frequencia)      
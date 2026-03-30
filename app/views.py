from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def lista_cursos(request):
    cursos = Curso.objects.select_related('area_saber', 'instituicao').all()
    return render(request, 'cursos.html', {'cursos': cursos})

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

def lista_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'turmas.html', {'turmas': turmas})

def lista_matriculas(request):
    matriculas = Matricula.objects.select_related('pessoa', 'curso', 'turma').all()
    return render(request, 'matriculas.html', {'matriculas': matriculas})

def lista_cidades(request):
    cidades = Cidade.objects.all().order_by('nome')
    return render(request, 'cidades.html', {'cidades': cidades})
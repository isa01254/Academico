from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def lista_cursos(request):
    cursos = Curso.objects.select_related('area_saber', 'instituicao').all()
    return render(request, 'cursos.html', {'cursos': cursos})

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.select_related('area_saber').all()
    return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

def lista_turmas(request):
    turmas = Turma.objects.select_related('curso').all()
    return render(request, 'turmas.html', {'turmas': turmas})

def lista_matriculas(request):
    matriculas = Matricula.objects.select_related('pessoa', 'curso', 'turma').all()
    return render(request, 'matriculas.html', {'matriculas': matriculas})

def lista_cidades(request):
    cidades = Cidade.objects.all().order_by('nome')
    return render(request, 'cidades.html', {'cidades': cidades})

def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.select_related('curso', 'disciplina', 'tipo').all()
    return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

def lista_disciplinas_curso(request):
    disc_cursos = CursoDisciplina.objects.select_related('curso', 'disciplina').all()
    return render(request, 'disc_curso.html', {'disc_cursos': disc_cursos})

def lista_frequencias(request):
    frequencias = Frequencia.objects.select_related('pessoa', 'curso', 'disciplina').all()
    return render(request, 'frequencia.html', {'frequencias': frequencias})

def lista_instituicao(request):
    instituicoes = InstituicaoEnsino.objects.select_related('cidade').all()
    return render(request, 'instituicao.html', {'instituicoes': instituicoes})

def lista_ocorrencias(request):

    try:
        ocorrencias = Ocorrencia.objects.all()
    except NameError:
        ocorrencias = [] 
    return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

def lista_tipos_avaliacao(request):
    tipos = AvaliacaoTipo.objects.all()
    return render(request, 'tipos_avaliacao.html', {'tipos': tipos})
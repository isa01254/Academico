from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name = "UF") 

    def __str__(self):
        return f"{self.nome} - {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural= "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Tipo de ocupação")

class Meta:
    verbose_name = "Ocupação"
    verbose_name_plural= "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name = "Nome")
    pai = models.CharField(max_length=255, blank=True, verbose_name = "Nome do pai")
    mae = models.CharField(max_length=255, verbose_name = "Nome da mãe")
    cpf = models.CharField(max_length=14, unique=True, verbose_name = "CPF")
    data_nasc = models.DateField(verbose_name = "Data de Nascimento")
    email = models.EmailField(verborse_name = "Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name = "Nome da cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, verbose_name = "Tipode ocupação")

class Meta:
    verbose_name = "Pessoa"
    verbose_name_plural= "Pessoas"

    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    periodo = models.CharField(max_length=50) # Ex: 1º Semestre

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=20) # Matutino, etc (RF11)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=50)

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField(default=0)


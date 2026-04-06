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

    def __str__(self):
        return self.nome 
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name = "Nome")
    pai = models.CharField(max_length=255, blank=True, verbose_name = "Nome do pai")
    mae = models.CharField(max_length=255, verbose_name = "Nome da mãe")
    cpf = models.CharField(max_length=14, unique=True, verbose_name = "CPF")
    data_nasc = models.DateField(verbose_name = "Data de Nascimento")
    email = models.EmailField(verbose_name = "Email")
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

    class Meta:
        verbose_name = "Instituição de ensino"

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Área Saber"

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural= "Cursos"

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Disciplinas"
        verbose_name_plural= "Disciplinas"

    def __str__(self):
        return self.nome

class CursoDisciplina(models.Model):
    carga_horaria = models.IntegerField()
    periodo = models.CharField(max_length=50) 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Curso disciplina"

    def __str__(self):
        return self.disciplina.nome
    
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=20) 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural= "Turmas"

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural= "Matrículas"

    def __str__(self):
        return f"Matrícula de {self.pessoa.nome}"
    
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Avaliação tipo"

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural= "Avaliações"

    def __str__(self):
        return self.descricao

class Frequencia(models.Model):
    numero_faltas = models.IntegerField(default=0)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural= "Frequências"

    def __str__(self):
        return f"Frequência de {self.pessoa.nome}"
    
class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição da Ocorrência")
    data = models.DateField(auto_now_add=True, verbose_name="Data do Registro")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno/Pessoa")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Disciplina Relacionada")

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

    def __str__(self):
        return f"{self.pessoa.nome} - {self.data}"
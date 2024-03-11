from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateTimeField()
    
    def __str__(self):
        return self.nome
    
    
NIVEL = (
    ('B', 'Básico'),
    ('I', 'Intermediário'),
    ('A', 'Avançado')
 )   
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10)
    nivel = models.CharField(max_length=2, choices=NIVEL, blank=False, null=False, default='B')
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
    
    
class Matricula(models.Model):
    PERIODO = (
        ('V', 'Vespertino'),
        ('M', 'Matutino'),
        ('N', 'Noturno')   
    )
    
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)


from django.contrib import admin
from .models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    
admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nivel')
    list_display_links = ('id','codigo')
    search_fields = ('codigo',)
    list_per_page = 20
    
admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'periodo', 'curso')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20    

admin.site.register(Matricula, Matriculas)



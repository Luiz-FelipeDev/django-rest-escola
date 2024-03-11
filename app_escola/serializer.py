#TODO entender o método ReadyOnlyField()

from rest_framework import serializers
from .models import Aluno, Curso, Matricula
class AlunoSerializer(serializers.ModelSerializer):
    
    ''' 
        Classe Responsavel por Transformar dados em forma python para Json
        do modelo de Aluno
    '''
    
    class Meta:
        model = Aluno
        fields = '__all__' 
        
class CursoSerializer(serializers.ModelSerializer):
    ''' 
        Classe Responsavel por Transformar dados em forma python para Json
        do modelo de Curso
    '''
    
    class Meta:
        model = Curso 
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    ''' 
        Classe Responsavel por Transformar dados em forma python para Json
        do modelo de Matrícula
    '''
    class Meta:
        model = Matricula 
        fields = '__all__'
        
        
class ListMatriculasAlunoSerializer(serializers.ModelSerializer):
    
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()
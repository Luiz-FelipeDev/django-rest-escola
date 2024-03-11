from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListMatriculasAlunoSerializer 

class AlunoViewSet(viewsets.ModelViewSet):
    """ View responsavel por exibir todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """ View responsavel por exibir todos os cursos """
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """ View responsavel por exibir todos as matriculas """
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListMatriculasAluno(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListMatriculasAlunoSerializer
    
    

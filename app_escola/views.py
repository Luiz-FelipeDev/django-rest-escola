from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListMatriculasAlunoSerializer, ListAlunosMatriculadosCursoSerializer 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class AlunoViewSet(viewsets.ModelViewSet):
    """ View responsavel por exibir todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):
    """ View responsavel por exibir todos os cursos """
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """ View responsavel por exibir todos as matriculas """
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListMatriculasAluno(generics.ListAPIView):
    """ View responsável por listar todas matriculas(cursos) pelo ID do aluno """
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListAlunosMatriculadosCurso(generics.ListAPIView):
    """ View responsável por listas por curso as matriculas de todos os alunos daquele curso em específico """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

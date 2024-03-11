
from django.contrib import admin
from django.urls import path, include
from app_escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet, ListMatriculasAluno
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

#TODO router é um arquivo? ver depois isso

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas', ListMatriculasAluno.as_view())
]

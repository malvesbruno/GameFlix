# url - view - template

from django.urls import path, include, reverse_lazy
from .views import Homefilmes, Homepage, Detalhes_filme, PesquisarFilme, CriarConta, PaginaPerfil, MudarSenha
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhes_filme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisarFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', PaginaPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('mudarsenha/', MudarSenha.as_view(), name='mudarsenha'),
    ]
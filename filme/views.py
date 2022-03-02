from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, FormHome
from django.contrib.auth import views as auth_view

# Create your views here.



class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) #redireciona pra homepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme


class Detalhes_filme(LoginRequiredMixin, DetailView):
    template_name = "detalhes_filme.html"
    model = Filme
    # Object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        #descobrir qual filme ele ta acessando
        filme = self.get_object()
        #somar 1 na visualização do filme
        filme.visualizacoes += 1
        filme.save()
        #adicionar como filme visto do usuario
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        #redireciona o usuario para a url final
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhes_filme, self).get_context_data(**kwargs)
        #filtrar filmes com a categoria igual ao filme
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[:21]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class PesquisarFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    #edita o object list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super(CriarConta, self).form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editar_perfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class MudarSenha(LoginRequiredMixin, auth_view.PasswordChangeView):
    template_name = 'mudarsenha.html'

    def get_success_url(self):
        return reverse('filme:homefilmes')
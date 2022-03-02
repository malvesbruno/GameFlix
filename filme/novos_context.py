from .models import Filme



def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    filme_destaque = lista_filmes[0]
    return {"lista_filmes_alta": lista_filmes}


def filme_destaque(request):
    if Filme.objects.order_by('visualizacoes'):
        filme = Filme.objects.order_by('-visualizacoes')[0]
    else:
        filme = None
    return {"filme_destaque": filme}
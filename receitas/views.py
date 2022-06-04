# o import abaixo tambem deve ser feito manualmente
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse('<h1>Receitas</h1>')

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

#def index(request):
#
#    receitas = {
#        1: 'Lasanha',
#        2: 'Sopa de legumes',
#        3: 'Sorvete',
#        4: 'Bolo de chocolate'
#    }
#
#    dados = {
#        'nome_das_receitas': receitas
#    }
#
#    return render(request, 'index.html', dados)

def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk = receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)
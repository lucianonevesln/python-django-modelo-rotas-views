# apos a criacao do arquivo urls.py, e necessario importar a biblioteca abaixo
from django.urls import path

# em seguida, as views
from . import views

# e depois urlpatterns
urlpatterns = [
    # cria uma rota, informando que a pagina principal de visualizacao
    # seja a pagina de receitas no primeiro parametro, quem sera responsavel 
    # por atender a requisicao no segundo e name space para entradas de urls
    path('', views.index, name = 'index'),
    path('<int:receita_id>', views.receita, name = 'receita')
]
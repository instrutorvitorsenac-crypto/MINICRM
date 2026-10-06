from django.shortcuts import render
from .models import Cliente

# Create your views here.
def home(requests):
    lista_clientes = Cliente.objects.all()


    total_negociacao = 0
    for cliente in lista_clientes:
        if cliente.status == 'negociacao':
            total_negociacao += 1
    # Criar o total de clientes
    # Total de clientes fechados
    # Total de valor da proposta

    total_fechado = 0
    for cliente in lista_clientes:
        if cliente.status == "fechado":
            total_fechado += 1

    total_proposta = 0
    for cliente in lista_clientes:
        if cliente.status == "fechado":
            total_proposta += cliente.valor_proposta

 
    contexto = {
        'lista_clientes': lista_clientes,
        'total_negociacao': total_negociacao,
        'total_fechado': total_fechado,
        'total_proposta': total_proposta
        
    }


    return render(requests, 'home.html', context=contexto)

    


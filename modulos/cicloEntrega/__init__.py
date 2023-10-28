import json
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas
from datetime import datetime

def buscaCiclosEntrega():
    with open('dadosJson/baseCiclosEntrega.json', 'r') as arquivo:
        dados = json.load(arquivo)

    dataAtual = datetime.now()
    
    retorno = []
    for dado in dados:
        dataFinal = datetime.strptime(dado['dataFinal'], "%d/%m/%Y")
        dadoRetorno = {
            "chave":dado['chave'],
            "titulo":dado['titulo'],
            "dataInicial":dado['dataInicial'],
            "dataFinal":dado['dataFinal'],
            "estado": 'desativado'
        }
        if dataFinal >= dataAtual:
            dadoRetorno['estado'] = 'ativo'
        
        retorno.append( dadoRetorno )

    return retorno

def buscaCiclosEntregaAtivos():
    dadosCicloEntregas = buscaCiclosEntrega()

    retorno = []
    ordem = 0
    for dadosCicloEntrega in dadosCicloEntregas:
        if dadosCicloEntrega['estado'] == 'ativo':
            dadosCicloEntrega['ordem'] = ordem
            ordem += 1
            retorno.append( dadosCicloEntrega )

    return retorno


def gravaCiclosEntrega(dados):
    with open('dadosJson/baseCiclosEntrega.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)
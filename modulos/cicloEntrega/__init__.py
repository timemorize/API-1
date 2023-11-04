import json
from flask import jsonify
import random
from modulos import configuracoesSistema, grupos, turmas
from datetime import datetime, timedelta

def buscaDados():
    with open('dadosJson/baseCiclosEntrega.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def buscaCiclosEntrega():
    dados = buscaDados()
    dataAtual = datetime.now()
    margemTempo = int(configuracoesSistema.buscaTempoLimiteConclusaoCicloEntrega())
    dataVencimento = dataAtual - timedelta(days=margemTempo)
    
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
        if dataFinal >= dataVencimento:
            dadoRetorno['estado'] = 'ativo'
        
        retorno.append( dadoRetorno )

    return retorno

def cadastrarCicloEntrega( dadosEntrada ):
    dados = buscaDados()

    if len(dados) == 0:
        chave = 1
    else:
        ultimoElemento = dados[-1]
        chave = int(ultimoElemento['chave']) + 1

    chave = str(chave)

    novoCiclo ={
        "chave":chave,
        "titulo":dadosEntrada['titulo'],
        'dataInicial':dadosEntrada['dataInicial'],
        'dataFinal': dadosEntrada['dataFinal'],
    }

    dados.append(novoCiclo)

    gravaCiclosEntrega(dados)

    return ''

def editarCicloEntrega( dadosEntrada ):
    dados = buscaDados()

    novosDados = []
    for dado in dados:
        if int(dado['chave']) == int(dadosEntrada['chave']):
            dadosEdiados ={
                "chave":dadosEntrada['chave'],
                "titulo":dadosEntrada['titulo'],
                'dataInicial':dadosEntrada['dataInicial'],
                'dataFinal': dadosEntrada['dataFinal'],
            }

            novosDados.append( dadosEdiados )
        else:
            novosDados.append( dado )

    gravaCiclosEntrega(novosDados)

    return ''

def excluirCicloEntrega( chave ):
    dados = buscaDados()

    novosDados = []
    for dado in dados:
        if int(dado['chave']) != int(chave):
            novosDados.append( dado )

    gravaCiclosEntrega(novosDados)

    return ''

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
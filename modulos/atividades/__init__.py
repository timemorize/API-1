import json
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas

def buscaAtividades():
    with open('dadosJson/baseAtividades.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def gravaAtividades(dados):
    with open('dadosJson/baseAtividades.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def cadastroAtividade( dados ):
    dadosAtividades = buscaAtividades()

    if len(dadosAtividades) == 0:
        chave = 1
    else:
        ultimoElemento = dadosAtividades[-1]
        chave = ultimoElemento['chave'] + 1

    novaAtividade ={
        "chave":chave,
        "dataEntrega":dados['dataEntrega'],
        "descricao":dados['descricao'],
        "turma":dados['idTurma']
    }

    dadosAtividades.append( novaAtividade )
    gravaAtividades( dadosAtividades )

    return ''

def editarAtividade( entradaDadosAtividade ):
    dadosAtividades = buscaAtividades()

    chave = entradaDadosAtividade['chave']

    novosDados = []
    for dadosAtividade in dadosAtividades:
        if dadosAtividade['chave'] != chave:
            novosDados.append(dadosAtividade)
        else:
            dadosAtividadeEditado = {
                "chave":entradaDadosAtividade['chave'],
                "dataEntrega":entradaDadosAtividade['dataEntrega'],
                "descricao":entradaDadosAtividade['descricao'],
                "turma":entradaDadosAtividade['idTurma']
            }
            novosDados.append(dadosAtividadeEditado)

    gravaAtividades(novosDados)

    return ''


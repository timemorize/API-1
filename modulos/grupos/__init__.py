import json
from flask import jsonify
import random
from modulos import alunos

def buscaDadosGrupos():
    with open('dadosJson/baseGrupos.json', 'r') as arquivo:
        dadosGrupos = json.load(arquivo)
        dadosGrupos = sorted(dadosGrupos, key=lambda x: x["nome"])

    return dadosGrupos

def gravarGrupos(dadosGrupos):
    with open('dadosJson/baseGrupos.json', 'w') as arquivoGrupos:
        json.dump(dadosGrupos, arquivoGrupos, indent=2)

def cadastrarGrupo( dadosGrupoEntrada ):
    dadosGrupos = buscaDadosGrupos()
    numeroRegistros = int(len(dadosGrupos))

    if numeroRegistros < 1:
        chave = 1
    else:
        ultimoElemento = dadosGrupos[-1]
        chave = ultimoElemento['chave'] + 1
        
    idGrupo = "GRP" + str( chave ) + str(random.randint(100, 999))

    novoGrupo = {
        'chave': chave,
        'identificador': idGrupo,
        'nome' :  dadosGrupoEntrada['nome'],
		'descricao' : dadosGrupoEntrada['descricao']
    }

    dadosGrupos.append(novoGrupo)

    gravarGrupos( dadosGrupos )

    return ''

def excluirGrupo( id ):
    dadosGrupos = buscaDadosGrupos()

    novosDados = []
    for dadosGrupo in dadosGrupos:
        if dadosGrupo['identificador'] != id:
            novosDados.append(dadosGrupo)

    gravarGrupos( novosDados )

    return ''

def editarGrupo( entradaDadosGrupo ):
    dadosGrupos = buscaDadosGrupos()

    id = entradaDadosGrupo['identificador']

    novosDados = []
    for dadosGrupo in dadosGrupos:
        if dadosGrupo['identificador'] != id:
            novosDados.append(dadosGrupo)
        else:
            novosDadosGrupo = {
                'identificador': id,
                'nome' :  entradaDadosGrupo['nome'],
                'descricao' : entradaDadosGrupo['descricao']
            }
            novosDados.append(novosDadosGrupo)

    gravarGrupos( novosDados )

    return ''

def buscaListaGruposAluno( listaGrupos ):
    dadosGrupos = buscaDadosGrupos()
    gruposInseridos = []
    gruposDisponiveis =[]
    for dadosTurma in dadosGrupos:
        retornoGrupos = {
                'identificador': dadosTurma['identificador'],
                'nome': dadosTurma['nome']
            }
        if dadosTurma['identificador'] in listaGrupos:
            gruposInseridos.append(retornoGrupos)
        else:
            gruposDisponiveis.append(retornoGrupos)

    retorno = {
        "gruposInseridos":gruposInseridos,
        "gruposDisponiveis":gruposDisponiveis
    }
    return retorno


def buscaAlunos( identificador ):
    dadosAlunos = alunos.buscaDadosAlunos()
    
    alunosInseridos = []
    alunosNaoInseridos = []

    for dadosAluno in dadosAlunos:
        if identificador in dadosAluno['grupos']:
            alunosInseridos.append( dadosAluno )
        else:
            alunosNaoInseridos.append( dadosAluno )

    retorno = {
        "inseridos":alunosInseridos,
        "naoInseridos":alunosNaoInseridos
    }

    return retorno
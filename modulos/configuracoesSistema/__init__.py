import json
from modulos import alunos,professores,turmas

def buscaDados():
    with open('dadosJson/baseConfiguracoesSistema.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def buscaTempoLimiteConclusaoCicloEntrega():
    dados = buscaDados()

    return dados['tempoLimiteConclusaoCicloEntrega']

def buscaMediaMinima():
    dados = buscaDados()

    return dados['mediaMinima']

def relacaoTiposUsuario():
    quantidadeAlunos = alunos.buscaQuantidadeAlunos()
    quantidadeTurmas = turmas.buscaQuantidadeTurmas()
    quantidadeProfessores = professores.buscaQuantidadeProfessores()

    retorno =[
        {
            'entidade':'Alunos',
            'quantidade': quantidadeAlunos
        },
        {
            'entidade':'Professores',
            'quantidade': quantidadeProfessores
        },
        {
            'entidade':'Turmas',
            'quantidade': quantidadeTurmas 
        }
    ]

    return retorno
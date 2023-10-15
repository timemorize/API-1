import json
from modulos import alunos,professores
import random

def buscaDadosTurmas():
    with open('dadosJson/baseTurmas.json', 'r') as arquivo:
        dadosTurmas = json.load(arquivo)
        retorno = []
        for dadosTurma in dadosTurmas:
            dadosProfessor = professores.pesquisaProfessor( dadosTurma['professor'] )
            dados = {
                'chave': dadosTurma['chave'],
                'identificador': dadosTurma['identificador'],
                'nome' :  dadosTurma['nome'],
                'professor' : dadosTurma['professor'],
                'nomeProfessor' : dadosProfessor['nome']
            }
            retorno.append( dados )

    return retorno

def gravarTurmas( dadosTurmas ):
    with open('dadosJson/baseTurmas.json', 'w') as arquivo:
        json.dump(dadosTurmas, arquivo, indent=2)

def cadastrarTurma( dadosTurma ):
    dadosTurmas = buscaDadosTurmas()

    if len(dadosTurmas) == 0:
        chave = 1
    else:
        ultimoElemento = dadosTurmas[-1]
        chave = ultimoElemento['chave'] + 1
    
    abreviacao = obtemAbreviacaoTurma( dadosTurma['nome'] )
    idTurma = abreviacao + str( chave ) + str(random.randint(100, 999))

    novoGrupo = {
        'chave': chave,
        'identificador': idTurma,
        'nome' :  dadosTurma['nome'],
		'professor' : dadosTurma['professor']
    }

    dadosTurmas.append(novoGrupo)

    gravarTurmas( dadosTurmas )

    return ''

def obtemAbreviacaoTurma( nomeTurma ):
    palavras = nomeTurma.split()
    palavras = nomeTurma.split()  # Divide a string em palavras
    iniciais = ''.join(word[0].upper() for word in palavras if len(word) >= 3)  # Obtém a primeira letra de palavras com 3 ou mais letras
    return iniciais

def buscaQuantidadeTurmas():
    return len(buscaDadosTurmas())

def buscaListaTurmas( listaTurmas ):
    dadosTurmas = buscaDadosTurmas()
    turmasMatriculado = []
    turmasNaoMatriculado =[]
    for dadosTurma in dadosTurmas:
        retornoTurma = {
                'identificador': dadosTurma['identificador'],
                'nome': dadosTurma['nome']
            }
        if dadosTurma['identificador'] in listaTurmas:
            turmasMatriculado.append(retornoTurma)
        else:
            turmasNaoMatriculado.append(retornoTurma)

    retorno = {
        "matriculado":turmasMatriculado,
        "naoMatriculado":turmasNaoMatriculado
    }
    return retorno

def buscaAlunos( identificador ):
    dadosAlunos = alunos.buscaDadosAlunos()
    
    alunosMatriculados = []
    alunosNaoMatriculados = []

    for dadosAluno in dadosAlunos:
        if identificador in dadosAluno['turmas']:
            alunosMatriculados.append( dadosAluno )
        else:
            alunosNaoMatriculados.append( dadosAluno )

    retorno = {
        "matriculado":alunosMatriculados,
        "naoMatriculado":alunosNaoMatriculados
    }

    return retorno

def buscaQuantidadeTurmasAluno(): 
    dadosAlunos = alunos.buscaDadosAlunos()
    dadosTurmas = buscaDadosTurmas()
    retorno = []
    for dadosTurma in dadosTurmas:
        quantidadeAlunos = 0
        for dadosAluno in dadosAlunos:
            if dadosTurma['identificador'] in dadosAluno['turmas']:
                quantidadeAlunos = quantidadeAlunos + 1
        retornoTurma = {
            'nome':dadosTurma['nome'],
            'identificador':dadosTurma['identificador'],
            'quantidade':quantidadeAlunos
        }
        retorno.append( retornoTurma )

    return retorno

def editarTurma( entradaDadosTurma ):
    dadosTurmas = buscaDadosTurmas()

    id = entradaDadosTurma['identificador']

    novosDados = []
    for dadosTurma in dadosTurmas:
        if dadosTurma['identificador'] != id:
            novosDados.append(dadosTurma)
        else:
            novosDadosGrupo = {
                'chave' :dadosTurma['chave'],
                'identificador': id,
                'nome' :  entradaDadosTurma['nome'],
                'professor' : entradaDadosTurma['professor']
            }
            novosDados.append(novosDadosGrupo)

    gravarTurmas( novosDados )

    return ''

def excluirTurma( id ):
    dadosTurmas = buscaDadosTurmas()

    novosDados = []
    for dadosTurma in dadosTurmas:
        if dadosTurma['identificador'] != id:
            novosDados.append(dadosTurma)

    gravarTurmas( novosDados )

    return ''
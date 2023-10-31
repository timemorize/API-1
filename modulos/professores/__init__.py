import json
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas, atividades

def buscaDadosProfessores():
    with open('dadosJson/baseProfessores.json', 'r') as arquivo:
        retorno = json.load(arquivo)
    return retorno

def gravarProfessor(dadosProfessor):
    with open('dadosJson/baseProfessores.json', 'w') as arquivoProfessor:
        json.dump(dadosProfessor, arquivoProfessor, indent=2)

def pesquisaProfessor( identificador ):
    dadosProfessores = buscaDadosProfessores()

    retorno = []
    for dadosProfessor in dadosProfessores:
        if dadosProfessor['identificador'] == identificador:
            retornoAlunos = {
                'identificador': identificador,
                'nome' :  dadosProfessor['nome']
            }

            retorno = retornoAlunos

    return retorno

def cadastrarProfessor( dadosAluno ):
    dadosProfessor = buscaDadosProfessores()

    if len(dadosAluno) == 0:
        chave = 1
    else:
        ultimoElemento = dadosProfessor[-1]
        chave = ultimoElemento['chave'] + 1
        
    idProfessor = "PRF" + str( chave ) + str(random.randint(100, 999))

    novoAluno = {
        'chave': chave,
        'identificador': idProfessor,
        'nome' :  dadosAluno['nome'],
		'email' : dadosAluno['email']
    }

    dadosProfessor.append(novoAluno)

    gravarProfessor( dadosProfessor )

    senha = usuarios.cadastrarUsuario( idProfessor, "professor")

    return jsonify({'result': '1', 'senhaProfessor': senha, 'identificador':idProfessor})

def buscarTurmas( identificador ):
    retorno = []
    dadosTurmas = turmas.buscaDadosTurmas()
    for dadosTurma in dadosTurmas:
        if dadosTurma['professor'] == identificador:
            
            pesoTotalTurma = atividades.getPesoTotalAtividades( dadosTurma['identificador'] )
            dadosRetorno ={
                'nome':dadosTurma['nome'],
                'identificador':dadosTurma['identificador'],
                'pesoTotalTurma': pesoTotalTurma
            }
            retorno.append(dadosRetorno)

    return retorno

def excluirProfessor( id ):
    dadosProfessores = buscaDadosProfessores()

    novosDados = []
    for dadosProfessor in dadosProfessores:
        if dadosProfessor['identificador'] != id:
            novosDados.append(dadosProfessor)

    gravarProfessor( novosDados )

    return ''

def editarProfessor( entradaDadosProfessor ):
    dadosProfessors = buscaDadosProfessores()

    id = entradaDadosProfessor['identificador']

    novosDados = []
    for dadosProfessor in dadosProfessors:
        if dadosProfessor['identificador'] != id:
            novosDados.append(dadosProfessor)
        else:
            novosDadosGrupo = {
                'chave' :dadosProfessor['chave'],
                'identificador': id,
                'nome' :  entradaDadosProfessor['nome'],
                'email' : entradaDadosProfessor['email']
            }
            novosDados.append(novosDadosGrupo)

    gravarProfessor( novosDados )

    return ''

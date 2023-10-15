import json
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas

def buscaDadosAlunos():
    with open('dadosJson/baseAlunos.json', 'r') as arquivo:
        dadosAlunos = json.load(arquivo)
        dadosAlunos = sorted(dadosAlunos, key=lambda x: x["nome"])

    return dadosAlunos

def gravarAlunos(dadosAlunos):
    with open('dadosJson/baseAlunos.json', 'w') as arquivoAlunos:
        json.dump(dadosAlunos, arquivoAlunos, indent=2)

def cadastrarAluno( dadosAluno ):
    dadosAlunos = buscaDadosAlunos()

    if len(dadosAluno) == 0:
        chave = 1
    else:
        ultimoElemento = dadosAlunos[-1]
        chave = ultimoElemento['chave'] + 1
        
    raAluno = "ALUNO" + str( chave ) + str(random.randint(100, 999))

    novoAluno = {
        'chave': chave,
        'RA': raAluno,
        'nome' :  dadosAluno['nome'],
		'cpf' : dadosAluno['cpf'],
		'rg' : dadosAluno['rg'],
		'email' : dadosAluno['email'],
		'telefone' : dadosAluno['telefone'],
		'cep' : dadosAluno['cep'],
		'numero' : dadosAluno['numero'],
		'logradouro' : dadosAluno['logradouro'],
		'bairro' : dadosAluno['bairro'],
		'cidade' : dadosAluno['cidade'],
		'estado' : dadosAluno['estado'],
        'turmas' : [],
        'grupos': []
    }

    dadosAlunos.append(novoAluno)

    gravarAlunos( dadosAlunos )

    senha = usuarios.cadastrarUsuario( raAluno, "aluno")

    return jsonify({'result': '1', 'senhaAluno': senha, 'raAlunos':raAluno})

def pesquisaAluno( ra ):
    dadosAlunos = buscaDadosAlunos()

    retorno = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] == ra:
            retornoAlunos = {
                'RA': ra,
                'nome' :  dadosAluno['nome'],
                'cpf' : dadosAluno['cpf'],
                'rg' : dadosAluno['rg'],
                'email' : dadosAluno['email'],
                'telefone' : dadosAluno['telefone'],
                'cep' : dadosAluno['cep'],
                'numero' : dadosAluno['numero'],
                'logradouro' : dadosAluno['logradouro'],
                'bairro' : dadosAluno['bairro'],
                'cidade' : dadosAluno['cidade'],
                'estado' : dadosAluno['estado'],
                'turmas' : dadosAluno['turmas'],
                'grupos':dadosAluno['grupos']
            }

            retorno = retornoAlunos

    return retorno

def editarAluno( entradaDadosAluno ):
    dadosAlunos = buscaDadosAlunos()

    ra = entradaDadosAluno['ra']

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] != ra:
            novosDados.append(dadosAluno)
        else:
            novosDadosAluno = {
                'RA': ra,
                'nome' :  entradaDadosAluno['nome'],
                'cpf' : entradaDadosAluno['cpf'],
                'rg' : entradaDadosAluno['rg'],
                'email' : entradaDadosAluno['email'],
                'telefone' : entradaDadosAluno['telefone'],
                'cep' : entradaDadosAluno['cep'],
                'numero' : entradaDadosAluno['numero'],
                'logradouro' : entradaDadosAluno['logradouro'],
                'bairro' : entradaDadosAluno['bairro'],
                'cidade' : entradaDadosAluno['cidade'],
                'estado' : entradaDadosAluno['estado']
            }
            novosDados.append(novosDadosAluno)

    gravarAlunos( novosDados )

    return ''

def excluirAlunos( ra ):
    dadosAlunos = buscaDadosAlunos()

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] != ra:
            novosDados.append(dadosAluno)

    gravarAlunos( novosDados )

    return ''

def buscaGruposAlunos( ra ):
    dadosAluno = pesquisaAluno( ra )

    listaGrupos = dadosAluno['grupos']
    retorno = grupos.buscaListaGruposAluno(listaGrupos)

    return retorno

def inserirGrupos( ra, listaGrupos ):
    dadosAlunos = buscaDadosAlunos()

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] == ra:
            dadosAluno['grupos'] = listaGrupos

        novosDados.append(dadosAluno)

    gravarAlunos( novosDados )

def inserirTurmas( ra, listaTurmas ):
    dadosAlunos = buscaDadosAlunos()

    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] == ra:
            dadosAluno['turmas'] = listaTurmas

        novosDados.append(dadosAluno)

    gravarAlunos( novosDados )

def buscaTurmasAlunos( ra ):
    dadosAluno = pesquisaAluno( ra )

    listaTurmas = dadosAluno['turmas']
    retorno = turmas.buscaListaTurmas(listaTurmas)

    return retorno
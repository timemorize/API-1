import json
from datetime import datetime
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas, atividades, cicloEntrega, configuracoesSistema

def buscaDadosAlunos():
    with open('dadosJson/baseAlunos.json', 'r') as arquivo:
        dadosAlunos = json.load(arquivo)
        dadosAlunos = sorted(dadosAlunos, key=lambda x: x["nome"])

    return dadosAlunos

def gravarAlunos(dadosAlunos):
    with open('dadosJson/baseAlunos.json', 'w') as arquivoAlunos:
        json.dump(dadosAlunos, arquivoAlunos, indent=2)

def buscaQuantidadeAlunos():
    return len(buscaDadosAlunos())

def cadastrarAluno( dadosAluno ):
    dadosAlunos = buscaDadosAlunos()
    numeroRegistros = len(dadosAlunos)

    if int(numeroRegistros) < 1:
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

    nomeAluno = ""
    novosDados = []
    for dadosAluno in dadosAlunos:
        if dadosAluno['RA'] == ra:
            dadosAluno['turmas'] = listaTurmas
            nomeAluno = dadosAluno['nome']

        novosDados.append(dadosAluno)

    
    for turma in listaTurmas:
        atividades.iniciaAlunoAtividadesTurma( ra, nomeAluno, turma)

    gravarAlunos( novosDados )

def buscaTurmasAlunos( ra ):
    dadosAluno = pesquisaAluno( ra )

    listaTurmas = dadosAluno['turmas']
    retorno = turmas.buscaListaTurmas(listaTurmas)

    return retorno

def buscaScoreAluno( ra, idTurma ):
    dadosAtividades = atividades.buscaAtividades()
    dadosCiclosEntrega = cicloEntrega.buscaCiclosEntrega()
    pesosCicloEntrega = atividades.buscaPesoTotal( idTurma )
    mediaMinima = configuracoesSistema.buscaMediaMinima()
    retorno = []

    for dadosCicloEntrega in dadosCiclosEntrega:
        estadoMedia = 'Integral'
        possuiAtividades = False
        parcialCicloEntrega = []
        pesoTotal = 1
        for pesoCicloEntrega in pesosCicloEntrega:
            if pesoCicloEntrega['chaveCicloEntrega'] == dadosCicloEntrega['chave']:
                pesoTotal = pesoCicloEntrega['pesoTotalCiclo']
        
        mediaParcial = 0
        for dadosAtividade in dadosAtividades:
            if dadosCicloEntrega['chave'] == dadosAtividade['cicloEntrega'] and dadosAtividade['turma'] == idTurma:
                parcialScores ={
                    "chave": dadosAtividade['chave'],
                    "peso": dadosAtividade['peso'],
                    "titulo": dadosAtividade['titulo'],
                    "descricao":dadosAtividade['descricao'],
                    "dataEntrega": dadosAtividade['dataEntrega'],
                    "score":""
                }
                
                possuiAtividades = True

                for scoresAluno in dadosAtividade['scores']:
                    if scoresAluno['RA'] == ra:
                        parcialScores["score"] = scoresAluno['nota']
                        notaFormatada = scoresAluno['nota'].replace('.', ',')

                if parcialScores['score'] != '':
                    mediaParcial += float(parcialScores['score']) * float(parcialScores['peso']) / float(pesoTotal)
                else:
                    estadoMedia = 'Parcial'

                parcialScores["score"] = notaFormatada
                parcialCicloEntrega.append(parcialScores)


        possuiAnoAtual = cicloEntrega.cicloPossuiAnoAtual(dadosCicloEntrega['dataInicial'],dadosCicloEntrega['dataFinal'])
        notaVermelha = mediaParcial < mediaMinima

        dataInicial = datetime.strptime(dadosCicloEntrega['dataInicial'], '%d/%m/%Y')
        dataFinal = datetime.strptime(dadosCicloEntrega['dataFinal'], '%d/%m/%Y')

        diasTotais=dataFinal-dataInicial
        dataHoje = datetime.today()
        diasPassados=dataFinal-dataHoje
        diasPorc=diasPassados*100/diasTotais

        retorno.append({
            "cicloEntregaTitulo":dadosCicloEntrega['titulo'],
            "cicloEntregaDataInicio":dadosCicloEntrega['dataInicial'],
            "cicloEntregaDataFinal":dadosCicloEntrega['dataFinal'],
            "cicloEntregaDiasPorcentagem":100-diasPorc,
            "parcialScores":parcialCicloEntrega,
            "mediaParcial":"{:.2f}".format(mediaParcial).replace('.', ','),
            "estadoMedia":estadoMedia,
            "pesoTotal":pesoTotal,
            "possuiAtividades":possuiAtividades,
            "possuiAnoAtual":possuiAnoAtual,
            "estado":dadosCicloEntrega['estado'],
            "notaVermelha":notaVermelha
        })

    return retorno
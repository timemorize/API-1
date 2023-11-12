import json
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas, cicloEntrega
from datetime import datetime

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

    alunosTurma = turmas.buscaAlunos(dados['idTurma'])['matriculado']

    scoresIniciais = []

    for alunoTurma in alunosTurma:
        notaInicial = {
            'RA': alunoTurma['RA'],
            'nota' : '',
            'nomeAluno': alunoTurma['nome']
        }

        scoresIniciais.append( notaInicial )

    novaAtividade ={
        "chave":chave,
        "peso":dados['peso'],
        "titulo":dados['titulo'],
        "dataEntrega":dados['dataEntrega'],
        "descricao":dados['descricao'],
        "turma":dados['idTurma'],
        "cicloEntrega": dados['chaveCicloEntrega'],
        "scores":scoresIniciais
    }

    dadosAtividades.append( novaAtividade )
    gravaAtividades( dadosAtividades )

    return ''

def pesquisaAtividade( chaveAtividade ):
    dadosAtividades = buscaAtividades()

    for dadosAtividade in dadosAtividades:
        if dadosAtividade['chave'] == chaveAtividade:
            return dadosAtividade
        
    return []

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
                "titulo":entradaDadosAtividade['titulo'],
                "dataEntrega":entradaDadosAtividade['dataEntrega'],
                "descricao":entradaDadosAtividade['descricao'],
                "cicloEntrega": entradaDadosAtividade['chaveCicloEntrega'],
                "turma":entradaDadosAtividade['idTurma'],
                "scores":dadosAtividade['scores']
            }
            novosDados.append(dadosAtividadeEditado)

    gravaAtividades(novosDados)

    return ''

def excluirAtividade( chave ):
    dadosAtividades = buscaAtividades()
    novosDados = []
    for dadosAtividade in dadosAtividades:
        if dadosAtividade['chave'] != int(chave):
            novosDados.append(dadosAtividade)

    gravaAtividades( novosDados )

    return ''

def pesquisaAtividadeTurma( idTurma ):
    dadosAtividades = buscaAtividades()

    retorno = []
    for dadosAtividade in dadosAtividades:
        if dadosAtividade['turma'] == idTurma:
            retorno.append( dadosAtividade )

    return retorno

def buscascores( chave ):
    dadosAtividades = buscaAtividades()

    for dadosAtividade in dadosAtividades:
        if dadosAtividade['chave'] == chave:
            return dadosAtividade['scores']

    return []

def buscaAtivadadesTurma( idTurma ):
    dadosAtividades = buscaAtividades()

    retorno = []
    ordem = 1
    for dadosAtividade in dadosAtividades:
        if dadosAtividade['turma'] == idTurma:
            dadosAtividade['ordem'] = ordem
            ordem += 1
            retorno.append(dadosAtividade)

    return retorno

def getPesoTotalAtividades( idTurma ):
    dadosAtividades = buscaAtividades()
    dadosCiclosEntregas = cicloEntrega.buscaCiclosEntregaAtivos()

    retorno = []

    for dadosCicloEntrega in dadosCiclosEntregas:
        pesoCiclo = 0
        for dadosAtividade in dadosAtividades:
            if (dadosAtividade['turma'] == idTurma) and (dadosCicloEntrega['chave'] == dadosAtividade['cicloEntrega']):
                pesoCiclo += int(dadosAtividade['peso'])

        pesoPorCiclo = {
            'chaveCicloEntrega':dadosCicloEntrega['chave'],
            'pesoTotalCiclo':pesoCiclo
        }

        retorno.append( pesoPorCiclo )

    retorno = json.dumps( retorno)

    return retorno

def extrair_data(dicionario):
    return datetime.strptime(dicionario['dataEntrega'], '%d/%m/%Y')

def buscascoresAtividades( idTurma ):
    dadosAlunos = turmas.buscaAlunos( idTurma )['matriculado']
    dadosAtiviades = buscaAtivadadesTurma( idTurma )
    dadosAtiviades = sorted(dadosAtiviades, key=extrair_data)
    dadosCicloEntregas = cicloEntrega.buscaCiclosEntregaAtivos()


    retorno = []
    for dadosCicloEntrega in dadosCicloEntregas:
        retornoscoresAluno = []
        atividadesCicloEntrega = []

        ordemAtividade = 1
        possuiAtivdades = False
        for dadosAtividade in dadosAtiviades:
            if dadosAtividade['cicloEntrega'] == dadosCicloEntrega['chave']:
                possuiAtivdades = True
                dadosAtividade['ordemAtividade'] = ordemAtividade
                atividadesCicloEntrega.append(dadosAtividade)
                ordemAtividade += 1
        
        for dadoAluno in dadosAlunos:
            scoresAluno = []
            for dadosAtividade in dadosAtiviades:
                if dadosAtividade['cicloEntrega'] == dadosCicloEntrega['chave']:
                    estadoscores = 'completo'
                    if len(dadosAtividade['scores']) != 0:
                        for notaAtividade in dadosAtividade['scores']:
                            if notaAtividade['RA'] ==  dadoAluno['RA']:
                                dadosNotaAtividade = {
                                    'nota':notaAtividade['nota'],
                                    'chaveAtividade':dadosAtividade['chave']
                                }
                                scoresAluno.append( dadosNotaAtividade )
                                
                    for notaAluno in scoresAluno:
                        if notaAluno == '':
                            estadoscores = 'incompleto'

                    dadosscoresAluno = {
                        "nomeAluno": dadoAluno['nome'],
                        "RA": dadoAluno['RA'],
                        "dadosscores":scoresAluno,
                        "estadoscores": estadoscores
                    }

            possuiscores = 'dadosscoresAluno' in locals()
            if possuiscores:
                retornoscoresAluno.append( dadosscoresAluno )

        scoresPorCicloEntrega = {
            "chaveCicloEntrega":dadosCicloEntrega['chave'],
            "tituloCicloEntrega":dadosCicloEntrega['titulo'],
            "atividadesCicloEntrega":atividadesCicloEntrega,
            "scoresAluno":retornoscoresAluno,
            "possuiAtividades":possuiAtivdades
        }

        retorno.append(scoresPorCicloEntrega)

    return retorno

def salvarscoresAluno( ra, nomeAluno, relacaoscores ):
    dadosAtividades = buscaAtividades()

    novosDadosAtividade = []
    
    for dadosAtidade in dadosAtividades:
        novasscoresAtividades = []
        for notaAtividade in dadosAtidade['scores']:
            if notaAtividade['RA'] == ra:
                notaNaoSubstituida = True
                for relacaoNota in relacaoscores:
                    if int(relacaoNota['chaveAtividade']) == dadosAtidade['chave']:
                        novaNota = {
                            "RA":ra,
                            "nota": relacaoNota['nota'],
                            "nomeAluno": nomeAluno
                        }

                        novasscoresAtividades.append( novaNota )
                        notaNaoSubstituida = False
                if( notaNaoSubstituida ):
                    novasscoresAtividades.append( notaAtividade )
            else:
                novasscoresAtividades.append( notaAtividade )
        
        dadosAtidade['scores'] = novasscoresAtividades
        novosDadosAtividade.append( dadosAtidade )

    gravaAtividades( dadosAtividades )



    return ''

def iniciaAlunoAtividadesTurma( ra, nomeAluno, idTurma):
    dadosAtividades = buscaAtividades()

    novosDadosAtividades = []

    for dadosAtividade in dadosAtividades:
        if(dadosAtividade['turma'] == idTurma):
            notaInicial = {
                "RA": ra,
                "nota": "",
                "nomeAluno": nomeAluno
            }
            possuiscoresNaTurma = False
            for scores in dadosAtividade['scores']:
                if(scores['RA']) == ra:
                    possuiscoresNaTurma = True
            
            if possuiscoresNaTurma == False:
                dadosAtividade['scores'].append( notaInicial )

        novosDadosAtividades.append(dadosAtividade)

    gravaAtividades(novosDadosAtividades)
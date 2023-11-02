import json

def buscaDados():
    with open('dadosJson/baseConfiguracoesSistema.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def buscaTempoLimiteConclusaoCicloEntrega():
    dados = buscaDados()

    return dados['tempoLimiteConclusaoCicloEntrega']
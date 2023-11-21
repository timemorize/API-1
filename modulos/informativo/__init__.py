import json

def buscaDados():
    with open('dadosJson/baseInformativo.json', 'r') as arquivo:
        dados_json = json.load(arquivo)
    return dados_json

def gravaDados(dados):
    with open('dadosJson/baseInformativo.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def salvarDados( dados ):

    novosDados = {
        "titulo": dados['titulo'],
        "texto": dados['texto'],
        "classe": dados['classe'],
        "classeInformativo": dados['classeInformativo'],
        "estado": dados['estado'],
    }

    gravaDados( novosDados )
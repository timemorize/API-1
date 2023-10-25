import json
from flask import jsonify
import random
from modulos import usuarios, grupos, turmas

def buscaCiclosEntrega():
    with open('dadosJson/basCiclosEntrega.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def gravaCiclosEntrega(dados):
    with open('dadosJson/basCiclosEntrega.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)


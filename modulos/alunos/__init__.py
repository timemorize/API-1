import json
from flask import jsonify
import random

def buscaDadosAlunos():
    with open('dadosJson/baseAlunos.json', 'r') as arquivo:
        dadosAlunos = json.load(arquivo)
        dadosAlunos = sorted(dadosAlunos, key=lambda x: x["nome"])

    return dadosAlunos
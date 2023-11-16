import json
import secrets
import string
import base64

def buscaDadosUsuarios():
    with open('dadosJson/baseUsuarios.json', 'r') as arquivo:
        dados_json = json.load(arquivo)
    return dados_json

def gravarDadosUsuarios(dadosUsuarios):
    with open('dadosJson/baseUsuarios.json', 'w') as arquivoUsuarios:
        json.dump(dadosUsuarios, arquivoUsuarios, indent=2)

def cadastrarUsuario(usuario, tipo):
    dadosUsuarios = buscaDadosUsuarios()

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(20))

    #senhaEncriptada = seguranca.encriptar( senha )

    novoUsuario = {
        "usuario": usuario,
        "senha": 'Teste12345678',
        "tipo": tipo,
        "resetSenha": True
    }

    dadosUsuarios.append(novoUsuario)

    gravarDadosUsuarios(dadosUsuarios)

    return senha
    
def redefinirSenha( idUsuario, senha ):
    dadosUsuarios = buscaDadosUsuarios()

    novosDadosUsuarios = []
    for dadosUsuario in dadosUsuarios:
        if dadosUsuario['usuario'] == idUsuario:
            dadosUsuario['senha'] = senha
            dadosUsuario['resetSenha'] = False
        
        novosDadosUsuarios.append(dadosUsuario)

    gravarDadosUsuarios(novosDadosUsuarios)
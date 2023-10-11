from flask import Flask, render_template
from modulos import alunos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('diretor/index.html')

@app.route('/gerenciarAlunos')
def rotaGerenciaAlunos():
    return render_template('diretor/alunos/alunos.html')

@app.route('/gerenciarProfessores')
def rotaGerenciaProfessores():
    return render_template('diretor/professores.html')

@app.route('/gerenciarTurmas')
def rotaGerenciaTurmas():
    return render_template('diretor/turmas.html')

@app.route('/gerenciarGrupos')
def rotaGerenciaGrupos():
    return render_template('diretor/grupos.html')

if __name__ == '__main__':
    app.run(debug=True)

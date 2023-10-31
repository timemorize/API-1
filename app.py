from flask import Flask, render_template, request,jsonify, session
from modulos import atividades,alunos,grupos,turmas, professores, cicloEntrega
import json
import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('diretor/index.html')

@app.route('/gerenciarAlunos')
def rotaGerenciaAlunos():
    dadosAlunos = alunos.buscaDadosAlunos()
    return render_template('diretor/alunos/alunos.html', listaAlunos = dadosAlunos )

@app.route('/cadastrarAluno', methods=['POST'])
def rotaCadastrarAluno():
    return alunos.cadastrarAluno( request.form )

@app.route('/editarAluno', methods=['POST'])
def rotaEditarAluno():
    return alunos.editarAluno( request.form )

@app.route('/excluirAluno/<string:ra>', methods=['POST', 'DELETE'])
def rotaExcluirAluno(ra):
    alunos.excluirAlunos( ra )

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/buscaDadosAluno/<string:ra>', methods=['POST', 'GET'])
def rotaBuscaAluno(ra):
    dadosAluno = alunos.pesquisaAluno(ra)
    return jsonify(
        {
            'result': '1',
            'dadosAluno':dadosAluno
        } )

@app.route('/buscaGruposAluno/<string:ra>', methods=['POST', 'GET'])
def rotaBuscaGruposAluno(ra):
    listaGruposAluno = alunos.buscaGruposAlunos(ra)
    return jsonify(
        {
            'result': '1',
            'gruposInseridos':listaGruposAluno['gruposInseridos'],
            'gruposDisponiveis':listaGruposAluno['gruposDisponiveis']
        } )

@app.route('/buscaAlunosGrupo/<string:identificador>', methods=['POST', 'GET'])
def rotaBuscaAlunosGrupo(identificador):
    listaAlunos = grupos.buscaAlunos(identificador)
    return jsonify(
    {
        'result': '1',
        'alunosNaoInseridos':listaAlunos['naoInseridos'],
        'alunosInseridos':listaAlunos['inseridos']
    } )

@app.route('/modificarGruposAluno', methods=['POST'])
def rotaModificarGruposAlunos():
    listaGruposInseridos = json.loads(request.form['grupos'])
    ra = request.form['ra']
    alunos.inserirGrupos(ra,listaGruposInseridos)

    return ''

@app.route('/buscaTurmasAluno/<string:ra>', methods=['POST', 'GET'])
def rotaBuscaTurmasAluno(ra):
    listaNomeTurmas = alunos.buscaTurmasAlunos(ra)
    return jsonify(
    {
        'result': '1',
        'turmasNaoMatriculadas':listaNomeTurmas['naoMatriculado'],
        'turmasMatriculadas':listaNomeTurmas['matriculado']
    } )

@app.route('/buscaAlunosTurma/<string:identificador>', methods=['POST', 'GET'])
def buscaAlunosTurma(identificador):
    listaAlunos = turmas.buscaAlunos(identificador)
    return jsonify(
    {
        'result': '1',
        'alunosNaoMatriculadas':listaAlunos['naoMatriculado'],
        'alunosMatriculadas':listaAlunos['matriculado']
    } )

@app.route('/modificarTurmasAluno', methods=['POST'])
def rotaModificarTurmasAlunos():
    listaTurmasMatriculadas = json.loads(request.form['turmas'])
    ra = request.form['ra']
    alunos.inserirTurmas(ra,listaTurmasMatriculadas)

    return ''

@app.route('/gerenciarProfessores')
def rotaGerenciaProfessores():
    dadosProfessores = professores.buscaDadosProfessores()
    return render_template('diretor/professores/professores.html',listaProfessores = dadosProfessores)

@app.route('/cadastrarProfessor', methods=['POST'])
def rotaCadastrarProfessor():
    return professores.cadastrarProfessor( request.form )

@app.route('/excluirProfessor/<string:id>', methods=['POST', 'DELETE'])
def rotaExcluirProfessor(id):
    professores.excluirProfessor( id )

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/editarProfessor', methods=['POST'])
def rotaEditarProfessor():
    return professores.editarProfessor( request.form )

@app.route('/buscaTurmasProfessor/<string:identificador>', methods=['POST', 'GET'])
def rotaBuscaListaTurmas(identificador):
    listaTurmas = professores.buscarTurmas(identificador)
    return jsonify(
        {
            'result': '1',
            'listaTurmas':listaTurmas
        } )

@app.route('/gerenciarTurmas')
def rotaGerenciaTurmas():
    dadosTurma = turmas.buscaDadosTurmas()
    dadosProfessores = professores.buscaDadosProfessores()
    return render_template('diretor/turmas/turmas.html', listaTurmas = dadosTurma, listaProfessores = dadosProfessores)

@app.route('/cadastrarTurma', methods=['POST'])
def rotaCadastrarTurma():
    return turmas.cadastrarTurma( request.form )

@app.route('/editarTurma', methods=['POST'])
def rotaEditarTurma():
    return turmas.editarTurma( request.form )

@app.route('/excluirTurma/<string:id>', methods=['POST', 'DELETE'])
def rotaExcluirTurma(id):
    turmas.excluirTurma( id )

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/cadastrarGrupo', methods=['POST'])
def rotaCadastrarGrupo():
    return grupos.cadastrarGrupo( request.form )

@app.route('/excluirGrupo/<string:id>', methods=['POST', 'DELETE'])
def rotaExcluirGrupo(id):
    grupos.excluirGrupo( id )

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/editarGrupo', methods=['POST'])
def rotaEditarGrupo():
    return grupos.editarGrupo( request.form )

@app.route('/gerenciarGrupos')
def rotaGerenciaGrupos():
    dadosGrupos = grupos.buscaDadosGrupos()
    return render_template('diretor/grupos/grupos.html', listaGrupos = dadosGrupos )

@app.route('/gerenciarCicloDeEntrega')
def rotaGerenciarCicloDeEntrega():
    dadosCicloDeEntrega = cicloEntrega.buscaCiclosEntrega()
    dataServidor = datetime.date.today()
    return render_template('diretor/cicloDeEntrega/cicloDeEntrega.html', dataAtual = dataServidor, listaCiclos = dadosCicloDeEntrega )


@app.route('/cadastrarCicloEntrega', methods=['POST'])
def rotaCadastrarCicloEntrega():
    return cicloEntrega.cadastrarCicloEntrega( request.form )


@app.route('/excluirCicloEntrega/<string:chave>', methods=['POST', 'DELETE'])
def rotaExcluirCicloEntrega(chave):
    cicloEntrega.excluirCicloEntrega( chave )

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/editarCicloEntrega', methods=['POST'])
def rotaEditarCicloEntrega():
    return cicloEntrega.editarCicloEntrega( request.form )

@app.route('/minhasTurmas')
def rotaMinhasTurmas():
    dadosTurmas = professores.buscarTurmas( 'PF03' )
    dadosCicloEntrega = cicloEntrega.buscaCiclosEntregaAtivos()
    return render_template('professor/turmas/turmas.html', listaTurmas = dadosTurmas, listaCicloEntrega= dadosCicloEntrega )

@app.route('/cadastrarAtividade', methods=['POST'])
def rotaCadastrarAtividade():
    return atividades.cadastroAtividade( request.form )

@app.route('/buscaAtividadesTurma/<string:identificador>', methods=['GET'])
def rotaBuscaAtividadesTurma(identificador):
    listaAtividades = atividades.pesquisaAtividadeTurma( identificador )
    listaCicloEntregas = cicloEntrega.buscaCiclosEntrega()
    pesoTotalTurma = atividades.getPesoTotalAtividades( identificador )
    return jsonify(
        {
            'result': '1',
            'pesoTotal':pesoTotalTurma,
            'listaAtividades':listaAtividades,
            'listaCiclosEntrega': listaCicloEntregas
        } )

@app.route('/excluirAtividade/<string:identificador>', methods=['POST', 'DELETE'])
def rotaExcluirAtividade(identificador):
    atividades.excluirAtividade(identificador)

    if request.method == 'DELETE':
        return '', 204

    return '', 200

@app.route('/notasProfessor/<string:identificador>', methods=['GET'])
def rotaNotasProfessor(identificador):
    notasAlunos = atividades.buscaNotasAtividades( identificador )
    pesoTotalTurma = atividades.getPesoTotalAtividades( identificador )
    ciclosEntrega = cicloEntrega.buscaCiclosEntregaAtivos()
    return render_template('professor/turmas/notas.html', listaDadosCicloEntrega = notasAlunos, listaCiclosEntrega = ciclosEntrega, pesoTotalTurma = pesoTotalTurma )

@app.route('/salvarNotas', methods=['POST'])
def rotaSalvarNotas():
    ra = request.form['ra']
    notas = json.loads( request.form['dadosNotas'] )
    nomeAluno = request.form['nomeALuno']

    return atividades.salvarNotasAluno(ra,nomeAluno,notas)

@app.route('/buscaDadosAtividade/<string:chave>', methods=['GET'])
def rotaBuscaDadosAtividade(chave):
    dadosAtividade = atividades.pesquisaAtividade( chave )
    return jsonify(
        {
            'result': '1',
            'dadosAtividade':dadosAtividade
        } )

if __name__ == '__main__':
    app.run(debug=True)

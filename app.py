from flask import Flask, render_template, request,jsonify, session, redirect, url_for
from modulos import atividades,alunos,grupos,turmas, professores, cicloEntrega, usuarios, configuracoesSistema, informativo
import json
import datetime



app = Flask(__name__)
app.secret_key = 'c0h0dXQyamJRM0t5RzVjdDVsUEZoSzBRUjdFMGJkMnBmMkZEVlJJS25raz0'

def is_logged_in():
    return 'userID' in session

def verificarDiretor():
    return session['tipo'] != 'diretor'
        

@app.route('/logout')
def logout():
    session.pop('userID', None)
    session.pop('tipo', None)
    return render_template('auth/login.html')

@app.route('/')
def index():
    if not is_logged_in():
        return render_template('auth/login.html')

    if session['tipo'] == 'diretor':
        dadosInformativo = informativo.buscaDados()
        relacaoTurmaAlunos = turmas.buscaQuantidadeTurmasAluno()
        
        relacaoEntidades = configuracoesSistema.relacaoTiposUsuario()
        return render_template('diretor/index.html', dadosInformativo = dadosInformativo, relacaoTurmaAlunos = relacaoTurmaAlunos,relacaoEntidades=relacaoEntidades)

    if session['tipo'] == 'professor':
        dadosTurmas = professores.buscarTurmas( session['userID'] )
        dadosCicloEntrega = cicloEntrega.buscaCiclosEntregaAtivos()
        
        dadosProfessor = professores.pesquisaProfessor( session['userID'])
        nomeProf = dadosProfessor['nome']
        return render_template('professor/turmas/turmas.html', listaTurmas = dadosTurmas, listaCicloEntrega= dadosCicloEntrega, nomeProfessor = nomeProf )
    
    if session['tipo'] == 'aluno':
        dadosAluno = alunos.pesquisaAluno( session['userID'] )
        turmasAluno = alunos.buscaTurmasAlunos( session['userID'] )
        turmasMatriculado = turmasAluno['matriculado']
        mediaMinina = configuracoesSistema.buscaMediaMinima()
        dataAtual = datetime.date.today()
        dataAtual = dataAtual.strftime('%d/%m/%Y')
        dadosInformativo = informativo.buscaDados()

        return render_template('aluno/aluno.html', listaTurmas = turmasMatriculado, nomeAluno = dadosAluno['nome'], raAluno = dadosAluno['RA'], mediaMinina=mediaMinina, dataAtualServidor=dataAtual, dadosInformativo=dadosInformativo )

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    dadosUsuarios = usuarios.buscaDadosUsuarios()
    autentica = False
    tipoUsuario = ""
    resetSenha = ""
    for dadosUsuario in dadosUsuarios:
        if dadosUsuario['usuario'] == username and dadosUsuario['senha'] == password:
            autentica = True
            tipoUsuario = dadosUsuario['tipo']
            resetSenha = dadosUsuario['resetSenha']
            break

    if autentica == True:
        session['userID'] = username
        session['tipo'] = tipoUsuario
         
        return jsonify({'result': '1', 'message': '', 'resetSenha':resetSenha})
    else:
        return jsonify({'result': '', 'message': 'Credenciais inválidas. Tente novamente.'})

@app.route('/redefinirSenha')
def rotaRedefinirSenha():
    return render_template('auth/redefinirSenha.html')

@app.route('/salvarInformativo', methods=['POST'])
def rotaSalvarInformativo():
    informativo.salvarDados( request.form )
    return jsonify(
        {
            'result': '1'
        } )

@app.route('/atualizarSenha', methods=['POST'])
def rotaAtualizarSenha():
    if session['tipo'] == 'diretor':
        identificador = request.form['idUsuario']
    else:
        identificador = session['userID']

    usuarios.redefinirSenha( identificador, request.form['password'] )
    return jsonify(
        {
            'result': '1'
        } )

@app.route('/minhasNotas/<string:idTurma>')
def rotaMinhasNotas(idTurma):
    scoresAluno = alunos.buscaScoreAluno( session['userID'] ,idTurma)
    dadosAluno = alunos.pesquisaAluno( session['userID'] )
    return render_template('aluno/scores.html', listaScoresCicloEntrega = scoresAluno, nomeAluno = dadosAluno['nome'] )

@app.route('/gerenciarAlunos')
def rotaGerenciaAlunos():
    if verificarDiretor():
        return redirect(url_for('logout'))

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
    if verificarDiretor():
        return redirect(url_for('logout'))
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
    if verificarDiretor():
        return redirect(url_for('logout'))
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
    if verificarDiretor():
        return redirect(url_for('logout'))
    dadosGrupos = grupos.buscaDadosGrupos()
    return render_template('diretor/grupos/grupos.html', listaGrupos = dadosGrupos )

@app.route('/gerenciarCicloDeEntrega')
def rotaGerenciarCicloDeEntrega():
    if verificarDiretor():
        return redirect(url_for('logout'))
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

@app.route('/listaCicloEntrega', methods=['GET'])
def rotaListaCicloEntrega():
    return jsonify({
        "result":"1",
        "dadosCicloEntrega":cicloEntrega.buscaCiclosEntrega()
    })

@app.route('/listaProfessores', methods=['GET'])
def rotaListaProfessores():
    return jsonify({
        "result":"1",
        "dadosProfessores":professores.buscaDadosProfessores()
    })

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

@app.route('/scoresProfessor/<string:identificador>', methods=['GET'])
def rotascoresProfessor(identificador):
    scoresAlunos = atividades.buscaScoresAtividades( identificador )
    pesoTotalTurma = atividades.getPesoTotalAtividades( identificador )
    ciclosEntrega = cicloEntrega.buscaCiclosEntregaAtivos()
    dadosProfessor = professores.pesquisaProfessor('PF03')
    nomeProf = dadosProfessor['nome']
    idTurmaGet = identificador
    return render_template('professor/turmas/scores.html', listaDadosCicloEntrega = scoresAlunos, listaCiclosEntrega = ciclosEntrega, pesoTotalTurma = pesoTotalTurma, idTurma = idTurmaGet, nomeProfessor = nomeProf )

@app.route('/buscaCicloEntregaTurma/<string:identificador>', methods=['GET'])
def rotaBuscaCicloEntregaTurma(identificador):
    scoresAlunos = atividades.buscaScoresAtividades( identificador )
    return jsonify(
        {
            'result': '1',
            'scoresAlunos':scoresAlunos
        } )

@app.route('/salvarscores', methods=['POST'])
def rotaSalvarscores():
    ra = request.form['ra']
    scores = json.loads( request.form['dadosscores'] )
    nomeAluno = request.form['nomeALuno']

    return atividades.salvarscoresAluno(ra,nomeAluno,scores)

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

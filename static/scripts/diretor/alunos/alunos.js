$(document).ready(function()
{
	$('#erroAlunos').hide();
	$('#cep').on('input', function()
	{
		const cep = $( '#cep' ).val().replace(/\D/g, '');
		console.log(cep);

		if (cep.length === 8)
		{
			$( '#cep' ).append('-');
		}
		if (cep.length === 8)
		{
			axios.get(`https://viacep.com.br/ws/${cep}/json/`)
			.then(function (response) {
			const data = response.data;
			if (!data.erro)
			{
				$('#logradouro').val(data.logradouro);
				$('#bairro').val(data.bairro);
				$('#cidade').val(data.localidade);
				$('#estado').val(data.uf);
			}
			})
			.catch(function () {
				alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
			});
		}
		else
		{
			$('#logradouro').val( '' );
			$('#bairro').val( '' );
			$('#cidade').val( '' );
			$('#estado').val( '' );
		}
	} );

	$('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();

		console.log(campoPesquisa);
		$(".trAluno").each( function(chave,tarefa)
		{
			let pesquisa = $(this).attr( campoPesquisa ).toUpperCase();
			if( !pesquisa.includes(valorPesquisa ) && valorPesquisa != "" )
			{
				$( this ).hide();
			}
			else
			{
				$( this ).show();   
			}
		});
	} );

	$('.form-control').on('input', function() {
		$(this).removeClass( "is-invalid" );
	} );
} );

function novoAluno()
{
	$('#erroAlunos').hide();
	$('#novoAluno').modal('show');
}

function cadastrarAluno()
{
	let formValido = true;

	$("#novoAluno").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	if( formValido )
	{
		const nome = $('#nome').val();
		const cpf = $('#cpf').val();
		const rg = $('#rg').val();
		const email = $('#email').val();
		const telefone = $('#telefone').val();
		const cep = $('#cep').val();
		const numero = $('#numero').val();
		const logradouro = $('#logradouro').val();
		const bairro = $('#bairro').val();
		const cidade = $('#cidade').val();
		const estado = $('#estado').val();

		$.ajax({
			url: '/cadastrarAluno',
			type: 'POST',
			data:
			{
				nome : nome,
				cpf : cpf,
				rg : rg,
				email : email,
				telefone : telefone,
				cep : cep,
				numero : numero,
				logradouro : logradouro,
				bairro : bairro,
				cidade : cidade,
				estado : estado
			},
			success: function(response)
			{
				$('#novoAluno').modal('hide');
				$('#modlExibirNovaSenha').modal('show');
				$('#novoRa').val( response.raAlunos );
				$('#novaSenha').val( response.senhaAluno );
				$("#modlExibirNovaSenha").attr('origemUsuario','/gerenciarAlunos');
			},
			error: function(error)
			{
				console.log('Erro ao editar o aluno.');
			}
		});
	}
	else
	{
		$('#erroAlunos').show();
	}
}

function editarAluno()
{
	let formValido = true;

	$("#editarAluno").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	  console.log(formValido)
	if( formValido )
	{
		const ra = $('#editarAluno').attr('ra');
		const nome = $('#nomeEditaAluno').val();
		const cpf = $('#cpfEditaAluno').val();
		const rg = $('#rgEditaAluno').val();
		const email = $('#emailEditaAluno').val();
		const telefone = $('#telefoneEditaAluno').val();
		const cep = $('#cepEditaAluno').val();
		const numero = $('#numeroEditaAluno').val();
		const logradouro = $('#logradouroEditaAluno').val();
		const bairro = $('#bairroEditaAluno').val();
		const cidade = $('#cidadeEditaAluno').val();
		const estado = $('#estadoEditaAluno').val();

		$.ajax({
			url: '/editarAluno',
			type: 'POST',
			data:
			{
				ra: ra,
				nome : nome,
				cpf : cpf,
				rg : rg,
				email : email,
				telefone : telefone,
				cep : cep,
				numero : numero,
				logradouro : logradouro,
				bairro : bairro,
				cidade : cidade,
				estado : estado
			},
			success: function(response)
			{
				window.location.href = '/gerenciarAlunos';
			},
			error: function(error)
			{
				console.log('Erro ao editar o aluno.');
			}
		});
	}
	else
	{
		$('#erroAlunos').show();
	}
}

function abreModalEdicaoAlunos( ra )
{
	axios.get('/buscaDadosAluno/' + ra )
	.then(function (response) {
		console.log(response.data.result)
	if( response.data.result )
	{
		$('#raEditaAluno').html("RA: " + ra);
		$('#nomeEditaAluno').val( response.data.dadosAluno.nome );
		$('#cpfEditaAluno').val( response.data.dadosAluno.cpf );
		$('#rgEditaAluno').val( response.data.dadosAluno.rg );
		$('#emailEditaAluno').val( response.data.dadosAluno.email );
		$('#telefoneEditaAluno').val( response.data.dadosAluno.telefone );
		$('#cepEditaAluno').val( response.data.dadosAluno.cep );
		$('#numeroEditaAluno').val( response.data.dadosAluno.numero );
		$('#logradouroEditaAluno').val( response.data.dadosAluno.logradouro );
		$('#bairroEditaAluno').val( response.data.dadosAluno.bairro );
		$('#cidadeEditaAluno').val( response.data.dadosAluno.cidade );
		$('#estadoEditaAluno').val( response.data.dadosAluno.estado );

		$('#editarAluno').modal('show');
		$('#editarAluno').attr('ra',ra);
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function iniciaExcluirAluno(RA)
{
	$('#confirmaExcluirAluno').modal('show');
	$('#botaoExcluir').attr('ra',RA);
}

function excluirAluno()
{
	const ra = $('#botaoExcluir').attr('ra');

	$.ajax({
		url: '/excluirAluno/' + ra,
		type: 'DELETE',
		success: function(response)
		{
			$('#tr' + ra).remove();
			$('#confirmaExcluirAluno').modal('hide');
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}

function definirNovaSenha(identificador)
{
	$('#reseteDeSenhaAluno').modal('show');
	$('#botaoRedefinirSenha').attr('identificador',identificador);
}

function exibirInputSenha( inputId )
{
	const input = $('#' + inputId);
	if (input.attr('type') === 'password') {
		input.attr('type', 'text');
	} else {
		input.attr('type', 'password');
	}
}

function resetPassword()
{
	const novaSenha = $('#password').val();
	const confirmPassword = $('#confirmPassword').val();
	const identificador = $('#botaoRedefinirSenha').attr('identificador');

	const errorDiv = $('#errorDiv');
	if (novaSenha !== confirmPassword)
	{
		errorDiv.text('As senhas não coincidem. Por favor, tente novamente.');
		errorDiv.show();
		return;
	}

	$.ajax({
		url: '/resetarSenha/' + identificador,
		type: 'POST',
		data:
		{
			senha: novaSenha
		},
		success: function(response)
		{
			$('#resetPasswordModal').modal('hide');
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});

  errorDiv.hide();
}

function exibirDadosAluno( ra )
{
	axios.get('/buscaDadosAluno/' + ra )
	.then(function (response) {
	if( response.data.result )
	{
		console.log(response.data.dadosAluno.nome)
		$('#raExibirDados').html(ra);
		$('#nomeExibirDados').html( response.data.dadosAluno.nome );
		$('#cpfExibirDados').html( response.data.dadosAluno.cpf );
		$('#rgExibirDados').html( response.data.dadosAluno.rg );
		$('#emailExibirDados').html( response.data.dadosAluno.email );
		$('#telefoneExibirDados').html( response.data.dadosAluno.telefone );
		$('#cepExibirDados').html( response.data.dadosAluno.cep );
		$('#numeroExibirDados').html( response.data.dadosAluno.numero );
		$('#logradouroExibirDados').html( response.data.dadosAluno.logradouro );
		$('#bairroExibirDados').html( response.data.dadosAluno.bairro );
		$('#cidadeExibirDados').html( response.data.dadosAluno.cidade );
		$('#estadoExibirDados').html( response.data.dadosAluno.estado );

		$('#modalDadosAluno').modal('show');
	}
	})
	.catch(function () {
		alert('Erro ao buscar os dados do aluno');
	});
}

function buscaListaGrupos(ra)
{
	$.ajax({
		url: '/buscaGruposAluno/' + ra,
		type: 'GET',
		success: function(response)
		{
			$('#modalGruposAluno').modal('show');
			$('#modalGruposBotaoSalvar').attr('ra',ra);

			const listaGruposInseridos = $("#listaGruposInseridos");
			listaGruposInseridos.html('');
			response.gruposInseridos.forEach( grupo =>{
				gruposInseridos.push( grupo.identificador );
				listaGruposInseridos.append( '<option value=' + grupo.identificador +'>' + grupo.nome + '</option>' );
			} );

			const listaGruposDisponiveis = $("#listaGruposDisponiveis");
			listaGruposDisponiveis.html('');
			response.gruposDisponiveis.forEach( grupo =>{
				listaGruposDisponiveis.append( '<option value=' + grupo.identificador +'>' + grupo.nome + '</option>' );
			} );

			validaBotoesGerenciarGrupo();
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}

function buscaListaTurmas(ra)
{
	$.ajax({
		url: '/buscaTurmasAluno/' + ra,
		type: 'GET',
		success: function(response)
		{
			console.log(response)
			$('#modalTurmas').modal('show');
			$('#modalTurmasBotaoSalvar').attr('ra',ra);

			const listTurmasMatriculadas = $("#listaTurmasMatriculadas");
			listTurmasMatriculadas.html('');
			if( Array.isArray( response.turmasMatriculadas ) )
			{
				response.turmasMatriculadas.forEach( turma =>{
					turmasMatriculadas.push( turma.identificador );
					listTurmasMatriculadas.append( '<option value=' + turma.identificador +'>' + turma.nome + '</option>' );
				} );
			}

			const listTurmasNaoMatriculadas = $("#listaTurmasNaoMatriculadas");
			listTurmasNaoMatriculadas.html('');
			response.turmasNaoMatriculadas.forEach( turma =>{
				listTurmasNaoMatriculadas.append( '<option value=' + turma.identificador +'>' + turma.nome + '</option>' );
			} );

			validaBotoesGerenciarTurma();
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}


function validaBotoesGerenciarGrupo()
{
	const numeroGruposDisponiveis = $('#listaGruposInseridos option').length;
	const habilitaBotaoRemover = numeroGruposDisponiveis < 1;
	$('#btnRemoveGrupoAluno ').attr('disabled',habilitaBotaoRemover);

	const numeroGruposInseridos = $('#listaGruposDisponiveis option').length;
	const habilitaBotaoAdd = numeroGruposInseridos < 1;
	$('#btnAddGrupoAluno ').attr('disabled', habilitaBotaoAdd );
}

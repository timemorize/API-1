$(document).ready(function()
{
	$('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();

		$(".trProfessor").each( function(chave,tarefa)
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

function novoProfessor()
{
	$('.erroAluno').hide();
	$('#novoProfessor').modal('show');
}

function resetarSenha( identificador )
{
	$('#loginForm').attr('idUsuario',identificador);
	$('#modalResetarSenha').modal('show');
}

function cadastrarProfessor()
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
		const nome = $('#nomeCadastroProfessor').val();
		const email = $('#emailCadastroProfessor').val();

		$.ajax({
			url: '/cadastrarProfessor',
			type: 'POST',
			data:
			{
				nome : nome,
				email : email
			},
			success: function(response)
			{
				$('#novoProfessor').modal('hide');
				$('#modlExibirNovaSenha').modal('show');
				$('#novoRa').val( response.identificador );
				$('#novaSenha').val( response.senhaProfessor );
				$("#modlExibirNovaSenha").attr('origemUsuario','/gerenciarProfessores');
			},
			error: function(error)
			{
				console.log('Erro ao cadastrar professor.');
			}
		});
	}
	else
	{
		$('#erroAlunos').show();
	}
}


function abreModalEdicaoTurma( id, nome, professor )
{
	$('#erroModalEditar').hide();
	$('#identificadorEditarTurma').html( "Identificador: " + id );
	$('#nomeEditarTurma').val( nome );
	$('#professorEditarTurma').val( professor );
	$('#botaoEditarTurma').attr('identificador',id);
	$('#editarTurma').modal('show');
}

function editarTurma()
{
	let formValido = true;

	$("#editarTurma").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	if( formValido )
	{
		const nome = $('#nomeEditarTurma').val();
		const professor = $('#professorEditarTurma').val();
        const id = $('#botaoEditarTurma').attr('identificador');

		$.ajax({
			url: '/editarTurma',
			type: 'POST',
			data:
			{
                identificador: id,
				nome : nome,
				professor : professor
			},
			success: function(response)
			{
				window.location.href = '/gerenciarTurmas';
			},
			error: function(error)
			{
				console.log('Erro ao editar o aluno.');
			}
		});
	}
	else
	{
		$('#erroModal').show();
	}
}

function buscaListaTurmas( identificador, nomeProfessor )
{
    axios.get('/buscaTurmasProfessor/' + identificador )
	.then(function (response) {
	if( response.data.result )
	{
		$('#visualizarTurmas').modal('show');

        $('#nomeProfessorTurmas').html('Turmas do professor ' + nomeProfessor + ":" );
        $('#listaTurmas').html('');
        response.data.listaTurmas.forEach( turma =>{
            $('#listaTurmas').append( '<li class="list-group-item">' + turma.nome + '</li>' );
        } );
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function iniciaExcluirProfessor(identificador)
{
	axios.get('/buscaTurmasProfessor/' + identificador )
	.then(function (response) {
	if( response.data.result )
	{
        if( response.data.listaTurmas.length > 0 )
		{
			$('#erroExcluirTitulo').html('Erro ao excluir Professor');
			$('#erroExcluirTexto').html('Impossível excluir este Professor pois a mesmo está vinculado a alguma turma');
			$('#erroExcluir').modal('show');
		}
		else
		{
			$('#confirmaExcluirProfessor').modal('show');
			$('#botaoExcluir').attr('identificador',identificador);
		}
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function excluirProfessor()
{
    const id = $('#botaoExcluir').attr('identificador');
    console.log(id)

	$.ajax({
		url: '/excluirProfessor/' + id,
		type: 'DELETE',
		success: function(response)
		{
			$('#tr' + id).remove();
			$('#confirmaExcluirProfessor').modal('hide');
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}

function editarProfessor()
{
	let formValido = true;

	$("#editarProfessor").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	if( formValido )
	{
		const nome = $('#nomeEditarProfessor').val();
		const email = $('#emailEditarProfessor').val();
        const id = $('#botaoEditarProfessor').attr('identificador');

		$.ajax({
			url: '/editarProfessor',
			type: 'POST',
			data:
			{
                identificador: id,
				nome : nome,
				email : email
			},
			success: function(response)
			{
				window.location.href = '/gerenciarProfessores';
			},
			error: function(error)
			{
				console.log('Erro ao editar o aluno.');
			}
		});
	}
	else
	{
		$('#erroModal').show();
	}
}

function abreModalEdicaoProfessor( id, nome, email )
{
	$('.erroModalEditar').hide();
	$('#identificadorEditarProfessor').html( "Identificador: " + id );
	$('#nomeEditarProfessor').val( nome );
	$('#emailEditarProfessor').val( email );
	$('#botaoEditarProfessor').attr('identificador',id);
	$('#editarProfessor').modal('show');
}
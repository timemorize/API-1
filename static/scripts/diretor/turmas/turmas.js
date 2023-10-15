$(document).ready(function()
{
	$('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();

		$(".trTurmas").each( function(chave,tarefa)
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

function novaTurma()
{
	$('#erroModal').hide();
	$('#novaTurma').modal('show');
}

function cadastrarTurma()
{
	let formValido = true;

	$("#novaTurma").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	if( formValido )
	{
		const nome = $('#nomeCadastroTurma').val();
		const professor = $('#professorCadastroTurma').val();

		$.ajax({
			url: '/cadastrarTurma',
			type: 'POST',
			data:
			{
				nome : nome,
				professor : professor
			},
			success: function(response)
			{
				window.location.href = '/gerenciarTurmas';
			},
			error: function(error)
			{
				console.log('Erro ao cadastrar turma.');
			}
		});
	}
	else
	{
		$('#erroModal').show();
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

function iniciaExcluirGrupo(identificador)
{
	axios.get('/buscaAlunosTurma/' + identificador )
	.then(function (response) {
	if( response.data.result )
	{
        if( response.data.alunosMatriculadas.length > 0 )
		{
			$('#erroExcluirTitulo').html('Erro ao excluir Turma');
			$('#erroExcluirTexto').html('Impossível excluir esta turma pois a mesmo possui alunos matrículados');
			$('#erroExcluir').modal('show');
		}
		else
		{
			$('#confirmaExcluirTurma').modal('show');
			$('#botaoExcluir').attr('identificador',identificador);
		}
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function buscaListaAlunos( identificador, nomeTurma )
{
    axios.get('/buscaAlunosTurma/' + identificador )
	.then(function (response) {
	if( response.data.result )
	{
		$('#visualizarAlunos').modal('show');

        $('#nomeTurmaTurmas').html('Alunos matrículados na turma de ' + nomeTurma + ":" );
        $('#listaAlunos').html('');
        response.data.alunosMatriculadas.forEach( aluno =>{
			$('#listaAlunos').append( '<li class="list-group-item"> ' + aluno.nome + ' ( RA: ' + aluno.RA + ' ) </li>' );
        } );
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function excluirTurma()
{
    const id = $('#botaoExcluir').attr('identificador');
    console.log(id)

	$.ajax({
		url: '/excluirTurma/' + id,
		type: 'DELETE',
		success: function(response)
		{
			$('#tr' + id).remove();
			$('#confirmaExcluirTurma').modal('hide');
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}
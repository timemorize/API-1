$(document).ready(function()
{
	$('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();

		$(".trGrupo").each( function(chave,tarefa)
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

function novoGrupo()
{
	$('#erroAlunos').hide();
	$('#novoGrupo').modal('show');
}

function cadastrarGrupo()
{
	let formValido = true;

	$("#novoGrupo").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	if( formValido )
	{
		const nome = $('#nome').val();
		const descricao = $('#descricao').val();

		$.ajax({
			url: '/cadastrarGrupo',
			type: 'POST',
			data:
			{
				nome : nome,
				descricao : descricao
			},
			success: function(response)
			{
				window.location.href = '/gerenciarGrupos';
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

function verDescricaoGrupo( label )
{
    const desc = $( label ).attr( 'descCompleta' );
	$('#modalDescricaoGrupo').modal('show');
	$('#descricaoGrupoCompleta').html( desc );
}

function iniciaExcluirGrupo(identificador)
{
	axios.get('/buscaAlunosGrupo/' + identificador )
	.then(function (response) {
	if( response.data.result )
	{
        if( response.data.alunosInseridos.length > 0 )
		{
			$('#erroExcluirTitulo').html('Erro ao excluir Grupo');
			$('#erroExcluirTexto').html('Impossível excluir este grupo pois o mesmo possui alunos vinculados');
			$('#erroExcluir').modal('show');
		}
		else
		{
			$('#confirmaExcluirGrupo').modal('show');
			$('#botaoExcluir').attr('identificador',identificador);
		}
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function excluirGrupo()
{
    const id = $('#botaoExcluir').attr('identificador');
    console.log(id)

	$.ajax({
		url: '/excluirGrupo/' + id,
		type: 'DELETE',
		success: function(response)
		{
			$('#tr' + id).remove();
			$('#confirmaExcluirGrupo').modal('hide');
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}

function abreModalEdicaoGrupo( id, nome, desc )
{
	$('#identificadorEditarGrupo').html( id );
	$('#nomeEditarGrupo').val( nome );
	$('#descricaoEditarGrupo').val( desc );
	$('#botaoSalvarEditarGrupo').attr('identificador',id);
	$('#erroModal').hide();
	$('#editarGrupo').modal('show');
}

function editarGrupo()
{
	let formValido = true;

	$("#editarGrupo").find(".form-control").each(function() {
		if ($(this).val() === '')
		{
		  formValido = false;
		  $(this).addClass( "is-invalid" );
		}
	  });

	if( formValido )
	{
		const nome = $('#nomeEditarGrupo').val();
		const descricao = $('#descricaoEditarGrupo').val();
        const id = $('#botaoSalvarEditarGrupo').attr('identificador');

		$.ajax({
			url: '/editarGrupo',
			type: 'POST',
			data:
			{
                identificador: id,
				nome : nome,
				descricao : descricao
			},
			success: function(response)
			{
				window.location.href = '/gerenciarGrupos';
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

function buscaListaAlunos( identificador, nomeGrupo )
{
    axios.get('/buscaAlunosGrupo/' + identificador )
	.then(function (response) {
	if( response.data.result )
	{
		$('#visualizarAlunos').modal('show');

        $('#nomeGrupos').html('Alunos inseridos no grupos: ' + nomeGrupo );
        $('#listaAlunos').html('');
        response.data.alunosInseridos.forEach( aluno =>{
			$('#listaAlunos').append( '<li class="list-group-item"> ' + aluno.nome + ' ( RA: ' + aluno.RA + ' ) </li>' );
        } );
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}
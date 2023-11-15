$(document).ready(function()
{
    $('#search').on('input', function()
	{
		pesquisaCiclosAluno();
	} );

	pesquisaCiclosAluno();

} );

function visualizaDescricao( descricao, tituloAtividade )
{
	$('#descricaoAtividade').modal('show');
	if( descricao == "<p><br></p>" )
	{
		descricao ='<div class="alert alert-info" role="alert">Atividade sem descrição</div>';
	}
	$('#descAtividade').html(descricao);
	$('#tituloModalAtividade').html("Descrição da Atividade: " + tituloAtividade );
}

function pesquisaCiclosAluno()
{
	const valorPesquisa = $('#search').val().toUpperCase();
	const campoPesquisa = $( '#campoPesquisa' ).val();

	const estado = $( '#filtrarAnoVigente' ).is(':checked');

	const div = $( '#search' ).closest( '.container' );
	const cards = $( div ).find( '.cardScores' )

	$( cards ).each( function(chave,tarefa)
	{
		let pesquisa = $(this).attr( campoPesquisa ).toUpperCase();
		if(
			(!pesquisa.includes(valorPesquisa ) && valorPesquisa != "" ) ||
			(estado == true && $( this ).attr('anoAtual') == 'False') )
		{
			$( this ).hide();
		}
		else
		{
			$( this ).show();   
		}
	});
}
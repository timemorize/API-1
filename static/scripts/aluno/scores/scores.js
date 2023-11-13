$(document).ready(function()
{
    $('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();
        const div = $( this ).closest( '.container' );
        const cards = $( div ).find( '.cardScores' )
		console.log(cards)

		$( cards ).each( function(chave,tarefa)
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
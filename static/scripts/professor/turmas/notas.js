$(document).ready(function()
{
    $('[data-toggle="popover"]').popover();
    $('.notasCicloEntrega').hide();
    $('.notasCicloEntrega:first').show();
    $('.abaCicloEntrega:first').addClass('active');
    $('.inputNota').on('input', function()
    {
        const divTabela = $( this ).closest(".notasCicloEntrega");
        const botaoSalvarNotas = $( divTabela ).find('.botaoSalvarNotas');
        $( botaoSalvarNotas ).attr('disabled',false);
    });

    $('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();
        const div = $( this ).closest( '.notasCicloEntrega' );
        const trs = $( div ).find( '.trNotasAluno' )

		$( trs ).each( function(chave,tarefa)
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

function revisarNotas( botao )
{
    const tr = $( botao ).closest(".trNotasAluno");
    const indicadoresNotas = $( tr ).find('.indicadorNota')

    let td = $( botao ).closest(".trAcaoAluno");

    $( td ).html( '<button class="btn btn-success" onclick="salvarNotas( this )"><i class="fa-solid fa-floppy-disk"></i></button>' )
    $( botao ).hide();

    indicadoresNotas.each( function(index,td)
    {
        const valorNota = $( td ).html();
        $( td ).html( '<input type="text" width="10px" class="form-control inputNota" value="' + valorNota + '">' )
    });
}

function salvarNotas( botao )
{
    let relacaoNotas = [];

    const tr = $( botao ).closest(".trNotasAluno");
    const ra = $( tr ).attr('ra');
    const nomeAluno = $( tr ).attr('nomeAluno');
    const inputsNotas = $( tr ).find('.inputNota')

    let tdAcao = $( botao ).closest(".trAcaoAluno");

    $( tdAcao ).html( '<button class="btn btn-primary" onclick="revisarNotas( this )"><i class="fa-solid fa-pen-to-square"></i></button>' );
    $( botao ).hide();

    inputsNotas.each( function(index,input)
    {
        $( input ).hide();
        const tdNota = $( input ).closest(".indicadorNota");
        const valorNota = $( input ).val();
        $( tdNota ).html( valorNota )
        relacaoNota = {
            'chaveAtividade' : tdNota.attr('chaveAtividade'),
            'nota':valorNota
        }

        relacaoNotas.push( relacaoNota )
    });

    console.log(relacaoNotas)
    $.ajax({
        url: '/salvarNotas',
        type: 'POST',
        data:
        {
            ra : ra,
            dadosNotas : JSON.stringify(relacaoNotas),
            nomeALuno:nomeAluno
        },
        success: function(response)
        {

        },
        error: function(error)
        {
            console.log('Erro ao editar o aluno.');
        }
    });
}

function mudaAbaCicloEntrega( aba )
{
   $('.abaCicloEntrega').removeClass('active');
   $(aba).addClass('active');

    const cicloEntregaSelecionado = $( aba ).attr('cicloEntrega');
    $('.notasCicloEntrega').each( function( index, tabela )
    {
        if( $( tabela ).attr('cicloEntrega') == cicloEntregaSelecionado)
        {
            $( tabela ).show();
        }
        else
        {
            $( tabela ).hide();
        }
    });
}
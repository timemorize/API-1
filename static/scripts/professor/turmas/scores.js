$(document).ready(function()
{
    $('[data-toggle="popover"]').popover();
    $('.scoresCicloEntrega').hide();
    $('.scoresCicloEntrega:first').show();
    $('.abaCicloEntrega:first').addClass('active');
    $('.inputNota').on('input', function()
    {
        const divTabela = $( this ).closest(".scoresCicloEntrega");
        const botaoSalvarscores = $( divTabela ).find('.botaoSalvarscores');
        $( botaoSalvarscores ).attr('disabled',false);
    });

    $('#search').on('input', function()
	{
		const valorPesquisa = $(this).val().toUpperCase();
		const campoPesquisa = $( '#campoPesquisa' ).val();
        const div = $( this ).closest( '.scoresCicloEntrega' );
        const trs = $( div ).find( '.trscoresAluno' )

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

function revisarscores( botao )
{
    const tr = $( botao ).closest(".trscoresAluno");
    const indicadoresscores = $( tr ).find('.indicadorNota')

    let td = $( botao ).closest(".trAcaoAluno");

    $( td ).html( '<button class="btn btn-success" onclick="salvarscores( this )"><i class="fa-solid fa-floppy-disk"></i></button>' )
    $( botao ).hide();

    indicadoresscores.each( function(index,td)
    {
        let valorNota = parseInt( $( td ).html() );
        if( isNaN( valorNota ) )
        {
            valorNota = '';
        }
        $( td ).html( '<input type="text" width="10px" class="form-control inputNota" value="' + valorNota + '">' )
    });
}

function salvarscores( botao )
{
    let relacaoscores = [];

    const tr = $( botao ).closest(".trscoresAluno");
    const ra = $( tr ).attr('ra');
    const nomeAluno = $( tr ).attr('nomeAluno');
    const inputsscores = $( tr ).find('.inputNota')

    let tdAcao = $( botao ).closest(".trAcaoAluno");

    $( tdAcao ).html( '<button class="btn btn-primary" onclick="revisarscores( this )"><i class="fa-solid fa-pen-to-square"></i></button>' );
    $( botao ).hide();

    inputsscores.each( function(index,input)
    {
        $( input ).hide();
        const tdNota = $( input ).closest(".indicadorNota");
        let valorNota = $( input ).val();
        
        relacaoNota = {
            'chaveAtividade' : tdNota.attr('chaveAtividade'),
            'nota':valorNota
        }

        if( valorNota == "" )
        {
            valorNota = '<span class="badge badge-secondary">sem nota</span>';
        }
        $( tdNota ).html( valorNota )

        relacaoscores.push( relacaoNota )
    });

    $.ajax({
        url: '/salvarscores',
        type: 'POST',
        data:
        {
            ra : ra,
            dadosscores : JSON.stringify(relacaoscores),
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
    $('.scoresCicloEntrega').each( function( index, tabela )
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

function downloadCsvCicloEntrega( idTurma )
{
    const dados = [];
    const cicloEntrega = $('#selectCicloDeEntregaFiltro').val();
    const considerarSemTodasscores = $( '#considerarAlunosSemscores' ).is(':checked');

    axios.get('/buscaCicloEntregaTurma/' + idTurma )
	.then(function (response) {
        
	if( response.data.result )
	{
        let dadosGerais = response.data.scoresAlunos;

        const dataCicloEntrega = dadosGerais.filter((dadosGeral) => dadosGeral.chaveCicloEntrega == cicloEntrega);
		const possuiAtividades = dataCicloEntrega[0].possuiAtividades;

        if( possuiAtividades )
        {
            const datascoresAlunos = dataCicloEntrega[0].scoresAluno;
            let data = [];
            datascoresAlunos.forEach((datascoresAluno) => 
            {
                let linhaAlunos = new Object();

                linhaAlunos['nome'] = datascoresAluno.nomeAluno;
                linhaAlunos['ra'] = datascoresAluno.RA;

                let considerarLinha = true;

                datascoresAluno.dadosscores.forEach((notaAluno,index) =>
                {
                    const numeroAtividade = index + 1;
                    if(!considerarSemTodasscores && notaAluno.nota == '')
                    {
                        considerarLinha = false;
                    }

                    if( notaAluno.nota == '' )
                    {
                        notaAluno.nota = 0;
                    }
                    linhaAlunos['Atividade ' + numeroAtividade] = notaAluno.nota;
                })

                if( considerarLinha )
                {
                    data.push( linhaAlunos );
                }
            });
            downloadCSV( data, 'cicloDeEntrega'+idTurma );
            
            $('#erroCicloSemAtividades').hide();
        }
        else
        {
            $('#erroCicloSemAtividades').show();
        }
	}
	})
	.catch(function (e) {
		alert(e);
	});

}

function iniciarExportacaoCsv( idTurma )
{
    $('#modalFiltroCsvscores2').modal('show');
    $('#erroCicloSemAtividades').hide();
}
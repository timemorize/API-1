let quill = '';
$(document).ready(function()
{
    let trAtividade = '';
    quill = new Quill('#descricaoAtivdade', {
        modules: {
        toolbar: [
            [{ header: [1, 2, false] }],
            ['bold', 'italic', 'underline'],
            ['image', 'code-block']
        ]
        },
        placeholder: 'Compose an epic...',
        theme: 'snow'
    });

    $('#selectCicloDeEntrega').on('change', function()
    {
        let dataInicial = $( "#selectCicloDeEntrega option:selected" ).attr('dataInicial');
        let dataFinal = $( "#selectCicloDeEntrega option:selected" ).attr('dataFinal');
        $("#dataEntregaAtividade").show();

        let momentDataInicio = moment(dataInicial, "DD/MM/YYYY");
        let momentDataFim = moment(dataFinal, "DD/MM/YYYY");

        let dataEntregaCicloEntrega = $('#dataEntregaCicloEntrega').datepicker({
          language: 'pt-BR',
          minDate: momentDataInicio.toDate(),
          maxDate: momentDataFim.toDate(),
          format: 'dd/mm/yyyy',
          autoClose: true,
          inline: true,
          onSelect: function(dataFormatada, date, inst) {
            $("#dataEntregaCicloEntregaValor").val( dataFormatada );
          }
        });
    });

	$('#searchTurmas').on('input', function()
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

    $('#pesoAtividade').on('input', function()
    {
        const valorAdicionar = parseInt( $( this ).val() );
        const valorAtual = parseInt( $( this ).attr('pesoatual') );
        let valorFinal = 0;

        if( isNaN( valorAdicionar ) )
        {
            valorFinal = valorAtual;
        }
        else
        {
            valorFinal = valorAdicionar + valorAtual;
        }
        $('#indicadorPesoTotal').html("/ " + valorFinal);
    });
});

function novaAtividade( idTurma, pesoJSON )
{
    const pesoCiclos = JSON.parse(pesoJSON);
    $('#novaAtividade').modal('show');
    $('#novaAtividade').attr( 'idTurma', idTurma );

    $('#selectCicloDeEntrega option').each( function( chave, option )
    {
        const chaveCiclo = $( option ).val()
        if( chaveCiclo )
        {
            const pesoCiclo = pesoCiclos.filter((peso) => peso.chaveCicloEntrega == chaveCiclo);
            $( option ).attr('peso',pesoCiclo[0].pesoTotalCiclo);
        }
    } );

    $("#pesoAtividade").attr('pesoAtividade',pesoCiclos)
    $("#dataEntregaAtividade").hide();
}

function selecionaCIcloEntregaAtividade( select )
{
    const peso = $( "#selectCicloDeEntrega option:selected" ).attr('peso');
    $("#indicadorPesoTotal").html( "/" + peso );
    $('#pesoAtividade').attr('pesoAtual',peso)
}

function cadastrarAtividade()
{
    const peso = $('#pesoAtividade').val();
    const titulo = $('#tituloAtividade').val();
    const dataEntrega = $('#dataEntregaCicloEntregaValor').val();
    const descricao = quill.root.innerHTML;
    const idTurma = $('#novaAtividade').attr( 'idTurma');
    const cicloEntrega = $('#selectCicloDeEntrega').val();
    
    $.ajax({
        url: '/cadastrarAtividade',
        type: 'POST',
        data:
        {
            titulo : titulo,
            dataEntrega : dataEntrega,
            descricao : descricao,
            idTurma:idTurma,
            chaveCicloEntrega:cicloEntrega,
            peso:peso
        },
        success: function(response)
        {
            window.location.href = '/minhasTurmas'
        },
        error: function(error)
        {
            console.log('Erro ao editar o aluno.');
        }
    });
}

function abreModalAtividades( idTurma, nomeTurma )
{
    axios.get('/buscaAtividadesTurma/' + idTurma )
	.then(function (response) {
	if( response.data.result )
	{
        $('#gerenciaAtividade').modal('show');
        $('#tituloModalGerenciarAtividades').html('Gerenciar Atividades da Turma ' + nomeTurma );

        $('#abasCiclosEntrega').html('');
        const ciclosEntrega = response.data.listaCiclosEntrega;
            let primerioCiclo = 'active';
            ciclosEntrega.forEach( ciclo =>{
                if( ciclo.estado == 'ativo' )
                {
                    $('#abasCiclosEntrega').append('<li class="nav-item"><a chave="' + ciclo.chave + '" class="nav-link abaAtividades ' + primerioCiclo + '" onClick="mudaSemestreGerenciaAtividades( this )">' + ciclo.titulo + '</a></li>');
                    primerioCiclo = ''
                }
            });

        $('#tbodyAtividades').html('');
        const pesoCiclos = JSON.parse( response.data.pesoTotal );
        const atividades = response.data.listaAtividades;
            atividades.forEach( atividade =>{

            const pesoCiclo = pesoCiclos.filter((peso) => peso.chaveCicloEntrega == atividade.cicloEntrega);
            const pesoTotal = pesoCiclo[0].pesoTotalCiclo ?? 0 ;
            const porcentagem = parseInt( 100 * atividade.peso / pesoTotal);
            htmlTabela = '';

            htmlTabela += '<tr class="trAtividadeCicloEntrega" idAtividade = ' + atividade.chave + ' cicloEntrega = ' + atividade.cicloEntrega + '>';
            htmlTabela += '    <td>' + atividade.titulo + '</td>';
            htmlTabela += '    <td>' + atividade.peso + '/' + pesoTotal + ' ('+ porcentagem +'%)' +'</td>';
            htmlTabela += '    <td>' + atividade.dataEntrega + '</td>';
            htmlTabela += '    <td>';
            htmlTabela += '        <button type="button" disabled class="btn btn-success" chave="' + atividade.chave + '"onclick="iniciaEditaModal( this )"><i class="fas fa-edit"></i></button>';
            htmlTabela += '        <button type="button" class="btn btn-danger" chave="' + atividade.chave + '"onclick="iniciarExcluirAtividade( this )"><i class="fa-solid fa-trash"></i></button>';
            htmlTabela += '    </td>';
            htmlTabela += '</tr>';

            $('#tbodyAtividades').append(htmlTabela);
        } );

        const primeiraAba = $('.abaAtividades:first');
        mudaSemestreGerenciaAtividades( primeiraAba );
	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}

function mudaSemestreGerenciaAtividades( aba )
{
    $('.nav-link').removeClass("active");
    $( aba ).addClass("active");
    const cicloEntregaSelecionado = $( aba ).attr('chave');

    $('#tabelaAtividadeCicloEntrega').hide();
    $('#semAtividadesCicloEntrega').show();

    $('.trAtividadeCicloEntrega').each( function( chave,tr )
    {
        const cicloEntregaTabela =  $( tr ).attr('cicloEntrega')
        if( cicloEntregaTabela !=  cicloEntregaSelecionado )
        {
            $( tr ).hide();
        }
        else
        {
            $( tr ).show();
            $('#tabelaAtividadeCicloEntrega').show();
            $('#semAtividadesCicloEntrega').hide();
        }
    } );
}

function iniciarExcluirAtividade( botaoExcluir )
{
    $('#confirmaExcluirAtividade').modal('show');
    trAtividade = $( botaoExcluir ).closest( '.trAtividadeCicloEntrega' );
}

function excluirAtividade()
{
    const identificador = $( trAtividade ).attr('idAtividade')
    console.log(identificador)
    $('#confirmaExcluirAtividade').modal('hide');

    $.ajax({
		url: '/excluirAtividade/' + identificador,
		type: 'DELETE',
		success: function(response)
		{
            $( trAtividade ).remove();
			$('#confirmaExcluirAtividade').modal('hide');
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}

function iniciaEditaModal( botao )
{
    const idAtividade = $( botao ).attr( 'chave' );

    axios.get('/buscaDadosAtividade/' + idAtividade )
	.then(function (response) {
		dadosTurma = response.data;
	if( dadosTurma.result )
	{
        $('#editaAtividade').modal('show');
        $('#editaAtividade').attr( 'idAtividade', idAtividade );


	}
	})
	.catch(function () {
		alert('Erro ao buscar o CEP. Tente novamente mais tarde.');
	});
}


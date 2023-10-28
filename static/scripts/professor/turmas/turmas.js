$(document).ready(function()
{
    let trAtividade = '';
    var quill = new Quill('#descricaoAtivdade', {
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
});

function novaAtividade( idTurma )
{
    $('#novaAtividade').modal('show');
    $('#novaAtividade').attr( 'idTurma', idTurma );
    $("#dataEntregaAtividade").hide();
}

function cadastrarAtividade()
{
    const titulo = $('#tituloAtividade').val();
    const dataEntrega = $('#dataEntregaCicloEntregaValor').val();
    const descricao = $('#descricaoAtivdade').val();
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
            chaveCicloEntrega:cicloEntrega
        },
        success: function(response)
        {
            $('#novaAtividade').modal('hide');
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
        const atividades = response.data.listaAtividades;
            atividades.forEach( atividade =>{
            htmlTabela = '';

            htmlTabela += '<tr class="trAtividadeCicloEntrega" idAtividade = ' + atividade.chave + ' cicloEntrega = ' + atividade.cicloEntrega + '>';
            htmlTabela += '    <td>' + atividade.chave + '</td>';
            htmlTabela += '    <td>' + atividade.titulo + '</td>';
            htmlTabela += '    <td>' + atividade.dataEntrega + '</td>';
            htmlTabela += '    <td>';
            htmlTabela += '        <button type="button" class="btn btn-success" chave="' + atividade.chave + '"onclick="editarAtividade( this )"><i class="fas fa-edit"></i></button>';
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


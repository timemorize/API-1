function novoCicloEntrega()
{
	$('#novoCicloEntrega').modal('show');
}

function inciarExcluirCicloEntrega( chave )
{
	$('#excluirCicloEntrega').modal('show');
  $('#excluirCicloEntrega').attr('chave',chave);
}

function excluirCicloEntrega()
{
  const chaveCicloEntrega = $('#excluirCicloEntrega').attr('chave');

  $.ajax({
		url: '/excluirCicloEntrega/' + chaveCicloEntrega,
		type: 'DELETE',
		success: function(response)
		{
			window.location.href = '/gerenciarCicloDeEntrega';
		},
		error: function(error)
		{
			console.error('Erro ao excluir elemento:', error);
		}
	});
}

function iniciaEditarCicloEntrega( chave, dataInicial, dataFinal, titulo )
{
	$('#editarCicloEntrega').modal('show');
  $('#editarCicloEntrega').attr('chave', chave);
  $('#tituloCicloEntregaEditar').val( titulo );

  var startDate = moment(dataInicial, "DD-MM-YYYY");
  var endDate = moment(dataFinal, "DD-MM-YYYY");

  $('#datePickerEditar').datepicker({
    language: 'pt-BR',
    inline: true,
    range: true,
    multipleDatesSeparator: ' até ',
    onSelect: function (formattedDate, date, inst) {
      startDate = moment(inst.date1);
      endDate = moment(inst.date2);
      dataInicialEditar = moment( date[0] ).format('DD/MM/YYYY') ?? '';
      dataFinalEditar = moment( date[1] ).format('DD/MM/YYYY') ?? '';
      $("#indicadorDataEditar").html( formattedDate );
    }
  });

  $('#datePickerEditar').data('datepicker')
    .selectDate([startDate.toDate(), endDate.toDate()]);
}

function salvarAlteracaoCicloEntrega()
{
  const tituloCicloEntrega = $('#tituloCicloEntregaEditar').val();
  const chaveCicloEntrega = $('#editarCicloEntrega').attr('chave');

  $.ajax({
      url: '/editarCicloEntrega',
      type: 'POST',
      data:
      {
          chave: chaveCicloEntrega,
          titulo: tituloCicloEntrega,
          dataInicial : dataInicialEditar,
          dataFinal : dataFinalEditar
      },
      success: function(response)
      {
          window.location.href = '/gerenciarCicloDeEntrega';
      },
      error: function(error)
      {
          console.log('Erro ao cadastrar ciclo de entrega');
      }
  });
}

function salvarCicloEntrega()
{
    const tituloCicloEntrega = $('#tituloCicloEntrega').val();
    $.ajax({
        url: '/cadastrarCicloEntrega',
        type: 'POST',
        data:
        {
            titulo: tituloCicloEntrega,
            dataInicial : dataInicial,
            dataFinal : dataFinal
        },
        success: function(response)
        {
            window.location.href = '/gerenciarCicloDeEntrega';
        },
        error: function(error)
        {
            console.log('Erro ao cadastrar ciclo de entrega');
        }
    });
}

let dataInicial = '';
let dataFinal = '';

let dataInicialEditar = '';
let dataFinalEditar = '';

$(document).ready(function()
{
    $('#search').on('input', function()
    {
      const valorPesquisa = $(this).val().toUpperCase();
      const campoPesquisa = $( '#campoPesquisa' ).val();
      filtrarCiclosEntrega( campoPesquisa,valorPesquisa );
    } );

    var datePicker = $('#datePicker').datepicker({
      language: 'pt-BR',
      autoClose: true,
      range: true,
      autoClose: true,
      inline: true,
      multipleDatesSeparator: ' até ',
          onSelect: function(formattedDate, date, inst)
          {
            dataInicial = moment( date[0] ).format('DD/MM/YYYY') ?? '';
            dataFinal = moment( date[1] ).format('DD/MM/YYYY') ?? '';
            $("#indicadorData").html( formattedDate );
          }
    });
  });

  $(document).ready(function(){
    var datePicker = $('#datePickerx').datepicker({
      language: 'pt-BR',
      dateFormat: 'dd-mm-yyyy',
      autoClose: true,
      range: true,
      multipleDatesSeparator: ' - ',
      onSelect: function(formattedDate, date, inst) {
        var selectedDates = inst.selectedDates;
        if (selectedDates.length === 2) {
          var startDate = selectedDates[0];
          var endDate = selectedDates[1];
          $('#startDate').val(startDate.toLocaleDateString('pt-BR'));
          $('#endDate').val(endDate.toLocaleDateString('pt-BR'));
        } else {
          $('#startDate').val('');
          $('#endDate').val('');
        }
      }
    });
  });

function filtraDesativados( check )
{
  const valorPesquisa = $( '#search').val().toUpperCase();
  const campoPesquisa = $( '#campoPesquisa' ).val();
  filtrarCiclosEntrega( campoPesquisa,valorPesquisa );
}

function filtrarCiclosEntrega(campoPesquisa,valorPesquisa)
{
  const considerarAtivados = $( '#filtrarAtivados' ).is(':checked');

  $(".trcicloDeEntrega").each( function(chave,tarefa)
  {
    let pesquisa = $(this).attr( campoPesquisa ).toUpperCase();
    const ocultarDesativado = $(this).attr('estado') == 'desativado' && !considerarAtivados
    if( (!pesquisa.includes(valorPesquisa ) && valorPesquisa != "" ) || ocultarDesativado )
    {
      $( this ).hide();
    }
    else
    {
      $( this ).show();   
    }
  });
}

function downloadCsvCicloEntrega(){
  axios.get('/listaCicloEntrega')
  .then(function (response) {
    
  if( response.data.result )
  {
    const dadosCicloEntrega =  response.data.dadosCicloEntrega;
    downloadCSV( dadosCicloEntrega, 'Relacao_Alunos');
  }
  })
  .catch(function (e) {
    alert(e);
  });
}
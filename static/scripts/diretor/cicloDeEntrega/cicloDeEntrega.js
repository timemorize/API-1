function novoSemestre()
{
	$('#novoCicloEntrega').modal('show');
}

function salvarSemestre()
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
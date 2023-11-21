$(document).ready(function()
{

} );

function mudaTipoAviso( select )
{
    const card = $('#cardInformativo');
    const classe = $( select ).val();
    $( card ).removeClass();
    $( card ).addClass( classe )
}

function salvarInformativo()
{
    let titulo = $('#tituloInformativo').val();
    let texto = $('#textoInformativo').val();
    let classe = $('#tipoAlerta').val();
    let classeInformativo = $('#tipoAlerta').find("option:selected").attr('classeAlerta');
    console.log(classeInformativo)
    let estado = $( '#estadoInformativo' ).is(':checked') ? 'ativo' : 'desativo';

    $.ajax({
        url: '/salvarInformativo',
        type: 'POST',
        data:
        {
            titulo : titulo,
            texto : texto,
            classe : classe,
            classeInformativo : classeInformativo,
            estado : estado
        },
        success: function(response)
        {
            window.location.href = '/';
        },
        error: function(error)
        {
            console.log('Erro ao cadastrar professor.');
        }
    });
}
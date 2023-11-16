$(document).ready(function() {
  $('#erroLogin').hide();
  $('#loginForm').submit(function(e)
  {
    e.preventDefault();

    const username = $('#username').val();
    const password = $('#password').val();

    $.ajax({
      url: '/login',
      type: 'POST',
      data: { username: username, password: password },
      success: function(response)
      {
        if( response.result )
        {
          if( response.resetSenha )
          {
            window.location.href = '/redefinirSenha';
          }
          else
          {
            window.location.href = '/';
          }
        }
        else
        {
          $('#erroLogin').show();
          $('#erroLogin').html(response.message);
        }
      },
      error: function(error)
      {  
        $('#erroLogin').show();
        $('#erroLogin').html('Erro ao tentar fazer login.');
      }
    });
  });
});

function visualizarSenha()
{
    const input = $( "#password");
    if (input.attr('type') === 'password') {
        input.attr('type', 'text');
    } else {
        input.attr('type', 'password');
    }
}

function login()
{

}
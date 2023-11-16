$(document).ready(function() {
    $('#erroLogin').hide();

    $('#loginForm').submit(function(e)
    {
      
      $('#erroLogin').show();
      $('#erroLogin').html('');

      e.preventDefault();
  
      const password = $('#password').val();
      const confirPassword = $('#confirPassword').val();

      if( password != confirPassword )
      {
          $('#erroLogin').show();
          $('#erroLogin').html('Confirmação de senha diferente da senha');

          return false;
      }
  
      $.ajax({
        url: '/atualizarSenha',
        type: 'POST',
        data: { password: password },
        success: function(response)
        {
          window.location.href = '/';
        },
        error: function(error)
        {  
          $('#erroLogin').show();
          $('#erroLogin').html('Erro ao tentar fazer login.');
        }
      });
    });
  
  });
  
  function visualizarSenha( inputId )
  {
      const input = $( "#" + inputId );
      if (input.attr('type') === 'password') {
          input.attr('type', 'text');
      } else {
          input.attr('type', 'password');
      }
  }
  
  function login()
  {

  }
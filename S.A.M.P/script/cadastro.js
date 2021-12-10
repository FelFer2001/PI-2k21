$(document).ready(function() {

   $("#verificacao").click(function(){
      $("#meucadastro").addClass("was-validated");
   });
   // Função de envio de cadastro para o banco de dados
   $("#meucadastro").submit(function(e) {
      //Cancela a funcionalidade de envio padrão do submit
      e.preventDefault();
      // Variavel que define se tem algum erro ou não
      var semErros = true
      // Recuperando dados da página
      NomeCompleto = $("#inputNome").val();
      DtNascimento = $("#inputData").val();
      Genero = $('input[name="genero"]:checked').val();
      Cpf = $("#inputCpf").val();
      Cep = $("#inputCep").val();
      Complemento = $("#inputComplemento").val();
      NomePai = $("#InputPai").val();
      NomeMae = $("#InputMae").val();
      Email = $("#inputEmail").val();
      Senha = $("#inputSenha").val();
      Tipo_Sanguineo = $("#Tipo_Sanguineo").val();
      DoencaHereditaria = $('[name="Doenca"]').val();
      Sintomas = $('[name="Sintomas"]').val();
      // Validação do Email
      if (Email != $("#inputConfirEmail").val()){
         semErros = false
         // Mostrando mensagem de aviso
         $("#EmailErrado").removeClass("invisivel");
      }
      // Validação da Senha
      if (Senha != $("#inputConfirSenha").val()){
         semErros = false
         // Mostrando mensagem de aviso
         $("#SenhaErrada").removeClass("invisivel");
      }
      // Caso não tenha erros, procede com o commit
      if(semErros){
         // transforma os dados em um arquivo json
         var dados = JSON.stringify({
            NomeCompleto: NomeCompleto, DtNascimento: DtNascimento, Genero: Genero, Cpf: Cpf, Cep: Cep, Complemento: Complemento, 
            NomePai: NomePai, NomeMae: NomeMae, Email: Email, Senha: Senha, Tipo_Sanguineo: Tipo_Sanguineo, DoencaHereditaria: DoencaHereditaria,
            Sintomas: Sintomas
         });
         // Faz o envio por meio do método ajax
         $.ajax({
            url: 'http://localhost:5000/incluir_paciente', // Endereço do banco de dados
            type: 'POST', // O tipo POST é o de envio, enquanto GET é o de recuperação de dados
            dataType: 'json', // Tipo de arquivo que será enviado
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: pessoaIncluida, // Mostra uma mensagem indicando o sucesso na operação e limpa o formulário
            error: erroAoIncluir // Caso de erro, mostra uma mensagem indicando o tal
         });
         // Função de sucesso
         function pessoaIncluida (retorno) {
            // Se o back-end retornar ok, procede com tais funções
            if (retorno.resultado == "ok") { 
               // Alerta que teve sucesso
               alert("Pessoa incluída com sucesso!");
               // Redireciona para outra página
               location.href = "index.html";
            } else if (retorno.resultado == "CPF"){
               // informar mensagem de erro
               alert("CPF Repetido");
            }            
         }
         // Função de erro
         function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ": " + retorno.detalhes);
         }
      }
   });
});
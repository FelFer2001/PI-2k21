$(document).ready(function() {
	// Caso o usuário seja um cidadão, mostra funções exclusivas
	if (sessionStorage.Type == 'cidadao'){
		$("#FunCidadao").removeClass("invisivel");
		$(".profile_content").removeClass("invisivel");
		$(".login_content").addClass("invisivel");
		// Adiciona dados superficiais no menu
        $('.Nome').append(sessionStorage.NomeCompleto);
        $('.trabalho').append(sessionStorage.Type);
	}
	// função que abre e fecha o menu
	// Caso tenha um click no botao ele executará a função
    $("#botao").click(function(){
		// Adiciona a classe no menu_lateral caso não tenha, caso tenha, remove dele
		$(".menu_lateral").toggleClass("active");
	});
	$("#logar").submit(function(e){
		e.preventDefault(); // Cancela as funções padrões de submit
		// Pega os dados necessários
		Email = $("#loginEmail").val();
      	Senha = $("#loginSenha").val();
		// Cria a variável que será mandada para o back-end no formato json
		var dados = JSON.stringify({
            Email: Email, Senha: Senha
        });
		// Enviando os dados pelo método Ajax
		$.ajax({
            url: 'http://localhost:5000/login', // Endereço do banco de dados
            type: 'POST', // O tipo POST é o de envio, enquanto GET é o de recuperação de dados
            dataType: 'json', // Tipo de arquivo que será enviado
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: executarLogin, // Mostra uma mensagem indicando o sucesso na operação e adiciona os dados do usuário na sessionStorage
            error: erroAoLogar // Caso de erro, mostra uma mensagem indicando o tal
        });
		function executarLogin (retorno) {
            // Se o back-end retornar ok, procede com tais funções
			if (retorno.resultado == "ok") { 
               // Alerta que teve sucesso
			   	alert("Resultado: " +retorno.resultado + " Detalhes: " + retorno.detalhes);
				// salva os dados em uma sessão
				sessionStorage.Id = retorno.usuario.Id;
				sessionStorage.NomeCompleto = retorno.usuario.NomeCompleto;
				sessionStorage.DtNascimento = retorno.usuario.DtNascimento;
				sessionStorage.Genero = retorno.usuario.Genero;
				sessionStorage.Cpf = retorno.usuario.Cpf;
				sessionStorage.Email = retorno.usuario.Email;
				sessionStorage.Cep = retorno.usuario.Cep;
				sessionStorage.Complemento = retorno.usuario.Complemento;
				sessionStorage.temComorbidades = retorno.usuario.temComorbidades;
				sessionStorage.TipoComorbidade = retorno.usuario.TipoComorbidade;
				sessionStorage.Type = retorno.usuario.Type;
				location.reload(); // Recarrega a página
            } else {
               // informar mensagem de erro
			   $("#LoginIncorreto").removeClass("invisivel");
               }            
        }
		function erroAoLogar (retorno) {
            // informar mensagem de erro
			alert("Erro: " +retorno.resultado + " Detalhes: " + retorno.detalhes);
         }
	});
	$("#log_out").click(function(){
		// Fazendo com que as informações do individuo desapareça quando clicar em logout
		$(".profile_content").addClass("invisivel");
		$(".login_content").removeClass("invisivel");
		sessionStorage.clear(); // Limpa os dados da sessionSotrage
		location.href = "index.html"; // Redireciona para outra página
	});
});
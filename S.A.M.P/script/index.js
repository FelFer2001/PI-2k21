$(document).ready(function() {	  
	// Sistema de slides
	// Adicionando contador de slides
	var contador = 1;
	// Adicionando função de intervalo entre acontecimentos
	// setInterval = função que faz com o que está dentro dela aconteça de tempo em tempo 
	setInterval(function(){
		// Fazendo com que o radio seja marcado 
		$('#radio' + contador)[0].checked = true;
		// Somando +1 na variavel contador
		contador++;
		// Caso o contador tenha atingindo o maximo de slides possiveis ele entra nessa condição
		if(contador > 4){
			// Reporta a variável ao valor inicial
			contador = 1;
		}
	}, 5000); // intervalo de tempo de acontecimento dessa função
});
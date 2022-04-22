
//import { lerCookie } from "./cookie";

function criarCookie(nome, valor)
{
	var dataExpira = "expires= Tue, 01 Jan 2022 12:00;00 UTC";
	document.cookie = nome + "=" + valor + "; " + dataExpira;
}

function lerCookie(nome) {
	var vNome = nome + "=";
	var ca = document.cookie.split(';');
	for(var i = 0; i < ca.length; i++)
	{
		var c = ca[i];
		while(c.charAt(0) == ' ')
		{
			c = c.substring(1);
		}

		if(c.indexOf(vNome) == 0)
			return c.substring(vNome.length, c.length);
		
	}
	return "";
}

var entrar = document.querySelector("#entrar");

entrar.addEventListener("click", function (e) {
	e.preventDefault();
	var email = String(document.querySelector("#email").value);
	var senha = String(document.querySelector("#senha").value);

	var verificacao = lerCookie("user");
	verificacao = verificacao.split(':');
	if(verificacao != "")
		if(email == verificacao[0])
			if(!(senha == verificacao[2]))
				alert("Senha incorreta!");
			else
			{
				var novosDados = "";
				for(var i = 0; i < (verificacao.length) - 1; i++)
					novosDados += verificacao[i] + ":";
				novosDados += "true";

				criarCookie("user", novosDados);
				alert("Login realizado com sucesso!");
			}
		else
			alert("Email não encontrado!");
	else
		alert("Email não encontrado!");
})

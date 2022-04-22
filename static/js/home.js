
function criarCookie(nome, valor, expira)
{
	var dataExpira = expira;
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

function logado()
{
	var autenticacao = lerCookie("user");
	if(autenticacao != "")
	{
		autenticacao = autenticacao.split(':');
		if(autenticacao[3] == 'true')
		{
			var nome = document.getElementById("linklogin");
			var saudacao = document.getElementById("saudacao");

			nome.innerHTML = autenticacao[1];
			saudacao.innerHTML = "Seja bem vindo(a), " + autenticacao[1] + "!";

		}
	}
}
logado();

var deslogar = document.querySelector("#linklogin");

deslogar.addEventListener("click", function () {
	var dados = lerCookie("user");
	if(dados != "")
	{
		dados = dados.split(':');

		var novosDados = "";

		for(var i = 0; i < (dados.length) - 1; i++)
			novosDados += dados[i] + ":";
		novosDados += "false";
		criarCookie("user", novosDados);
	}

})

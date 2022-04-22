

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

function validarSenha(senha1, senha2)
{
	if(senha1 == senha2)
	{
		return false;
	}
	else
		return true;
}

function validarCadastro(email)
{
	var verificacao = lerCookie("user");
	if(verificacao != "")
	{
		verificacao = verificacao.split(':');
		return (verificacao[0] == email) ? true : false;
	}
	return false;
}

var cadastrar = document.querySelector("#cadastrar");

cadastrar.addEventListener("click", function (e) {
	e.preventDefault();

	var nome  = String(document.querySelector("#login").value);
	var email = String(document.querySelector("#email").value);
	var senha1 = String(document.querySelector("#senha1").value);
	var senha2 = String(document.querySelector("#senha2").value);

	if(validarSenha(senha1, senha2))
		alert("As senhas não são iguais. Tente novamente.");
	else
	{
		if(validarCadastro(email))
		{
			alert("Email já cadastrado. Tente fazer login.");
		}
		else
		{
			var valor = "" + email + ":" + nome + ":" + senha1 + ":" + "true";
			criarCookie("user", valor);
			alert("Cadastro realizado com sucesso!");
		}
	}
})

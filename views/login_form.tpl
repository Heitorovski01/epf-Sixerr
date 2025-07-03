<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Sixerr</title>
    <link rel="stylesheet" type="text/css" href="/static/css/register_style.css">
</head>
<body>
    <div class="form-container">
        <img src="/static/img/logo.png" class="form-logo"/>
        <h1>Acesse sua Conta</h1>
        <p>Bem-vindo de volta!</p>

        % if defined('error'):
            <p style="color: red; font-weight: bold;">{{error}}</p>
        % end

        <form action="/login" method="post">
            <div>
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div>
                <label for="password">Senha:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <br>
            <button type="submit">Entrar</button>
        </form>

        <div class="login-link">
             <p>Não tem uma conta? <a href="/register">Cadastre-se</a></p>
        </div>

    </div>
</body>
</html>
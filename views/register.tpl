<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro - Sixerr</title>
    </head>
<body>
    <h1>Crie sua conta</h1>
    <form action="/register" method="post">
        <label for="name">Nome:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Senha:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <label for="user_type">Eu quero:</label><br>
        <select name="user_type" id="user_type">
            <option value="comprador">Contratar um serviço</option>
            <option value="vendedor">Vender um serviço</option>
        </select><br><br>

        <button type="submit">Cadastrar</button>
    </form>
</body>
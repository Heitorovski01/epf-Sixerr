%rebase('layout', title=title, style=style)

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crie sua Conta - Sixerr</title>
    <link rel="stylesheet" type="text/css" href="/static/css/register_style.css">
    <style>
        #seller-fields {
            display: none;
        }
    </style>
</head>
<body>

    <div class="form-container">
        <img src="/static/img/logo.png" class="form-logo"/>
        <h1>Crie sua Conta</h1>

        <p>Comece a vender ou contratar serviços hoje mesmo.</p>

        <form action="/register" method="post">
            
            <div>
                <label for="name">Nome Completo:</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div>
                <label for="email">Seu melhor E-mail:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div>
                <label for="password">Crie uma Senha:</label>
                <input type="password" id="password" name="password" required>
            </div>
            
            <div>
                <label for="user_type_select">Qual seu objetivo na plataforma?</label>
                <select name="user_type" id="user_type_select">
                    <option value="comprador" selected>Quero contratar serviços</option>
                    <option value="vendedor">Quero vender meus serviços</option>
                </select>
            </div>
            
            <div id="seller-fields">
                <hr>
                <h3>Complete seu Perfil de Vendedor</h3>
                <div>
                    <label for="username">Apelido (URL pública):</label>
                    <input type="text" id="username" name="username">
                </div>
                <div>
                    <label for="headline">Título Profissional:</label>
                    <input type="text" id="headline" name="headline">
                </div>
                <div>
                    <label for="bio">Biografia:</label>
                    <textarea id="bio" name="bio" rows="4"></textarea>
                </div>
                <div>
                    <label for="skills">Habilidades (separadas por vírgula):</label>
                    <input type="text" id="skills" name="skills">
                </div>
                <div>
                    <label for="location">Sua Localização:</label>
                    <input type="text" id="location" name="location">
                </div>
            </div>
            <br>
            <button type="submit">Registrar</button>
        </form>

        <div class="login-link">
             <p>Já tem uma conta? <a href="/login">Faça Login</a></p>
        </div>

    </div> <script>
        document.addEventListener('DOMContentLoaded', function() {
            const userTypeSelect = document.getElementById('user_type_select');
            const sellerFields = document.getElementById('seller-fields');

            userTypeSelect.addEventListener('change', function() {
                if (this.value === 'vendedor') {
                    sellerFields.style.display = 'block';
                } else {
                    sellerFields.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>

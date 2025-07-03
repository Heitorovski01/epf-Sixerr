<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>{{title or 'Bem-Vindo'}} - Sixerr</title>
    
    <link rel="stylesheet" href="/static/css/layout_style.css" />
    
    % if defined('style'):
        <link rel="stylesheet" href="/static/css/{{style}}.css" />
    % end
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>

    <header class="main-header">
        <div class="container">
            <a href="/" class="logo">
                <img src="static/img/logo.png" alt="Logo Sixerr">
                <span>Sixerr</span>
            </a>
            </div>
    </header>

    <main class="main-content">
        {{!base}}
    </main>

    <footer class="main-footer">
        <div class="container">
            <p>&copy; 2025 Sixerr. Todos os direitos reservados.</p>
        </div>
    </footer>

</body>
</html>
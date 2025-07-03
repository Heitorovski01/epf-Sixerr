<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{get('title', 'Sixerr Marketplace')}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">Sixerr</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    % if defined('usuario') and usuario:
                        <li class="nav-item">
                            <span class="navbar-text me-3">
                                Olá, {{usuario.nome}}
                            </span>
                        </li>
                        % if usuario.tipo == 'freelancer':
                        <li class="nav-item">
                            <a class="nav-link" href="/servicos/meus">Meus Serviços</a>
                        </li>
                        % end
                        <li class="nav-item">
                            <a class="nav-link" href="/logout">Logout</a>
                        </li>
                        <li class="nav-item">
                            <a href="/usuario/deletar" class="nav-link text-danger" onclick="return confirm('Atenção! Esta ação é permanente. Tem a certeza de que quer excluir a sua conta e todos os seus dados?');">
                                Excluir Conta
                            </a>
                        </li>
                    % else:
                        <li class="nav-item">
                            <a class="nav-link" href="/login">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/register">Registrar</a>
                        </li>
                    % end
                </ul>
            </div>
        </div>
    </nav>

    <main class="container">
        {{!base}}
    </main>

    <footer class="text-center text-muted mt-5 py-3">
        <p>&copy; 2025 Sixerr Marketplace</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
<!DOCTYPE html>
<html lang="pt-br" class="h-100">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{get('title', 'Bem-Vindo')}} - Sixerr</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="/static/css/custom.css" />
    
    % if defined('style'):
        <link rel="stylesheet" href="/static/css/{{style}}.css" />
    % end
</head>
<body class="d-flex flex-column h-100">

    <header class="main-header">
        <nav class="navbar navbar-expand-lg navbar-light bg-white">
            <div class="container">
                <a href="/" class="navbar-brand logo" style="display: flex; align-items: center; text-decoration: none;">
                    <img src="/static/img/logo.png" alt="Logo Sixerr" style="height: 30px; margin-right: 10px;">
                    <span style="color: black; font-weight: bold;">Sixerr</span>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto align-items-center">
                        % if defined('usuario') and usuario:
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Olá, {{usuario.nome.split(' ')[0]}}
                                </a>
                                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                                    
                                    <li><a class="dropdown-item" href="/perfil">Meu Perfil</a></li>

                                    % if usuario.tipo == 'freelancer':
                                        <li><a class="dropdown-item" href="/servicos/meus">Meus Serviços</a></li>
                                        <li><a class="dropdown-item" href="/minhas-vendas">Minhas Vendas</a></li>
                                    % elif usuario.tipo == 'cliente':
                                        <li><a class="dropdown-item" href="/meus-pedidos">Meus Pedidos</a></li>
                                    % end

                                    <li>
                                        <a class="dropdown-item d-flex justify-content-between align-items-center" href="/carteira">
                                            <span>Minha Carteira</span>
                                            <span class="badge bg-success rounded-pill">R$ {{'%.2f' % usuario.saldo}}</span>
                                        </a>
                                    </li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li><a class="dropdown-item text-danger" href="/usuario/deletar" onclick="return confirm('Atenção! Esta ação é permanente e irá apagar todos os seus dados. Tem certeza?');">Excluir Conta</a></li>
                                    <li><a class="dropdown-item" href="/logout">Logout</a></li>
                                </ul>
                            </li>
                        % else:
                            <li class="nav-item">
                                <a class="nav-link" href="/login">Login</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/register">Cadastre-se</a>
                            </li>
                        % end
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <main class="flex-shrink-0">
        {{!base}}
    </main>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
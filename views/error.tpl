% rebase('layout.tpl', title='Erro', style='meus_servicos')

<div class="dark-section">
    <div class="container text-center">
        <h1 class="display-1 fw-bold">{{error.status_code}}</h1>
        <p class="lead">{{error.body}}</p>
        <a href="/" class="btn btn-primary mt-3">Voltar para a Página Inicial</a>
    </div>
</div>
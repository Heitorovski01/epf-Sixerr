% rebase('layout.tpl', title='Página Inicial')

<div class="p-5 mb-4 bg-light rounded-3">
    <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">Encontre o Freelancer Perfeito</h1>
        <p class="col-md-8 fs-4">Milhares de serviços de alta qualidade ao seu alcance.</p>
    </div>
</div>

<div class="row">
    <h2 class="mb-4">Serviços Populares</h2>
    % if not servicos:
        <p class="text-muted">Nenhum serviço disponível no momento.</p>
    % else:
        % for servico in servicos:
        <div class="col-md-4 mb-4">
            <div class="card h-100">
                <div class="card-body">
                    <h5 class="card-title">{{servico.titulo}}</h5>
                    <p class="card-text">{{servico.descricao[:100]}}...</p>
                    <h6 class="card-subtitle mb-2 text-success">R$ {{'%.2f' % servico.preco}}</h6>
                </div>
                <div class="card-footer">
                    <a href="#" class="btn btn-primary">Ver Serviço</a>
                </div>
            </div>
        </div>
        % end
    % end
</div>
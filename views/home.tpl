% rebase('layout.tpl', title='Talento Sob Demanda')

<div class="hero-section">
    <div class="container">
        <h1>Talento e Criatividade Sob Demanda</h1>
        <p class="lead">Conectando você aos melhores profissionais para transformar suas ideias em realidade.</p>
        % if not defined('usuario') or not usuario:
        <a href="/register" class="btn btn-primary btn-lg cta-button">Comece Agora</a>
        % else:
        <a href="#servicos" class="btn btn-primary btn-lg cta-button">Explorar Serviços</a>
        % end
    </div>
</div>

<div class="dark-section">
    <div class="container py-5">
        <h2 class="text-center mb-5" id="servicos">Serviços</h2>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
            % if not servicos:
                <div class="col-12">
                    <p class="text-center text-muted">Nenhum serviço disponível no momento.</p>
                </div>
            % else:
                % for servico in servicos:
                <div class="col">
                    <div class="card h-100 service-card">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title">{{servico.titulo}}</h5>
                            <p class="card-text text-muted">{{servico.descricao[:95]}}...</p>
                            <div class="mt-auto d-flex justify-content-between align-items-center">
                                <span class="price">R$ {{'%.2f' % servico.preco}}</span>
                                <a href="/servicos/detalhe/{{servico.id}}" class="btn btn-outline-primary btn-sm">Ver Detalhes</a>
                            </div>
                        </div>
                    </div>
                </div>
                % end
            % end
        </div>
    </div>
</div>
 <footer class="footer mt-auto py-3">
        <div class="container text-center">
            <span class="text-light">&copy; 2025 Sixerr. Todos os direitos reservados</span>
        </div>
</footer>
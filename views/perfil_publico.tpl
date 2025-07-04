% rebase('layout.tpl', title=freelancer.nome, style='auth_form')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-9 col-md-11">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-body p-5">
                        <h1 class="display-5">{{ freelancer.nome }}</h1>
                        <p class="text-white-50 fs-5">Freelancer</p>
                        
                        <hr class="border-secondary my-4">

                        <h5 class="mb-3">Biografia</h5>
                        <p class="text-white-50">{{ freelancer.bio if freelancer.bio else 'Nenhuma biografia fornecida.' }}</p>

                        <h5 class="mt-4 mb-3">Habilidades</h5>
                        <p class="text-white-50">{{ freelancer.habilidades if freelancer.habilidades else 'Nenhuma habilidade listada.' }}</p>

                        <h5 class="mt-4 mb-3">Contato</h5>
                        <p class="text-white-50"><strong>Localização:</strong> {{ freelancer.cidade if freelancer.cidade else 'Não informada.' }}</p>
                        <p class="text-white-50"><strong>Telefone:</strong> {{ freelancer.telefone if freelancer.telefone else 'Não informado.' }}</p>
                        
                        % if freelancer.portfolio_url:
                        <h5 class="mt-4 mb-3">Portfólio</h5>
                        <p><a href="{{freelancer.portfolio_url}}" target="_blank" class="link-light">{{freelancer.portfolio_url}}</a></p>
                        % end

                        <hr class="border-secondary my-4">
                        
                        <h4 class="text-center mb-4">Outros Serviços de {{ freelancer.nome.split(' ')[0] }}</h4>
                        <div class="row row-cols-1 row-cols-md-2 g-4">
                            % for s in servicos:
                            <div class="col">
                                <div class="card h-100 service-card">
                                    <div class="card-body">
                                        <h5 class="card-title">{{s.titulo}}</h5>
                                    </div>
                                    <div class="card-footer bg-transparent border-top-0 d-flex justify-content-between align-items-center">
                                        <span class="price">R$ {{'%.2f' % s.preco}}</span>
                                        <a href="/servicos/detalhe/{{s.id}}" class="btn btn-outline-primary btn-sm">Ver Detalhes</a>
                                    </div>
                                </div>
                            </div>
                            % end
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</div>
<footer class="footer mt-auto py-3">
        <div class="container text-center">
            <span class="text-light">&copy; 2025 Sixerr. Todos os direitos reservados</span>
        </div>
</footer>
% rebase('layout.tpl', title='Meu Perfil', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4 border-bottom border-secondary d-flex justify-content-between align-items-center">
                        <h1 class="h4 mb-0">Meu Perfil</h1>
                        % # Mostra o botão de editar apenas para freelancers
                        % if usuario.tipo == 'freelancer':
                        <a href="/perfil/editar" class="btn btn-outline-light btn-sm">Editar Perfil</a>
                        % end
                    </div>
                    <div class="card-body p-4">
                        
                        <h3>{{ usuario.nome }}</h3>
                        <p class="text-muted">{{ usuario.email }}</p>

                        <hr class="my-4 border-secondary">

                        % # Esta seção só aparece se o utilizador for do tipo 'freelancer'
                        % if usuario.tipo == 'freelancer':
                            <h5 class="mb-3">Perfil de Freelancer</h5>
                            
                            <h6>Biografia:</h6>
                            <p class="text-white-50">{{ usuario.bio if usuario.bio else 'Nenhuma biografia fornecida.' }}</p>

                            <h6>Habilidades:</h6>
                            <p class="text-white-50">{{ usuario.habilidades if usuario.habilidades else 'Nenhuma habilidade listada.' }}</p>
                            
                            <h6>Portfólio:</h6>
                            % if usuario.portfolio_url:
                                <p><a href="{{usuario.portfolio_url}}" target="_blank" class="link-light">{{usuario.portfolio_url}}</a></p>
                            % else:
                                <p class="text-white-50">Nenhum link de portfólio fornecido.</p>
                            % end
                        % end

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
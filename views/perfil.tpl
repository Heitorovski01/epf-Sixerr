% rebase('layout.tpl', title='Meu Perfil', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4 border-bottom border-secondary d-flex justify-content-between align-items-center">
                        <h1 class="h4 mb-0">Meu Perfil</h1>
                        
                        <a href="/perfil/editar" class="btn btn-outline-light btn-sm">Editar Perfil</a>

                    </div>
                    <div class="card-body p-4">
                        
                        <h3>{{ usuario.nome }}</h3>
                        <p class="text-white-50">{{ usuario.email }}</p>

                        <hr class="my-4 border-secondary">

                        % # Mostra informações diferentes com base no tipo de utilizador
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

                        % # Esta nova secção mostra os dados de contato para ambos
                        <h5 class="mt-4 mb-3">Informações de Contato</h5>
                        <h6>Localização:</h6>
                        <p class="text-white-50">{{ usuario.cidade if usuario.cidade else 'Não informada.' }}</p>
                        
                        <h6>Telefone:</h6>
                        <p class="text-white-50">{{ usuario.telefone if usuario.telefone else 'Não informado.' }}</p>

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
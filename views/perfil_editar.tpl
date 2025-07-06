% rebase('layout.tpl', title='Editar Perfil', style='auth_form')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4 border-bottom border-secondary">
                        <h1 class="h4 mb-0">Editar Perfil</h1>
                    </div>
                    <div class="card-body p-4">
                        
                        <form action="/perfil/editar" method="post">
                            
                            % # Campos que só aparecem para FREELANCERS
                            % if usuario.tipo == 'freelancer':
                                <h5 class="mb-3">Seu Perfil Profissional</h5>
                                <div class="mb-3">
                                    <label for="habilidades" class="form-label">Suas Habilidades (separadas por vírgula)</label>
                                    <input type="text" class="form-control form-control-dark" id="habilidades" name="habilidades" value="{{usuario.habilidades or ''}}">
                                </div>
                                <div class="mb-3">
                                    <label for="bio" class="form-label">Sua Biografia</label>
                                    <textarea class="form-control form-control-dark" id="bio" name="bio" rows="5">{{usuario.bio or ''}}</textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="portfolio_url" class="form-label">Link para seu Portfólio</label>
                                    <input type="url" class="form-control form-control-dark" id="portfolio_url" name="portfolio_url" value="{{usuario.portfolio_url or ''}}">
                                </div>
                                <hr class="my-4 border-secondary">
                            % end

                            % # Campos de Contato que aparecem para AMBOS
                            <h5 class="mb-3">Suas Informações de Contato</h5>
                            <div class="mb-3">
                                <label for="telefone" class="form-label">Telefone de Contato</label>
                                <input type="tel" class="form-control form-control-dark" id="telefone" name="telefone" value="{{usuario.telefone or ''}}">
                            </div>
                            <div class="mb-3">
                                <label for="cidade" class="form-label">Cidade / Localização</label>
                                <input type="text" class="form-control form-control-dark" id="cidade" name="cidade" value="{{usuario.cidade or ''}}">
                            </div>

                            <hr class="my-4 border-secondary">

                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                                <a href="/perfil" class="btn btn-outline-secondary">Cancelar</a>
                                <button type="submit" class="btn btn-primary">Salvar Alterações</button>
                            </div>
                        </form>
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
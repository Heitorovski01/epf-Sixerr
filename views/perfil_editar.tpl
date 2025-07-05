% rebase('layout.tpl', title='Editar Perfil', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4 border-bottom border-secondary">
                        <h1 class="h4 mb-0">Editar Perfil de Freelancer</h1>
                    </div>
                    <div class="card-body p-4">
                        <form action="/perfil/editar" method="post">
                            
                            % # Se for freelancer, mostra os campos de perfil de freelancer
                            % if usuario.tipo == 'freelancer':
                                <div class="mb-3">
                                    <label for="cidade" class="form-label">Cidade / Localização</label>
                                    <input type="text" class="form-control form-control-dark" id="cidade" name="cidade" value="{{usuario.cidade or ''}}">
                                </div>
                            % # Se for cliente, mostra os campos de contato do cliente
                            % elif usuario.tipo == 'cliente':
                                <h5 class="mb-3">Suas Informações de Contato</h5>
                                <div class="mb-3">
                                    <label for="telefone" class="form-label">Telefone de Contato</label>
                                    <input type="tel" class="form-control form-control-dark" id="telefone" name="telefone" value="{{usuario.telefone or ''}}">
                                </div>
                                <div class="mb-3">
                                    <label for="cidade" class="form-label">Sua Cidade</label>
                                    <input type="text" class="form-control form-control-dark" id="cidade" name="cidade" value="{{usuario.cidade or ''}}">
                                </div>
                            % end

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
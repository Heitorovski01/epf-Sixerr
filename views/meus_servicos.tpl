% rebase('layout.tpl', title='Meus Servicos', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        
        <div class="card border-secondary shadow-sm bg-dark text-light">

            <div class="card-header p-4 border-bottom border-secondary">
                <div class="d-flex justify-content-between align-items-center">
                    <h1 class="h4 mb-0">Meus Serviços</h1>
                    <a href="/servicos/novo" class="btn btn-primary btn-sm">Criar Novo Serviço</a>
                </div>
            </div>

            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-dark table-hover align-middle">
                        <thead>
                            <tr>
                                <th scope="col" class="border-secondary">Título</th>
                                <th scope="col" class="border-secondary">Preço</th>
                                <th scope="col" class="text-end border-secondary">Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            % if not servicos:
                            <tr>
                                <td colspan="3" class="text-center text-muted py-5 border-secondary">
                                    Você ainda não publicou nenhum serviço. <br>
                                    <a href="/servicos/novo" class="btn btn-success btn-sm mt-3">Crie seu primeiro serviço!</a>
                                </td>
                            </tr>
                            % else:
                                % for servico in servicos:
                                <tr>
                                    <td class="border-secondary">{{servico.titulo}}</td>
                                    <td class="border-secondary">R$ {{'%.2f' % servico.preco}}</td>
                                    <td class="text-end border-secondary">
                                        <a href="/servicos/editar/{{servico.id}}" class="btn btn-sm btn-outline-light">Editar</a>
                                        <a href="/servicos/deletar/{{servico.id}}" class="btn btn-sm btn-danger" onclick="return confirm('Tem certeza?');">Excluir</a>
                                    </td>
                                </tr>
                                % end
                            % end
                        </tbody>
                    </table>
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
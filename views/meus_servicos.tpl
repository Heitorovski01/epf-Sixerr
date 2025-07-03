% rebase('layout.tpl', title='Meus Serviços')

<div class="d-flex justify-content-between align-items-center mb-4">
    <h1>Meus Serviços</h1>
    <a href="/servicos/novo" class="btn btn-success">Criar Novo Serviço</a>
</div>

<div class="table-responsive">
    <table class="table table-striped table-hover">
        <thead>
            <tr>
                <th>Título</th>
                <th>Preço</th>
                <th class="text-end">Ações</th>
            </tr>
        </thead>
        <tbody>
            % if not servicos:
            <tr>
                <td colspan="3" class="text-center text-muted">Você ainda não criou nenhum serviço.</td>
            </tr>
            % else:
                % for servico in servicos:
                <tr>
                    <td>{{servico.titulo}}</td>
                    <td>R$ {{'%.2f' % servico.preco}}</td>
                    <td class="text-end">
                        <a href="/servicos/editar/{{servico.id}}" class="btn btn-sm btn-warning">Editar</a>
                        <a href="/servicos/deletar/{{servico.id}}" class="btn btn-sm btn-danger" onclick="return confirm('Tem certeza que deseja apagar este serviço?');">Deletar</a>
                    </td>
                </tr>
                % end
            % end
        </tbody>
    </table>
</div>
% rebase('layout.tpl', title='Minhas Vendas', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="card bg-dark text-light border-secondary shadow-lg">
            <div class="card-header p-4 border-bottom border-secondary">
                <h1 class="h4 mb-0">Meu Histórico de Vendas</h1>
            </div>
            <div class="card-body p-0">
                <div class="table-responsive">
                    <table class="table table-dark table-hover align-middle mb-0">
                        <thead>
                            <tr>
                                <th class="px-4 py-3">Serviço Vendido</th>
                                <th class="px-4 py-3">Comprador</th>
                                <th class="px-4 py-3">Data</th>
                                <th class="px-4 py-3 text-end">Valor Recebido</th>
                            </tr>
                        </thead>
                        <tbody>
                            % if not vendas:
                            <tr>
                                <td colspan="4" class="text-center text-muted py-5">
                                    Você ainda não realizou nenhuma venda.
                                </td>
                            </tr>
                            % else:
                                % for venda in vendas:
                                <tr>
                                    <td class="px-4">{{venda['servico_titulo']}}</td>
                                    <td class="px-4">{{venda['cliente_nome']}}</td>
                                    <td class="px-4">{{venda['data_contratacao']}}</td>
                                    <td class="px-4 text-end">R$ {{'%.2f' % venda['preco_pago']}}</td>
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
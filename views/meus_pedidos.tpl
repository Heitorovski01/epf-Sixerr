% rebase('layout.tpl', title='Meus Pedidos', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="card bg-dark text-light border-secondary">
            <div class="card-header p-4">
                <h1 class="h4 mb-0">Meus Serviços Contratados</h1>
            </div>
            <div class="card-body p-0">
                <div class="table-responsive">
                    <table class="table table-dark table-hover align-middle mb-0">
                        <thead>
                            <tr>
                                <th class="px-4 py-3">Serviço</th>
                                <th class="px-4 py-3">Data da Contratação</th>
                                <th class="px-4 py-3 text-end">Valor Pago</th>
                            </tr>
                        </thead>
                        <tbody>
                            % if not pedidos:
                            <tr>
                                <td colspan="3" class="text-center text-muted py-5">
                                    Você ainda não contratou nenhum serviço.
                                </td>
                            </tr>
                            % else:
                                % for pedido in pedidos:
                                <tr>
                                    <td class="px-4">{{pedido['servico_titulo']}}</td>
                                    <td class="px-4">{{pedido['data_contratacao']}}</td>
                                    <td class="px-4 text-end">R$ {{'%.2f' % pedido['preco_pago']}}</td>
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
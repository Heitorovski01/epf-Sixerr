% rebase('layout.tpl', title='Minha Carteira', style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-7 col-md-9">
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4">
                        <h1 class="h4 mb-0">Minha Carteira</h1>
                    </div>
                    <div class="card-body p-4">
    
                        <div class="text-center mb-4">
                            <h5 class="text-muted">Saldo Atual</h5>
                            <h2 class="display-4 fw-bold text-success">R$ {{'%.2f' % usuario.saldo}}</h2>
                        </div>

                        % if success:
                            <div class="alert alert-success">{{success}}</div>
                        % end
                        % if error:
                            <div class="alert alert-danger">{{error}}</div>
                        % end

                        <hr class="border-secondary my-4">

                        % if usuario.tipo == 'cliente':
                        <form action="/carteira" method="post" class="mb-4">
                            <h5 class="mb-3">Depositar Dinheiro</h5>
                            <div class="input-group">
                                <span class="input-group-text">R$</span>
                                <input type="number" class="form-control form-control-dark" name="deposito" placeholder="0.00" step="0.01" min="0.01">
                                <button class="btn btn-success" type="submit">Depositar</button>
                            </div>
                        </form>
                        % end

                        % if usuario.tipo == 'freelancer':
                        <form action="/carteira" method="post">
                            <h5 class="mb-3">Sacar Dinheiro</h5>
                            <div class="input-group">
                                <span class="input-group-text">R$</span>
                                <input type="number" class="form-control form-control-dark" name="saque" placeholder="0.00" step="0.01" min="0.01">
                                <button class="btn btn-warning" type="submit">Sacar</button>
                            </div>
                        </form>
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
% rebase('layout.tpl', title='Login')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-5 col-md-8">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-body p-5">

                        <h2 class="card-title text-center mb-4">Acessar sua Conta</h2>
                        
                        <form action="/login" method="post">
                            % if defined('error') and error:
                                <div class="alert alert-danger">{{error}}</div>
                            % end
                            
                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control form-control-dark" id="email" name="email" required>
                            </div>

                            <div class="mb-4">
                                <label for="senha" class="form-label">Senha</label>
                                <input type="password" class="form-control form-control-dark" id="senha" name="senha" required>
                            </div>

                            <button type="submit" class="btn btn-primary w-100 btn-lg">Entrar</button>
                        </form>

                        <div class="text-center mt-4">
                            <small>Não tem uma conta? <a href="/register">Registre-se</a></small>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </div>
</div>
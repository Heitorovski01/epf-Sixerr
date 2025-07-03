% rebase('layout.tpl', title='Registrar')

<div class="row justify-content-center">
    <div class="col-md-6">
        <h2 class="text-center mb-4">Criar Conta</h2>
        <form action="/register" method="post" class="card p-4">
            % if defined('error') and error:
                <div class="alert alert-danger">{{error}}</div>
            % end
            <div class="mb-3">
                <label for="nome" class="form-label">Nome Completo</label>
                <input type="text" class="form-control" id="nome" name="nome" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="senha" class="form-label">Senha</label>
                <input type="password" class="form-control" id="senha" name="senha" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Eu quero me registrar como:</label>
                <select class="form-select" name="tipo_usuario" required>
                    <option value="" disabled selected>Selecione uma opção...</option>
                    <option value="cliente">Cliente (Quero contratar)</option>
                    <option value="freelancer">Freelancer (Quero trabalhar)</option>
                </select>
            </div>
            <button type="submit" class="btn btn-success w-100">Registrar</button>
        </form>
    </div>
</div>
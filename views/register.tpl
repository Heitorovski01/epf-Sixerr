% rebase('layout.tpl', title='Criar Conta', style='login')

<div class="dark-section">
   <div class="container">
       <div class="row justify-content-center">
           <div class="col-lg-5 col-md-8">

               <div class="card bg-dark text-light border-0 shadow-lg">
                   <div class="card-body p-5">

                       <h2 class="card-title text-center mb-4">Crie sua Conta</h2>

                       <form action="/register" method="post">
                           % if defined('error') and error:
                               <div class="alert alert-danger alert-dark">{{error}}</div>
                           % end

                           <div class="mb-3">
                               <label for="nome" class="form-label">Nome Completo</label>
                               <input type="text" class="form-control form-control-dark" id="nome" name="nome" required>
                           </div>
                           <div class="mb-3">
                               <label for="email" class="form-label">Email</label>
                               <input type="email" class="form-control form-control-dark" id="email" name="email" required>
                           </div>
                           <div class="mb-3">
                               <label for="senha" class="form-label">Senha</label>
                               <input type="password" class="form-control form-control-dark" id="senha" name="senha" required>
                           </div>
                           <div class="mb-4">
                               <label class="form-label">Tipo de Conta</label>
                               <select class="form-select form-control-dark" name="tipo_usuario" required>
                                   <option value="" disabled selected>Selecione...</option>
                                   <option value="cliente">Quero Contratar</option>
                                   <option value="freelancer">Quero Trabalhar</option>
                               </select>
                           </div>

                           <button type="submit" class="btn btn-primary w-100 btn-lg">Criar Conta</button>
                       </form>

                       <div class="text-center mt-4">
                           <small class="text-light-50">Já tem uma conta? <a href="/login">Faça login</a></small>
                       </div>

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
% rebase('layout.tpl', title=servico.titulo, style='auth_form')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4">
                        <h1 class="h3 mb-0">{{servico.titulo}}</h1>
                    </div>
                    <div class="card-body p-4">
                        <h4 class="text-success mb-3">Preço: R$ {{'%.2f' % servico.preco}}</h4>
                        
                        <hr class="border-secondary">
                        
                        <h5 class="mt-4">Descrição Completa</h5>
                        <p class="text-white-50" style="white-space: pre-wrap;">{{servico.descricao}}</p>
                    </div>
                    <div class="card-footer p-4 border-top border-secondary text-end">
                        <a href="/" class="btn btn-outline-light btn-sm">Voltar</a>
                        <a href="#" class="btn btn-primary">Contratar Serviço</a>
                    </div>
                </div>

            </div>
        </div>
    </div>
</div>
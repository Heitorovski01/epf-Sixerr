% rebase('layout.tpl', title=cliente.nome, style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4">
                        <h1 class="h3 mb-0">{{ cliente.nome }}</h1>
                        <p class="mb-0 text-white-50">Cliente</p>
                    </div>
                    <div class="card-body p-4">
                        <h5 class="mt-4 mb-3">Informações de Contato</h5>
                        <hr class="border-secondary my-4">
                        <h6>Localização:</h6>
                        <p class="text-white-50">{{ cliente.cidade if cliente.cidade else 'Não informada.' }}</p>
                        
                        <h6>Telefone:</h6>
                        <p class="text-white-50">{{ cliente.telefone if cliente.telefone else 'Não informado.' }}</p>
                        
                        <h6>Email:</h6>
                        <p class="text-white-50">{{ cliente.email }}</p>
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
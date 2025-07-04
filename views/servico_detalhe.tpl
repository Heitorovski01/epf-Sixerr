% rebase('layout.tpl', title=servico.titulo, style='meus_servicos')

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    
                    <div class="card-header p-4">
                        <h1 class="h3 mb-1">{{servico.titulo}}</h1>
                        <p class="mb-0 text-white-50">
                            Oferecido por: 
                            <a href="/freelancer/{{freelancer.id}}" class="link-light fw-bold">{{freelancer.nome}}</a>
                        </p>
                    </div>
                    
                    <div class="card-body p-4">
                        <h5 class="mt-4">Descrição Completa</h5>
                        <p class="text-white-50" style="white-space: pre-wrap;">{{servico.descricao}}</p>
                    </div>

                    <div class="card-footer p-4 border-top border-secondary text-end">
                        <a href="/" class="btn btn-outline-light btn-sm">Voltar</a>
                        
                        % # Lógica para mostrar o botão de contratar
                        % if defined('usuario') and usuario and usuario.tipo == 'cliente':
                        <form action="/servicos/contratar/{{servico.id}}" method="post" style="display: inline;">
                            <button type="submit" class="btn btn-primary">Contratar por R$ {{'%.2f' % servico.preco}}</button>
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
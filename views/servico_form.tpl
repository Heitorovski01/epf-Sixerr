% rebase('layout.tpl', title='Gerenciar Serviço', style='meus_servicos')

% # Define o título com base se estamos a editar ou a criar
% if servico:
%   page_title = 'Editar Serviço'
% else:
%   page_title = 'Criar Novo Serviço'
% end

<div class="dark-section">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8 col-md-10">
                
                <div class="card bg-dark text-light border-secondary">
                    <div class="card-header p-4 border-bottom border-secondary">
                        <h1 class="h4 mb-0">{{page_title}}</h1>
                    </div>
                    <div class="card-body p-4">
                        <form action="/servicos/salvar" method="post">
                            % if defined('error') and error:
                                <div class="alert alert-danger">{{error}}</div>
                            % end
                            
                            % if servico:
                                <input type="hidden" name="id" value="{{servico.id}}">
                            % end

                            <div class="mb-3">
                                <label for="titulo" class="form-label">Título do Serviço</label>
                                <input type="text" class="form-control form-control-dark" id="titulo" name="titulo" value="{{servico.titulo if servico else ''}}" required>
                            </div>
                            <div class="mb-3">
                                <label for="descricao" class="form-label">Descrição Detalhada</label>
                                <textarea class="form-control form-control-dark" id="descricao" name="descricao" rows="5" required>{{servico.descricao if servico else ''}}</textarea>
                            </div>
                            <div class="mb-3">
                                <label for="preco" class="form-label">Preço (R$)</label>
                                <input type="number" class="form-control form-control-dark" id="preco" name="preco" step="0.01" value="{{servico.preco if servico else ''}}" required>
                            </div>

                            <hr class="my-4 border-secondary">

                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg">Salvar Serviço</button>
                            </div>
                        </form>
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
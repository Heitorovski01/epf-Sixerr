% rebase('layout.tpl', title='Gerenciar Serviço')

% # Define o título e o texto do botão com base se estamos editando ou criando
% if servico:
%   page_title = 'Editar Serviço'
%   button_text = 'Salvar Alterações'
% else:
%   page_title = 'Criar Novo Serviço'
%   button_text = 'Criar Serviço'
% end

<div class="row justify-content-center">
    <div class="col-md-8">
        <h2 class="text-center mb-4">{{page_title}}</h2>
        <form action="/servicos/salvar" method="post" class="card p-4">
            % if defined('error') and error:
                <div class="alert alert-danger">{{error}}</div>
            % end
            
            % # Se estivermos editando, precisamos enviar o ID do serviço de forma oculta
            % if servico:
                <input type="hidden" name="id" value="{{servico.id}}">
            % end

            <div class="mb-3">
                <label for="titulo" class="form-label">Título do Serviço</label>
                <input type="text" class="form-control" id="titulo" name="titulo" value="{{servico.titulo if servico else ''}}" required>
            </div>
            <div class="mb-3">
                <label for="descricao" class="form-label">Descrição Detalhada</label>
                <textarea class="form-control" id="descricao" name="descricao" rows="5" required>{{servico.descricao if servico else ''}}</textarea>
            </div>
            <div class="mb-3">
                <label for="preco" class="form-label">Preço (R$)</label>
                <input type="number" class="form-control" id="preco" name="preco" step="0.01" value="{{servico.preco if servico else ''}}" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">{{button_text}}</button>
        </form>
    </div>
</div>
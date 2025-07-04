# controllers/servico_controller.py (versão corrigida)

from bottle import request, redirect, template
from models.servico import Servico
from models.usuario import Usuario
from models.pedido import Pedido

class ServicoController:
    def list_my_services(self, user_id):
        # 2. Além dos serviços, buscamos o objeto do usuário
        usuario = Usuario.find_by_id(user_id)
        servicos = Servico.find_by_freelancer_id(user_id)
        # 3. Passamos AMBOS para o template
        return template('meus_servicos.tpl', servicos=servicos, usuario=usuario)

    def add_service_form(self, user_id):
        # Corrigido aqui também
        usuario = Usuario.find_by_id(user_id)
        return template('servico_form.tpl', servico=None, error=None, usuario=usuario)

    def edit_service_form(self, servico_id, user_id):
        # Corrigido aqui também
        usuario = Usuario.find_by_id(user_id)
        servico = Servico.find_by_id(servico_id)
        return template('servico_form.tpl', servico=servico, error=None, usuario=usuario)

    def save_service(self, user_id):
        servico_id = request.forms.get('id')
        titulo = request.forms.get('titulo')
        descricao = request.forms.get('descricao')
        preco = request.forms.get('preco')
        
        if servico_id:
            servico = Servico(id=int(servico_id), titulo=titulo, descricao=descricao, preco=float(preco), freelancer_id=user_id)
        else:
            servico = Servico(titulo=titulo, descricao=descricao, preco=float(preco), freelancer_id=user_id)
        
        servico.save()
        redirect('/servicos/meus')

    def delete_service(self, servico_id):
        Servico.delete_by_id(servico_id)
        redirect('/servicos/meus')

    def contratar_servico(self, servico_id, cliente_id):
        from models.pedido import Pedido
        from models.usuario import Usuario
        from models.servico import Servico
        
        cliente = Usuario.find_by_id(cliente_id)

        servico = Servico.find_by_id(servico_id)
        
        if not servico:
            return "Erro: Serviço não encontrado."

        freelancer = Usuario.find_by_id(servico.freelancer_id)

        if cliente.saldo < servico.preco:
            redirect(f"/servicos/detalhe/{servico_id}?error=Saldo insuficiente!")
            return 

        cliente.saldo -= servico.preco
        freelancer.saldo += servico.preco

        novo_pedido = Pedido(preco_pago=servico.preco, cliente_id=cliente.id, servico_id=servico.id)
        novo_pedido.save()

        cliente.atualiza_saldo()
        freelancer.atualiza_saldo()

        redirect(f"/meus-pedidos?success=Serviço '{servico.titulo}' contratado com sucesso!")

    def show_service_details(self, servico_id, user_id=None):

        servico = Servico.find_by_id(servico_id)

        usuario = Usuario.find_by_id(user_id) if user_id else None
        
        if not servico:
            return "Serviço não encontrado!"
            
       
        return template('servico_detalhe.tpl', servico=servico, usuario=usuario, request=request)
    
    def show_service_details(self, servico_id, user_id=None):
        servico = Servico.find_by_id(servico_id)
        if not servico: return "Serviço não encontrado!"

        # A linha mais importante: buscar o freelancer dono do serviço
        freelancer = Usuario.find_by_id(servico.freelancer_id)
        
        usuario_logado = Usuario.find_by_id(user_id) if user_id else None
            
        return template('servico_detalhe.tpl', 
                        servico=servico, 
                        freelancer=freelancer, # Passa o freelancer para a view
                        usuario=usuario_logado, 
                        request=request)
    
    
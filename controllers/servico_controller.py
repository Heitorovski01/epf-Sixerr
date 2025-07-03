# controllers/servico_controller.py (versão corrigida)

from bottle import request, redirect, template
from models.servico import Servico
from models.usuario import Usuario # <-- 1. Importamos a classe Usuario

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
        
        if servico_id: # Editando
            servico = Servico(id=int(servico_id), titulo=titulo, descricao=descricao, preco=float(preco), freelancer_id=user_id)
        else: # Criando
            servico = Servico(titulo=titulo, descricao=descricao, preco=float(preco), freelancer_id=user_id)
        
        servico.save()
        redirect('/servicos/meus')

    def delete_service(self, servico_id):
        Servico.delete_by_id(servico_id)
        redirect('/servicos/meus')
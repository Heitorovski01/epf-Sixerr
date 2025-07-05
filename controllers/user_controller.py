from bottle import request, template, response, redirect
from models.usuario import Usuario
from models.freelancer import Freelancer
from models.cliente import Cliente

class UserController:
    def login(self): return template('login.tpl', error=None)
    def register(self): return template('register.tpl', error=None)

    def do_register(self):
        nome, email, senha, tipo = request.forms.get('nome'), request.forms.get('email'), request.forms.get('senha'), request.forms.get('tipo_usuario')
        if not all([nome, email, senha, tipo]): return template('register.tpl', error="Todos os campos são obrigatórios.")
        if Usuario.find_by_email(email): return template('register.tpl', error="Este e-mail já está em uso.")
        
        if tipo == 'freelancer':
            bio = request.forms.get('bio')
            habilidades = request.forms.get('habilidades')
            portfolio_url = request.forms.get('portfolio_url')
            novo_usuario = Freelancer(nome=nome, email=email, bio=bio, habilidades=habilidades, portfolio_url=portfolio_url)
        else:
            novo_usuario = Cliente(nome=nome, email=email)
            
        novo_usuario.set_senha(senha)
        novo_usuario.save()
        return True

    def do_login(self):
        email, senha = request.forms.get('email'), request.forms.get('senha')
        if not all([email, senha]): return None 
        usuario = Usuario.find_by_email(email)
        if usuario and usuario.check_senha(senha):
            return usuario
        return None

    def logout(self):
        response.delete_cookie("user_id", path='/')
        return True

    def show_profile(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        return template('perfil.tpl', usuario=usuario)

    def edit_profile_form(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        return template('perfil_editar.tpl', usuario=usuario)

    def save_profile(self, user_id):
        usuario = Usuario.find_by_id(user_id)

        if usuario.tipo == 'freelancer':
            usuario.bio = request.forms.get('bio')
            usuario.habilidades = request.forms.get('habilidades')
            usuario.portfolio_url = request.forms.get('portfolio_url')
            usuario.telefone = request.forms.get('telefone')
            usuario.cidade = request.forms.get('cidade')
        
        elif usuario.tipo == 'cliente':
            usuario.telefone = request.forms.get('telefone')
            usuario.cidade = request.forms.get('cidade')
        
        usuario.save()
    
    def delete_self(self, user_id):
        Usuario.delete_by_id(user_id)
        response.delete_cookie("user_id", path='/')
        return True
    
    def show_wallet(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        query_dict = request.query.decode()
        success_msg = query_dict.get('success')
        error_msg = query_dict.get('error')
        return template('carteira.tpl', usuario=usuario, success=success_msg, error=error_msg)

    def process_transaction(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        deposito_str = request.forms.get('deposito')
        saque_str = request.forms.get('saque')
        try:
            if deposito_str:
                valor = float(deposito_str)
                if valor <= 0: raise ValueError("O valor do depósito deve ser positivo.")
                usuario.saldo += valor
                usuario.atualiza_saldo()
                redirect(f"/carteira?success=Depósito de R$ {valor:.2f} realizado com sucesso!")
            elif saque_str: 
                valor = float(saque_str)
                if valor <= 0: raise ValueError("O valor do saque deve ser positivo.")
                if valor > usuario.saldo: raise ValueError("Saldo insuficiente para realizar o saque.")
                usuario.saldo -= valor
                usuario.atualiza_saldo()
                redirect(f"/carteira?success=Saque de R$ {valor:.2f} realizado com sucesso!")
        except ValueError as e:
            redirect(f"/carteira?error={e}")
    
        redirect('/carteira')

    def show_my_orders(self, user_id):
        from models.pedido import Pedido
        
        usuario = Usuario.find_by_id(user_id)
        pedidos = Pedido.find_by_cliente(user_id)
        
        return template('meus_pedidos.tpl', usuario=usuario, pedidos=pedidos)
    def show_public_profile(self, freelancer_id):
        
        freelancer = Usuario.find_by_id(freelancer_id)
        
        if not freelancer or freelancer.tipo != 'freelancer':
            return template("simple_message.tpl", message="Perfil de freelancer não encontrado.")

        from models.servico import Servico
        servicos_do_freelancer = Servico.find_by_freelancer_id(freelancer.id)

        user_id = request.get_cookie("user_id", secret="uma-chave-secreta-muito-forte-e-dificil")
        usuario_logado = Usuario.find_by_id(user_id) if user_id else None

        return template('perfil_publico.tpl', 
                        freelancer=freelancer, 
                        servicos=servicos_do_freelancer,
                        usuario=usuario_logado)

    def show_my_sales(self, user_id):
        from models.pedido import Pedido
        usuario = Usuario.find_by_id(user_id)
        vendas = Pedido.find_by_freelancer(user_id)
        return template('minhas_vendas.tpl', usuario=usuario, vendas=vendas)

    def show_public_client_profile(self, cliente_id):
        cliente = Usuario.find_by_id(cliente_id)
        
        if not cliente or cliente.tipo != 'cliente':
            return template("simple_message.tpl", message="Perfil de cliente não encontrado.")

        user_id = request.get_cookie("user_id", secret="uma-chave-secreta-muito-forte-e-dificil")
        usuario_logado = Usuario.find_by_id(user_id) if user_id else None

        return template('perfil_cliente.tpl', 
                        cliente=cliente,
                        usuario=usuario_logado)
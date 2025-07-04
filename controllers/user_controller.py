# controllers/user_controller.py (Versão Corrigida)

from bottle import request, template, response # 'response' ainda é necessário para o logout
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
        
        UserClass = Freelancer if tipo == 'freelancer' else Cliente
        novo_usuario = UserClass(nome=nome, email=email)
        novo_usuario.set_senha(senha)
        novo_usuario.save()
        print(f"\n--- [REGISTO] Utilizador '{novo_usuario.nome}' (ID: {novo_usuario.id}) salvo com sucesso no banco! ---\n")
        return True # Retorna sucesso

# Em controllers/user_controller.py
    def do_login(self):
        email = request.forms.get('email')
        senha = request.forms.get('senha')

        print(f"\n--- [LOGIN] Tentativa de login para email: {email} ---")
        print(f"--- [LOGIN] Senha digitada no formulário: {senha} ---")

        if not all([email, senha]):
            return None 

        usuario = Usuario.find_by_email(email)

        if usuario:
            print(f"--- [LOGIN] Utilizador encontrado. ID: {usuario.id}. A verificar a senha... ---")
            senha_valida = usuario.check_senha(senha)
            print(f"--- [LOGIN] O resultado de check_senha foi: {senha_valida} ---")
            if senha_valida:
                return usuario
        else:
            print(f"--- [LOGIN] Utilizador com email '{email}' não foi encontrado no banco. ---")

        return None

    def logout(self):
        # O logout pode continuar aqui, pois é uma ação simples
        response.delete_cookie("user_id", path='/')
        return True
    
    # (O resto dos seus métodos de perfil continuam iguais)
    def show_profile(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        return template('perfil.tpl', usuario=usuario)

    def edit_profile_form(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        if usuario.tipo != 'freelancer':
            return redirect('/perfil')
        return template('perfil_editar.tpl', usuario=usuario)

# Em controllers/user_controller.py

    def save_profile(self, user_id):
        usuario = Usuario.find_by_id(user_id)

        if usuario.tipo == 'freelancer':
            # --- DEBUGGING ---
            print("\n--- [CONTROLLER] DADOS RECEBIDOS DO FORMULÁRIO ---")
            print(f"Bio recebida: {request.forms.get('bio')}")
            print(f"Habilidades recebidas: {request.forms.get('habilidades')}")
            # -----------------

            usuario.bio = request.forms.get('bio')
            usuario.habilidades = request.forms.get('habilidades')
            usuario.portfolio_url = request.forms.get('portfolio_url')
            
            # --- DEBUGGING ---
            print("\n--- [CONTROLLER] OBJETO ANTES DE CHAMAR .save() ---")
            print(f"Valor de usuario.bio: {usuario.bio}")
            print("-------------------------------------------------")
            # -----------------
            
            usuario.save()
        
        return True
    
    def delete_self(self, user_id):
        Usuario.delete_by_id(user_id)
        response.delete_cookie("user_id", path='/')
        return True
    
    def show_wallet(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        return template('carteira.tpl', usuario=usuario, success=None, error=None)

    def process_transaction(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        
        # Pega os valores do formulário
        deposito_str = request.forms.get('deposito')
        saque_str = request.forms.get('saque')

        try:
            if deposito_str:
                valor = float(deposito_str)
                if valor <= 0:
                    raise ValueError("O valor do depósito deve ser positivo.")
                usuario.saldo += valor
                usuario.atualiza_saldo()
                return template('carteira.tpl', usuario=usuario, success=f"Depósito de R$ {valor:.2f} realizado com sucesso!", error=None)

            if saque_str: 
                valor = float(saque_str)
                if valor <= 0:
                    raise ValueError("O valor do saque deve ser positivo.")
                if valor > usuario.saldo:
                    raise ValueError("Saldo insuficiente para realizar o saque.")
                usuario.saldo -= valor
                usuario.atualiza_saldo()
                return template('carteira.tpl', usuario=usuario, success=f"Saque de R$ {valor:.2f} realizado com sucesso!", error=None)
        
        except ValueError as e:
            return template('carteira.tpl', usuario=usuario, success=None, error=str(e))

        
        redirect('/carteira')
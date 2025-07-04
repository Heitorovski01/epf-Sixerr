# controllers/user_controller.py
from bottle import request, response, redirect, template
from models.usuario import Usuario
from models.freelancer import Freelancer
from models.cliente import Cliente

class UserController:
    def register(self): return template('register.tpl', error=None)
    def login(self): return template('login.tpl', error=None)

    def do_register(self):
        nome, email, senha, tipo = request.forms.get('nome'), request.forms.get('email'), request.forms.get('senha'), request.forms.get('tipo_usuario')
        if not all([nome, email, senha, tipo]): return template('register.tpl', error="Todos os campos são obrigatórios.")
        if Usuario.find_by_email(email): return template('register.tpl', error="Este e-mail já está em uso.")
        
        UserClass = Freelancer if tipo == 'freelancer' else Cliente
        novo_usuario = UserClass(nome=nome, email=email)
        novo_usuario.set_senha(senha)
        novo_usuario.save()
        redirect('/login')

    def do_login(self):
        email, senha = request.forms.get('email'), request.forms.get('senha')
        if not all([email, senha]): return template('login.tpl', error="Email e senha são obrigatórios.")
        
        usuario = Usuario.find_by_email(email)
        if usuario and usuario.check_senha(senha):
            response.set_cookie("user_id", str(usuario.id), secret="troque-por-uma-frase-muito-longa-e-segura-depois", path='/')
            redirect('/')
        else:
            return template('login.tpl', error="E-mail ou senha inválidos.")

    def logout(self):
        response.delete_cookie("user_id", path='/')
        redirect('/login')
    
    def delete_self(self, user_id):
        Usuario.delete_by_id(user_id)
       
        response.delete_cookie("user_id", path='/')
    
        redirect('/')
    
    def edit_profile_form(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        if usuario.tipo != 'freelancer':
            return redirect('/perfil')
        return template('perfil_editar.tpl', usuario=usuario)

    def save_profile(self, user_id):
        usuario = Usuario.find_by_id(user_id)

        if usuario.tipo == 'freelancer':
            usuario.bio = request.forms.get('bio')
            usuario.habilidades = request.forms.get('habilidades')
            usuario.portfolio_url = request.forms.get('portfolio_url')
            usuario.save()

        redirect('/perfil')
    
    def show_profile(self, user_id):
        usuario = Usuario.find_by_id(user_id)
        
        return template('perfil.tpl', usuario=usuario)
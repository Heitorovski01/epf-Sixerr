from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()


    # Rotas User
    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)

    def login(self):

        if request.method == 'GET':
            return self.render('login_form')

        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')

            user = self.user_service.check_password(email, password)

            if user:
                print(f"Login bem-sucedido para o usuário: {user.name}")
                return self.redirect('/users')
            else:
                return self.render('login_form', error="E-mail ou senha inválidos.")


    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)


    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add")
        else:
            # POST - salvar usuário
            self.user_service.save()
            self.redirect('/users')


    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            # POST - salvar edição
            self.user_service.edit_user(user)
            self.redirect('/users')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')

    def register(self):
        if request.method == 'GET':
            return self.render('register_form')

        if request.method == 'POST':
            name = request.forms.get('name')
            email = request.forms.get('email')
            password = request.forms.get('password')
            user_type = request.forms.get('user_type')
            
            try:
                
                extra_data = {}
                if user_type == 'vendedor':
                    extra_data = {
                        'username': request.forms.get('username'),
                        'headline': request.forms.get('headline'),
                        'bio': request.forms.get('bio'),
                        'skills': request.forms.get('skills'),
                        'location': request.forms.get('location')
                    }
                
                self.user_service.save_user(name, email, password, user_type, **extra_data)
                
                return self.redirect('/users')
            except Exception as e:
                return f"<h1>Ocorreu um erro ao registrar: {e}</h1>"


user_routes = Bottle()
user_controller = UserController(user_routes)

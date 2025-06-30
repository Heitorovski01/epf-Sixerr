import bcrypt
from bottle import request
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()


    def get_all(self):
        users = self.user_model.get_all()
        return users


    def save_user(self, name, email, password, user_type, **kwargs):
        
        all_users = self.user_model.get_all()
        last_id = max([u.id for u in all_users], default=0)
        new_id = last_id + 1

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if 'skills' in kwargs and isinstance(kwargs.get('skills'), str):
            kwargs['skills'] = [skill.strip() for skill in kwargs['skills'].split(',')]

        user = User(
            id=new_id,
            name=name,
            email=email,
            password_hash=hashed_password.decode('utf-8'),
            user_type=user_type,
            **kwargs 
        )

    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)


    def edit_user(self, user):
        user = self.get_by_id(user_id)
        if not user:
            return None

        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.user_type = data.get('user_type', user.user_type)
        user.username = data.get('username', user.username)
        user.headline = data.get('headline', user.headline)
        user.bio = data.get('bio', user.bio)
        user.location = data.get('location', user.location)

        if 'skills' in data and isinstance(data.get('skills'), str):
            user.skills = [skill.strip() for skill in data['skills'].split(',')]

        new_password = data.get('password')
        if new_password:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            user.password_hash = hashed_password.decode('utf-8')

        self.user_model.update_user(user)
        return user


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)

    def check_password(self, email: str, password: str):
        
        all_users = self.user_model.get_all()
        user_found = next((u for u in all_users if u.email == email), None)

        if not user_found:
            return None

        password_is_valid = bcrypt.checkpw(
            password.encode('utf-8'), 
            user_found.password_hash.encode('utf-8')
        )

        if password_is_valid:
            return user_found
        else:
            return None
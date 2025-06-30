import json
import os
import uuid
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, id: int, name: str, email: str, password_hash: str, user_type: str,
                 username: str = None, headline: str = None, bio: str = None, 
                 skills: list = None, location: str = None):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.user_type = user_type
        self.username = username
        self.headline = headline
        self.bio = bio
        self.skills = skills if skills is not None else [] 
        self.location = location

    def to_dict(self):
        
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "user_type": self.user_type,
            "username": self.username,
            "headline": self.headline,
            "bio": self.bio,
            "skills": self.skills,
            "location": self.location
        }


    


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)


    def add_user(self, user: User):
        self.users.append(user)
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()

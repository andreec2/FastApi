from app.db.session import users_db
from app.models.user import User

def get_user(user_id: int) -> User | None:
    return users_db.get(user_id)

def get_users() -> list[User]:
    return list(users_db.values())

def create_user(user: User) -> User:
    if user.id in users_db:
        raise ValueError("User with this ID already exists.")
    users_db[user.id] = user
    return user

def update_user(user_id: int, user: User) -> User:
    if user_id not in users_db:
        raise ValueError("User not found.")
    users_db[user_id] = user
    return user

def delete_user(user_id: int) -> bool:
    if user_id in users_db:
        del users_db[user_id]
        return True
    return False 

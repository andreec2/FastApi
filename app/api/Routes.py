from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import get_user, create_user, update_user, delete_user, get_users

router = APIRouter()

@router.get("/{user_id}", response_model=User)
def get_user_id(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HHTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[User])
def get_all_users():
    return get_users()

@router.post("/", response_model=User)
def add_user(user: User):
    return create_user(user)

@router.put("/{user_id}", response_model=User)
def update_user_route(user_id: int, user: User):
    try:
        updated_user = update_user(user_id, user)
        return updated_user
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def remove_user(user_id: int):
    bool = delete_user(user_id)
    if not bool:
        raise HHTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}


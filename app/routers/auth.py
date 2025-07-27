from fastapi import APIRouter
from app.services import AuthService
from app.schemas import UserCreate, UserRead, LoginSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=str, summary="Register a new user and return a session token", responses={400: {"description": "Email already registered"}})
def register(user: UserCreate):
    return AuthService.register(user)


@router.post("/login", response_model=str, summary="Login a user and return a session token", responses={401: {"description": "Invalid credentials"}})
def login(data: LoginSchema):
    return AuthService.login(data.email, data.password)

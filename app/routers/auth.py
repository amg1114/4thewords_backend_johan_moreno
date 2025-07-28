from fastapi import APIRouter, Depends
from app.services import AuthService
from app.schemas import UserCreate, UserRead, LoginSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=str, summary="Register a new user and return a session token", responses={400: {"description": "Email already registered"}})
def register(user: UserCreate):
    return AuthService.register(user)


@router.post("/login", response_model=str, summary="Login a user and return a session token", responses={401: {"description": "Invalid credentials"}})
def login(data: LoginSchema):
    return AuthService.login(data.email, data.password)

@router.get("/me", response_model=UserRead, summary="Get the current authenticated user")
def get_current_user(current_user: UserRead = Depends(AuthService.get_current_user)):
    return current_user
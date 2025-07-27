from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.schemas import UserCreate, UserRead
from app.services import UserService
from jose import JWTError
from app.utils.security import authenticate_user, create_jwt_token, decode_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthService:
    @staticmethod
    def register(user_data: UserCreate) -> str:
        user = UserService.create(user_data)

        token_data = {"sub": user.email, "user_id": user.id}
        token = create_jwt_token(token_data)
        return token

    @staticmethod
    def login(email: str, password: str) -> str:
        user = UserService.find_by_email(email)
        is_authenticated = authenticate_user(email, password, user)

        if not is_authenticated:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        token_data = {"sub": user.email, "user_id": user.id}
        token = create_jwt_token(token_data)
        return token

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme)) -> UserRead:
        try:
            payload = decode_jwt_token(token)
            user_email = payload.get("sub")
            user_id = payload.get("user_id")

            if not user_email or not user_id:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token: missing user information"
                )

            user = UserService.find_by_email(user_email)
            if user.id != user_id:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token: user ID mismatch"
                )

            return UserRead(**user.model_dump())
        except JWTError as e:
            raise HTTPException(
                status_code=401,
                detail="Invalid token: " + str(e)
            ) from e
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="Unexpected Error: " + str(e)
            ) from e

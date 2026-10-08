from fastapi import APIRouter, HTTPException

from dto.user_dto import LoginRequest, LoginResponse


router = APIRouter(
    prefix='/auth',
    tags=['로그인 관련 라우터']
)


@router.post('/login', response_model=LoginResponse)
def login(login_data: LoginRequest):
    pass
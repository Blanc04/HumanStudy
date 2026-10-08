from pydantic import BaseModel, Field

# 로그인 요청 DTO
class LoginRequest(BaseModel):
    user_id: str = Field(min_length=1, max_length=12)
    user_pw: str = Field(min_length=1, max_length=255)

# 로그인 성공 응답 DTO
class LoginResponse(BaseModel):
    user_id: str
    user_name: str | None
    user_status_id: int
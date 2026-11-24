# SQLModel: 테이블 모델 정의, Field: PK/길이 등의 컬럼 설정
from sqlmodel import SQLModel, Field
# Optional은 None 허용 타입 표현용이지만 현재 코드에서는 직접 사용하지 않음
from typing import Optional
# 유저상태 테이블 DTO
# 사용자 상태 정보를 저장하는 테이블 모델
class UserStatus(SQLModel,table=True):
    # 사용자 상태 식별자(PK)
    user_status_id:int=Field(
		primary_key = True,  
	)
    # 사용자 상태 이름. 최대 20자
    user_status_name:str=Field(
        max_length=20
    )
    
    # 사용자 상태를 코드 값으로 구분하기 위한 정수 컬럼
    user_status_code:int
    
# SQLModel: 테이블 모델 정의, Field: PK/FK/문자열 길이 등의 컬럼 설정
from sqlmodel import SQLModel, Field
# Optional은 None 허용 타입 표현용이지만 현재 코드에서는 직접 사용하지 않음
from typing import Optional
# userDTO 설계
# 사용자 계정 정보를 저장하는 테이블 모델
class User(SQLModel,table=True):
     
    # 사용자 ID(PK). 현재 타입 선언상 None도 허용
    user_id:str | None=Field(
		primary_key = True,
        max_length=12
  
	)
    # 사용자 이름. 최대 20자
    user_name:str=Field(
        max_length=20
    )
    # 사용자 닉네임. 최소 2자, 최대 30자
    user_nickname:str=Field(
        min_length=2,
        max_length=30
    )
    # 비밀번호를 저장하는 문자열 컬럼. 최대 255자
    user_pw:str=Field(
        max_length=255
    )
    # 전화번호를 저장하는 문자열 컬럼. 최대 30자
    user_phone:str=Field(
        max_length=30
    )
    # 사용자의 상태를 user_status 테이블과 연결하는 FK
    user_status_id:int=Field(
          foreign_key='user_status.user_status_id',
    )
    # 사용자 거주지/주소 관련 문자열. 최대 50자
    user_home:str=Field(
        max_length=50
    )
    # 사용자 이메일. 최대 40자
    user_email:str=Field(
        max_length=40
    )
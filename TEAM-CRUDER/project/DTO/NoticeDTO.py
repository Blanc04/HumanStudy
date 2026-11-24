# SQLModel: 테이블 모델 정의, Field: PK/FK/길이 등의 컬럼 설정
from sqlmodel import SQLModel, Field
# from typing import Optional
# datetime은 공지 등록 날짜와 시간을 저장할 때 사용
from datetime import datetime
# 공지사항 한 건을 저장하는 테이블 모델
class Notice(SQLModel, table=True):
    # 공지사항 식별자(PK). 생성 전에는 None 허용
    notice_id:int | None=Field(
        default=None,
        primary_key=True
    )
    # 공지 제목. 최대 200자
    notice_title:str=Field(
        max_length=200
    )
    # 공지 본문. 최대 2000자
    notice_detail:str=Field(
        max_length=2000
    )
    
    # 공지가 등록된 날짜와 시간
    notice_date:datetime
    
    # 공지 작성자를 user 테이블과 연결하는 FK
    user_id:str=Field(
        foreign_key='user.user_id',
        max_length=12
    )
    
    
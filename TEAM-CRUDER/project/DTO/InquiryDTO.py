# SQLModel: 테이블 모델 정의, Field: 컬럼의 제약조건(PK/FK/길이 등)을 지정
from sqlmodel import SQLModel, Field
# datetime은 날짜+시간, date는 날짜만 저장할 때 사용
from datetime import datetime,date
# 사용자 문의 내용을 저장하는 테이블 모델
class Inquiry(SQLModel, table=True):
    # 문의 식별자(PK). 새 문의 생성 시 아직 ID가 없을 수 있어 None 허용
    inquiry_id:int| None=Field(
        default=None,
        primary_key=True
    )
    # 문의 제목. 최대 100자
    inquiry_title:str=Field(
        max_length=100
    )
    # 문의 본문. 최대 5000자
    inquiry_detail:str=Field(
        max_length=5000
    )
    # 문의가 등록된 날짜와 시간
    inquiry_date:datetime
    # 관리자 등의 답변 내용. 답변 전에는 None
    inquiry_answer:str | None=Field(
        default=None,
        max_length=2000
    )
    # 답변 날짜. 답변 전에는 None
    inquiry_answer_date:date | None=None
    
    # 문의를 작성한 사용자를 user 테이블과 연결하는 FK
    user_id:str=Field(
        foreign_key='user.user_id'
    )
    # 문의 처리 상태를 inquiry_status 테이블과 연결하는 FK
    inquiry_status_id:int=Field(
        foreign_key='inquiry_status.inquiry_status_id'
    )
    
    # 문의 유형을 저장하는 문자열 컬럼. 최대 5자
    inquiry_type:str=Field(
        max_length=5
    )
    
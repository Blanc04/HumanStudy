# SQLModel: 테이블 모델 정의, Field: PK/기본값/길이 등을 설정
from sqlmodel import SQLModel, Field

# 문의의 처리 상태 종류를 관리하는 테이블 모델
class InquiryStatus(SQLModel, table=True):
    # 실제 데이터베이스 테이블 이름
    __tablename__ = "inquiry_status"
    # 문의 상태 식별자(PK). 생성 전에는 None일 수 있음
    inquiry_status_id:int|None=Field(
        default=None,
        primary_key=True
    )
    # 문의 상태 이름. 최대 5자
    inquiry_status_name:str=Field(
        max_length=5
    )
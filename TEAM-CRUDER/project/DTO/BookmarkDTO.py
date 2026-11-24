# SQLModel: 테이블 모델 정의, Field: 컬럼 제약조건을 설정
from sqlmodel import SQLModel, Field

# 사용자가 채용공고를 북마크한 관계를 저장하는 테이블 모델
class BookMark(SQLModel,table=True):
    # 사용자 ID. 아래 채용공고 번호와 함께 복합 기본키를 구성
    user_id:str |None=Field(
        primary_key = True,
        foreign_key='user.user_id',
        max_length=12
    )
    # 채용공고 식별값. user_id와 함께 같은 북마크의 중복 저장을 막는 복합 PK
    recrut_pblnt_sn: str=Field(
        primary_key = True,
        # 현재는 jobs 테이블과의 FK 연결이 주석 처리된 상태
        # foreign_key='jobs.recrut_pblnt_sn',
        max_length=20
    )
# SQLModel: 테이블 모델 정의, Field: PK/FK/기본값/길이 등을 설정
from sqlmodel import SQLModel, Field

# 게시글 신고 기록을 저장하는 테이블 모델
class ReportLogsDTO(SQLModel,table=True):
    # 실제 데이터베이스 테이블 이름
    __tablename__ = "report_logs"
    # 신고 기록 식별자(PK). 생성 전에는 None 허용
    report_id:int |None=Field(
        default=None,
        primary_key=True
    )
    # 신고 사유. 사유가 없을 수도 있어 None 허용, 최대 120자
    report_reason:str | None=Field(
        default=None,
        max_length=120
    ) 
    # 신고한 사용자를 user 테이블과 연결하는 FK
    user_id:str=Field(
        foreign_key='user.user_id',
        max_length=12
    )
    # 신고 대상 취업 팁 게시글을 job_tip 테이블과 연결하는 FK
    job_tip_no:int=Field(
        foreign_key='job_tip.job_tip_no'
    )
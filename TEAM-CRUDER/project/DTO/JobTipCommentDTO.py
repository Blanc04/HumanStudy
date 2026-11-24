# SQLModel: 테이블 모델 정의, Field: PK/FK/길이 등의 컬럼 설정
from sqlmodel import SQLModel, Field
# Optional은 None 허용 타입 표현에 사용할 수 있지만, 현재 코드에서는 직접 사용하지 않음
from typing import Optional
# 댓글 DTO
# 취업 팁 게시글의 댓글 및 대댓글을 저장하는 테이블 모델
class JobTipComment(SQLModel, table=True):
    # 실제 데이터베이스 테이블 이름
    __tablename__ = "job_tip_comment"
    # 댓글 번호(PK). 자동 생성 전에는 None 허용
    reple_no:int | None=Field(
        default=None,
        primary_key=True
    )
    # 댓글 본문. 최대 500자
    reple:str=Field(
        max_length=500
    )
   
    # 부모 댓글 번호. 값이 있으면 대댓글, None이면 일반 댓글로 볼 수 있음
    parent_reple_no:int | None=Field(
        default=None,
        foreign_key='job_tip_comment.reple_no'
    )
    # 댓글이 달린 취업 팁 게시글을 job_tip 테이블과 연결하는 FK
    job_tip_no:int=Field(
        foreign_key='job_tip.job_tip_no'
    )
    # 댓글 작성자를 user 테이블과 연결하는 FK
    user_id:str=Field(
        foreign_key='user.user_id',
        max_length=12
    )
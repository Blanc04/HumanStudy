# SQLModel: 테이블 모델 정의, Field: 컬럼 옵션 지정
from sqlmodel import SQLModel, Field
# Optional은 None 허용 타입 표현용이지만 현재 코드에서는 직접 사용하지 않음
from typing import Optional
# datetime은 작성일처럼 날짜와 시간을 함께 저장할 때 사용
from datetime import datetime
# 취업 꿀팀 게시판 Dto
# auto_increment 들어가는 곳은 기본값 none이라고 설정하기
# 취업 팁 게시글 한 건을 저장하는 테이블 모델
class JobTip(SQLModel,table=True):

    # erd에서 설계한 테이블 명과 일치시키는 작업 추가
    # 실제 데이터베이스 테이블 이름을 ERD의 이름과 맞춤
    __tablename__ = "job_tip"

    # 게시글 번호(PK). auto_increment 전에 값이 없으므로 None 허용
    job_tip_no:int| None=Field(
        default=None,
        primary_key=True
    )
    # 게시글 제목. 최대 200자
    job_tip_title:str=Field(
        max_length=200
    )
    # 게시글 작성 날짜와 시간
    job_tip_date:datetime
    # 게시글 본문
    job_tip_detail:str
    # 첨부파일 경로/이름 등을 저장할 수 있는 선택 항목
    job_tip_attachment:str | None=None
    # 작성자를 user 테이블과 연결하는 FK
    user_id:str=Field(
        foreign_key='user.user_id',
        max_length=12
    )
    # 조회수. 새 글은 기본값 0에서 시작
    view_count:int=Field(
        default=0
    )
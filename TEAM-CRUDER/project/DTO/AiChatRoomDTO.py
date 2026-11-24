# SQLModel: 테이블 모델 정의, Field: 컬럼의 PK/FK/기본값 등을 설정
from sqlmodel import SQLModel, Field
# date 타입은 날짜(연-월-일)만 저장할 때 사용
from datetime import date

# AI 채팅방 정보를 저장하는 테이블 모델
class AiChatRoom(SQLModel, table=True):
  # 실제 데이터베이스 테이블 이름
  __tablename__ = "ai_chat_room"
  # 채팅방 식별자(PK). DB에서 생성되기 전에는 None일 수 있음
  ai_chat_id:int|None=Field(
      default=None,
      primary_key=True
  )
  # 채팅방 생성/기준 날짜. 값이 없을 수도 있어 None 허용
  ai_chat_date:date|None=None
  # 채팅방을 소유한 사용자의 ID를 user 테이블과 연결하는 FK
  user_id:str=Field(
      foreign_key='user.user_id'
  )
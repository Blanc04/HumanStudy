# SQLModel: 데이터베이스 테이블 모델을 만들기 위한 기본 클래스, Field: 컬럼의 상세 설정(PK/FK/기본값 등)을 지정할 때 사용
from sqlmodel import SQLModel, Field

# AI 채팅 메시지 한 건을 저장하는 테이블 모델
class AiChatMsg(SQLModel,table=True):
    # 실제 데이터베이스에서 사용할 테이블 이름을 지정
    __tablename__ = "ai_chat_message"
    # 메시지 식별자(PK). 새 레코드 생성 전에는 값이 없을 수 있어 None 허용
    ai_chat_message_id:int|None=Field(
        default=None,
        primary_key=True
    )
    # 실제 채팅 메시지 내용. 내용이 비어 있을 가능성을 고려해 None 허용
    ai_chat_detail:str|None=None
    # 이 메시지가 어느 채팅방에 속하는지 나타내는 외래 키(FK)
    ai_chat_id:int=Field(
        foreign_key='ai_chat_room.ai_chat_id'
    )
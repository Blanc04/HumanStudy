from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator, model_validator

class Emp3(SQLModel, table=True):
    # 없으면 클래스명이 테이블 명이 됨
    # __tablename__ = "emp"

    # empno: int = Field(primary_key = True)
    empno: int | None = Field(
        default = None,
        primary_key = True
    )
    ename: str
    job: str
    # mgr: int | None = None
    mgr: Optional[int] | None
    hiredate: str
    sal: float
    # comm: float | None = None
    comm: Optional[float] | None
    deptno: int = Field(
        foreign_key='dept3.deptno'
    )

    # 지정 변수들만 검증
    # @field_validator('comm', mode='before')
    # @classmethod
    # def empty_to_none(cls, value):
    #     if value == '':
    #         return None
    #     else:
    #         return value

    #     return None if value == '' else value
    #     return value if value != '' else None

    # 모든 변수 검증
    # @model_validator('comm', mode='before')
    # @classmethod
    # def empty_to_none(cls, value):
    #     return { key: (value if value != "" else None) for key, value in value.items()}
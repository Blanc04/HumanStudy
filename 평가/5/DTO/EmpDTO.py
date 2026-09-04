from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator, model_validator

class Emp3(SQLModel):
    # 없으면 클래스명이 테이블 명이 된다
    # __tablename__ = "emp"

    # empno: int = Field(primary_key = True)
    empno: int | None = Field(
        default = None,         # auto_increment
        primary_key = True
    )
    ename: str
    job: str
    # mgr: int | None = None
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    # comm: float | None = None
    # comm: Optional[float] = None
    comm: Optional[float] = None
    deptno: int = Field(
        foreign_key='dept3.deptno'
    )

    # 지정 변수들 만 검증
    @field_validator('comm', 'mgr', mode='before')
    @classmethod
    def empty_to_none(cls, value):
        print('>>>>>>>>', value)
        if value == "":
            return None
        else:
            return value

        # return None if value == "" else value
        # return value if value != "" else None

    # # 모든 변수 검증
    # @model_validator(mode='before')
    # @classmethod
    # def empty_to_none(cls, values):
    #     print('>>', values.items())
    #     return { key :  (value if value != "" else None) for key, value in values.items() }



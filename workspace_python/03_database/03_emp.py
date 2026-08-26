# sqlmodel 라이브러리 설치
# pip install sqlmodel

# create_engine : DB와 연결하기 위한 엔진 생성
# Session : DB와 실제로 SQL을 주고받는 세션
# SQLModel : DB 테이블과 연결할 모델의 기본 클래스
from sqlmodel import create_engine, Session, SQLModel
# FastAPI : FastAPI 서버 생성
# Depends : 특정 함수를 의존성으로 자동 실행/주입
# Request : 브라우저에서 들어온 요청 정보
# Form : HTML form에서 전달된 값을 받음
from fastapi import FastAPI, Depends, Request, Form
# Jinja2 HTML 템플릿을 FastAPI에서 사용하기 위한 클래스
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

# 직접 작성한 SQL문을 실행할 수 있도록 text를 가져옴
from sqlalchemy import text

# SQLModel.metadata에 등록 시킴
# 그러면 create_all로 테이블이 없으면 만들어 줌
# Emp3(SQLModel, table=True) 이것 둘 다 적으면 자동으로 만들어 줌
# Emp3 모델을 불러오면서 SQLModel.metadata에 emp3 테이블 정보를 등록
from DTO.EmpDTO import Emp3
# Dept3 모델을 불러오면서 SQLModel.metadata에 dept3 테이블 정보를 등록
from DTO.DeptDTO import Dept3


# FastAPI 애플리케이션 객체 생성
app = FastAPI()
# templates 폴더를 Jinja2 HTML 파일이 있는 폴더로 지정
templates = Jinja2Templates(directory='templates/')

# DB+driver://id:pw@ip:port/database
# MySQL DB 접속 주소
# mysql : 사용할 DB
# pymysql : Python에서 MySQL과 연결할 드라이버
# root : DB 사용자 ID
# human1234$ : DB 비밀번호
# 127.0.0.1 : 현재 컴퓨터에 있는 DB 서버
# 3306 : MySQL 기본 포트
# human : 사용할 데이터베이스 이름
DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'
# 위 DATABASE_URL을 이용해 DB 연결 엔진 생성
# echo=True : 실행되는 SQL문을 터미널에 출력
engine = create_engine(DATABASE_URL, echo=True)

# 먼저 EMP 테이블 표시하는 것을 목표로 함

# FastAPI에서 사용할 DB Session을 생성하는 함수
def get_session():
    # engine을 이용해 DB Session 생성
    # with가 끝나면 Session도 자동으로 정리됨
    with Session(engine) as session :
        # Depends를 통해 해당 Session을 라우터 함수에 전달
        yield session
        session.commit()

# FastAPI 서버가 시작될 때 한 번 실행
@app.on_event('startup')
def on_startup():
    # SQLModel.metadata에 등록된 테이블 중
    # DB에 존재하지 않는 테이블이 있으면 자동으로 생성
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        sql = text('''
            insert into emp3
            select * from emp;
        ''')
        session.execute(sql)
        session.commit()

# 전체 조회
# /emp 주소로 GET 요청이 들어오면 실행
@app.get('/emp')
def emp_list(
    # 현재 브라우저의 요청 정보를 받음
    request:Request,
    # get_session()에서 만든 DB Session을 자동으로 받아옴
    session:Session = Depends(get_session)
):
    try:
        # text : sql문을 실행하기 전에 미리 컴파일 해둠
        # emp3 테이블의 모든 데이터를 조회하는 SQL문 작성
        sql = text('''
            select *
            from emp3
        ''')

        # 작성한 SQL문을 현재 DB Session에서 실행
        result = session.execute(sql)
        # 조회 결과를 컬럼명:값 형태의 딕셔너리 구조로 변환한 뒤 전부 가져옴
        emp_list = result.mappings().fetchall()
        # 일반 Row 형태로 모든 결과를 가져오는 방법
        # emp_list = result.fetchall()
        # fetchall()과 비슷하게 모든 결과를 가져오는 방법
        # emp_list = result.all()
        # 조회된 직원 목록을 터미널에서 확인
        print(emp_list)

    # try 안에서 오류가 발생한 경우 실행
    except Exception as e :
        # 발생한 오류 내용을 터미널에 출력
        print(e)

    # list.html을 브라우저에 보여줌
    # emp_list라는 이름으로 조회한 직원 목록을 HTML에 전달
    return templates.TemplateResponse(request, 'list.html', {
        'emp_list': emp_list
    })

if __name__=="__main__":
    import uvicorn
    uvicorn.run('02_sqlmodel:app', port=8000, reload=True, host="0.0.0.0")
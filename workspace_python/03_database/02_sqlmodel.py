# pip install sqlmodel

from sqlmodel import create_engine, Session, SQLModel
from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy import text

# SQLModel.metadata에 등록 시킨다
# 그러면 create_all로 테이블이 없으면 만들어 준다
# Emp3(SQLModel, table=True) 이것 둘다 적으면 자동으로 만들어 준다
from DTO.EmpDTO import Emp3
from DTO.DeptDTO import Dept3


# FastAPI 애플리케이션 객체 생성
app = FastAPI()

# HTML 템플릿 파일이 들어 있는 폴더 지정
# templates/ 폴더에 있는 HTML 파일들을 Jinja2로 렌더링
templates = Jinja2Templates(directory='templates/')


# ==============================
# 데이터베이스 연결 설정
# ==============================

# DB 연결 주소 형식
# DB종류+드라이버://사용자ID:비밀번호@호스트:포트/DB이름

# MySQL 데이터베이스 연결 정보
# mysql    : 사용할 데이터베이스 종류
# pymysql  : Python에서 MySQL에 연결할 때 사용하는 드라이버
# root     : DB 사용자 ID
# 127.0.0.1:3306 : DB 서버 주소와 포트
# human    : 사용할 데이터베이스 이름
DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'

# 데이터베이스와 통신하기 위한 Engine 객체 생성
# echo=True : 실행되는 SQL문을 콘솔에 출력
engine = create_engine(DATABASE_URL, echo=True)


# 자동 커밋(AUTOCOMMIT)을 사용하는 설정 예시
# 현재는 주석 처리되어 있으므로 실행되지 않음
#
# engine = create_engine(
#     DATABASE_URL,
#     echo=True,
#     execution_options={
#         # 각 SQL문이 자동으로 커밋되는 방식
#         # 일반적인 트랜잭션 rollback으로 변경을 되돌릴 수 없음
#         'isolation_level': 'AUTOCOMMIT'
#     }
# )


# ==============================
# 데이터베이스 세션 관리
# ==============================

# DB 세션을 생성하고 관리하는 함수
# FastAPI의 Depends()를 통해 호출됨
def get_session():

    # Session 객체 생성
    # with 블록이 종료되면 세션이 자동으로 닫힘
    with Session(engine) as session:

        # DB 세션을 라우터 함수에 전달
        # yield 이후 코드는 요청 처리가 끝난 뒤 다시 실행됨
        yield session

        # 세션에서 수행한 DB 변경사항을 저장
        # commit()이 성공하면 트랜잭션이 확정됨
        session.commit()


# ==============================
# 서버 시작 시 실행
# ==============================

# FastAPI 서버가 시작될 때 실행하는 이벤트
@app.on_event('startup')
def on_startup():

    # SQLModel에 등록된 테이블 정보를 기준으로
    # DB에 존재하지 않는 테이블을 생성
    # 기존 테이블을 자동으로 수정하거나 삭제하지는 않음
    SQLModel.metadata.create_all(engine)


# ==============================
# 부서 번호로 직원 조회
# ==============================

# GET /emp/deptno?deptno=30
# URL의 쿼리 파라미터로 부서 번호를 전달받음
@app.get('/emp/deptno')
def emp_list_deptno(

    # 클라이언트의 HTTP 요청 정보
    request: Request,

    # 조회할 부서 번호
    # int 타입이므로 정수 형태로 입력받음
    deptno: int,

    # Depends를 사용하여 DB 세션 주입
    # get_session()에서 생성한 Session을 전달받음
    session: Session = Depends(get_session)
):

    # 조회 결과를 저장할 빈 리스트
    emp_list = []

    try:
        # SQL문 작성
        # text() : 문자열로 작성한 SQL문을
        # SQLAlchemy에서 실행할 수 있는 SQL 객체로 변환
        #
        # :deptno는 바인드 파라미터
        # 실행할 때 실제 deptno 값을 별도로 전달
        sql = text('''
            select *
            from emp3
            where deptno = :deptno
        ''')

        # SQL문 실행
        # {'deptno': deptno}를 이용하여
        # SQL문의 :deptno에 실제 부서 번호 전달
        result = session.execute(sql, {'deptno': deptno})

        # SQL 실행 결과를 가져오는 방법들

        # 모든 결과 행을 가져옴
        # emp_list = result.fetchall()

        # 모든 결과 행을 리스트 형태로 가져옴
        # emp_list = result.all()

        # 각 행을 컬럼명으로 접근할 수 있는
        # RowMapping 객체 형태로 가져옴
        emp_list = result.mappings().fetchall()

        # 조회 결과를 콘솔에 출력
        print(emp_list)

    except Exception as e:

        # SQL 실행 중 오류가 발생하면 콘솔에 출력
        print(e)

    # 조회 결과를 list.html에 전달
    # HTML에서는 emp_list라는 이름으로 데이터 사용 가능
    return templates.TemplateResponse(
        request,
        'list.html',
        {
            'emp_list': emp_list
        }
    )


# ==============================
# 특정 부서 직원의 급여 수정
# ==============================

# GET /emp/update/sal?per=10
# per에는 급여 인상률(%)을 전달
@app.get('/emp/update/sal')
def update_sal(

    # 급여 변경 비율
    # 예: per=10이면 10% 인상
    #     per=-10이면 10% 감소
    per: int,

    # DB 세션 주입
    session: Session = Depends(get_session)
):

    # 백분율을 급여에 곱할 배율로 변환
    # per=10  -> 1.1
    # per=20  -> 1.2
    # per=-10 -> 0.9
    upsal = 1 + (per / 100)

    # 계산된 급여 배율 출력
    print('upsal', upsal)

    try:
        # 직원 급여를 수정하는 UPDATE SQL문
        #
        # sal : 직원 급여 컬럼
        # :upsal : 계산한 급여 배율
        # deptno = 30 : 30번 부서 직원만 수정
        sql = text('''
            update emp3
            set sal = sal * :upsal
            where deptno = 30
        ''')

        # UPDATE SQL문 실행
        # :upsal에 실제 배율 값을 전달
        result = session.execute(sql, {'upsal': upsal})

        # UPDATE문으로 영향을 받은 행의 수 출력
        print('실행 결과로 영향을 받은 row 수 : ', result.rowcount)

        # 변경사항을 DB에 저장
        # 현재는 주석 처리된 상태
        # get_session()의 yield 이후 commit()이 실행됨
        # session.commit()

    except Exception as e:

        # DB 처리 도중 오류가 발생하면 출력
        print('ERR', e)

        # 현재 트랜잭션의 변경사항 취소
        session.rollback()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("02_sqlmodel:app", port=8000, reload=True, host="0.0.0.0")


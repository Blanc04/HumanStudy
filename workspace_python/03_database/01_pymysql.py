# pip install fastapi uvicorn jinja2 pymysql

import pymysql
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

# MySQL 데이터베이스에 연결하는 함수
def get_connect():

    # pymysql을 사용해서 MySQL DB에 연결
    conn = pymysql.connect(
        host="127.0.0.1",              # DB 서버 주소 (현재 내 컴퓨터)
        port=3306,                     # MySQL 기본 포트 번호
        database='human',             # 사용할 데이터베이스 이름
        user='root',                  # DB 접속 계정
        password='human1234$',        # DB 접속 비밀번호

        # 조회 결과를 튜플이 아니라 딕셔너리 형태로 받아오도록 설정
        # 예:
        # {'empno': 7369, 'ename': 'SMITH', ...}
        cursorclass=pymysql.cursors.DictCursor
    )

    # 생성한 DB 연결 객체 반환
    return conn


# 부서번호가 20인 직원 목록을 조회하는 함수
def emp_list_deptno20():

    # get_connect()를 호출해서 DB 연결 객체 가져오기
    connect = get_connect()

    try:
        # DB에서 SQL을 실행할 수 있는 cursor 객체 생성
        # with문을 사용하므로 작업이 끝나면 cursor가 자동으로 정리됨
        with connect.cursor() as cursor:

            # 실행할 SELECT SQL문
            sql = '''
                select * from emp
                where deptno = %s
            '''

            # %s는 실제 값을 넣기 위한 플레이스홀더
            #
            # 문자열에 값을 직접 합쳐서 SQL을 만드는 것이 아니라
            # execute()를 통해 값을 따로 전달하기 때문에
            # 더 안전하게 SQL문을 실행할 수 있음

            # SQL문 실행
            #
            # (20,)은 하나의 값이 들어 있는 튜플
            # SQL의 첫 번째 %s 자리에 20이 들어감
            cursor.execute(sql, (20,))

            # SQL 조회 결과 전체를 가져옴
            #
            # fetchall() : 조회 결과 전체
            # fetchone() : 조회 결과 중 한 행만 가져옴
            emp_list = cursor.fetchall()

            # 조회 결과 확인
            print(emp_list)

    except Exception as e:
        # DB 연결 또는 SQL 실행 중 오류 발생 시 출력
        print(e)

    finally:
        # 성공 여부와 상관없이 DB 연결 종료
        # finally는 try에서 오류가 발생해도 실행됨
        connect.close()


# /emp/deptno 주소로 GET 요청이 들어오면 실행
#
# 예:
# /emp/deptno?deptno=20
@app.get('/emp/deptno')
def emp_list_deptno(

    # URL에서 전달받을 부서 번호
    deptno: int,

    # 현재 HTTP 요청 정보
    request: Request
):
    # DB 연결
    connect = get_connect()

    # 조회 결과를 저장할 빈 리스트
    # SQL 실행에 실패해도 아래 TemplateResponse에서 사용할 수 있도록
    # 미리 빈 리스트로 만들어 둠
    emp_list = []

    try:
        # SQL 실행용 cursor 객체 생성
        with connect.cursor() as cursor:

            # 부서 번호에 따라 직원을 조회하는 SQL문
            sql = '''
                select * from emp
                where deptno = %s
            '''

            # SQL 실행
            #
            # URL로 전달받은 deptno 값을
            # SQL의 %s 플레이스홀더에 전달
            #
            # 예:
            # /emp/deptno?deptno=30
            #
            # 실행 결과:
            # where deptno = 30
            cursor.execute(sql, (deptno,))

            # 조회된 모든 직원 데이터 가져오기
            emp_list = cursor.fetchall()

            # 결과 확인
            print(emp_list)

    except Exception as e:
        # SQL 실행 중 오류가 발생하면 출력
        print(e)

    finally:
        # DB 작업이 끝나면 연결 종료
        connect.close()

    # list.html을 렌더링해서 사용자에게 반환
    #
    # HTML에서는 emp_list라는 변수 이름으로
    # 조회한 직원 목록을 사용할 수 있음
    return templates.TemplateResponse(
        request,
        'list.html',
        {
            'emp_list': emp_list
        }
    )

# emp_list_deptno20()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")

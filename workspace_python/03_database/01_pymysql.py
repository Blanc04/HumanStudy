# pip install fastapi uvicorn jinja2 pymysql

import pymysql
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

def get_connect():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        database='human',
        user='root',
        password='human1234$',
        cursorclass=pymysql.cursors.DictCursor
    )

    return conn

def emp_list_deptno20():
    connect = get_connect()

    try:
        with connect.cursor() as cursor :
        # 연결된 DB에서 sql을 실행할 수 있는 객체를 얻어온다

            sql = '''
                select * from emp
                where deptno = %s
            '''
            # %s : 플레이스홀더
            # 값을 넣을 수 있는 자리
            # 안전한 sql을 만들기 위함

            cursor.execute(sql, (20,))
            # 전달값은 튜플로 작성한다
            # 플레이스홀더에 순서대로 반영된다

            # fetchall : 전체 목록 가져오기
            # fetchone : 맨 위 하나만 가져오기
            emp_list = cursor.fetchall()
            
            
            print(emp_list)
    except Exception as e :
        print(e)
    finally :
        connect.close()

@app.get('/emp/deptno')
def emp_list_deptno(deptno:int, request:Request):
    connect = get_connect()

    emp_list = []
    try:
        with connect.cursor() as cursor :

            sql = '''
                select * from emp
                where deptno = %s
            '''

            cursor.execute(sql, (deptno,))

            emp_list = cursor.fetchall()
            print(emp_list)
    except Exception as e :
        print(e)
    finally :
        connect.close()

    return templates.TemplateResponse(request, 'list.html', {
        'emp_list': emp_list
    })

# emp_list_deptno20()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")

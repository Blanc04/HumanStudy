
# fastapi를 구동하겠다
# 주소를 적어서 메소드를 실행겠다
#   필요하면 전달인자를 받을 수 있다
#   db에 접속해서 sql을 실행하고 결과를 받을 수 있다
#   웹페이지로 결과를 보여줄 수 있다
#       jinja를 쓰자
#       jinja로 sql 결과를 전달할 수 있다
#       jinja에서 받아서 표현할 수 있다

from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from sqlmodel import create_engine, Session
from sqlalchemy import text

from DTO.EmpDTO import Emp3
import traceback

# 서버
app = FastAPI()

# DB 설정
DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'
engine = create_engine(DATABASE_URL, echo=True)

# 템플릿(jinja) 설정
templates = Jinja2Templates(directory='templates/')

def get_session():
    with Session(engine) as session :
        yield session
        session.commit()

@app.get("/list")
def list(
    request:Request,
    session:Session = Depends(get_session) ) :

    try:
        # DB
        # 1. DB 접속
        #     전달 인자의 session:Session = Depends(get_session) ) :

        # 2. sql 준비
        query = text(f'''
            select * from emp3
        ''')
        print('>> 1 >> ', query)

        # 3. 실행
        #   select만 결과가 있다
        result = session.execute(query)
        print('>> 2 >> ', result)

        # 4. 결과 활용
        # emp_list = result.fetchall()
        # print('>> 3 >> fetchall >> ', emp_list)

        emp_list = result.mappings().fetchall()
        print('>> 4 >> .mappings().fetchall() >> ', emp_list)

        return templates.TemplateResponse(request, 'list.html', {
            'emp_list': emp_list
        })

    except Exception as e:
        print(e)
        traceback.print_exc()

        # 500 에러 페이지인데 이쁘게 꾸며놓은 곳으로 보낸다.. 약간의 에러 메세지를 첨부해서

@app.get('/add')
def add(request:Request, count:int = -1) :
    # print('count', count)
    # if count and count > 0 :
    #     print(11111)

    return templates.TemplateResponse(request, 'add.html', {
        'count': count
    })

@app.post('/api/add')
def api_add(
        # empno: int = Form(), # 이거 한번 쓰면 이 다음에 못씀
        request:Request,
        empDTO: Emp3 = Form(),
        session:Session = Depends(get_session),
) :
    # 실행은 되는가?
    print('/api/add 실행')
    # 전달인자들 모두 받았는지 확인
    # print('empno:', empno)
    print('empDTO:', empDTO)

    count = 0
    try:
        # db에 넣기
        query = text('''
            insert into emp3 (empno, ename, job, mgr, hiredate, sal, comm, deptno)
            values (
                :empno,
                :ename,
                :job,
                :mgr,
                :hiredate,
                :sal,
                :comm,
                :deptno
            )
        ''')
        result = session.execute(query, {
            'empno': empDTO.empno,
            'ename': empDTO.ename,
            'job': empDTO.job,
            'mgr': empDTO.mgr,
            'hiredate': empDTO.hiredate,
            'sal': empDTO.sal,
            'comm': empDTO.comm,
            'deptno': empDTO.deptno
        })
        
        # rowcount
        # insert, update, delete등을 통해 
        # 영향을 받은 줄의 수
        count = result.rowcount
        
        # commit : auto commit이 아닌 경우 직접 확정해야 한다
        session.commit()
    except:
        print('오류! except로 빠짐')
        # 오류 추적 내용 출력
        traceback.print_exc()
        
        # 제약 조건 등의 오류 발생 시
        # 모두 되돌리기
        session.rollback()


    # TODO 어디로 갈지 정하자

    # # forward
    # list(request, session)

    # redirect
    print('count : ', count)

    if count == 0 :
        # insert 실패
        return RedirectResponse(
            url=f'/add?count={count}',
            status_code=303
        )
    else :
        # insert 성공
        return RedirectResponse(
            url='/list',
            status_code=303
        )

@app.get('/detail/{empno}')
def detail(
    request:Request, 
    empno:int, 
    session:Session = Depends(get_session)):

    print('/detail/{empno}', empno)

    query = text('''
        select * from emp3
        where empno = :empno
    ''')

    result = session.execute(query, {'empno': empno})
    emp = result.mappings().fetchone()
    print(emp)

    return templates.TemplateResponse(request, 'detail.html', {
        'emp': emp
    })

@app.get('/modify')
def modify(
    request:Request, 
    empno:int, 
    session:Session = Depends(get_session)):


    print('/modify', empno)

    query = text('''
        select * from emp3
        where empno = :empno
    ''')

    result = session.execute(query, {'empno': empno})
    emp = result.mappings().fetchone()
    print(emp)

    return templates.TemplateResponse(request, 'update.html', {
        'emp': emp
    })



@app.post('/api/modify')
def api_modify(
        request:Request,
        empDTO: Emp3 = Form(),
        session:Session = Depends(get_session)
) :
    # 실행은 되는가?
    print('/api/modify 실행')

    count = 0
    try:
        query = text('''
            update 
                emp3
            set 
                ename = :ename,
                job = :job,
                mgr = :mgr,
                hiredate = :hiredate,
                sal = :sal,
                comm = :comm,
                deptno = :deptno
            where
                empno = :empno
        ''')
        result = session.execute(query, {
            'empno': empDTO.empno,
            'ename': empDTO.ename,
            'job': empDTO.job,
            'mgr': empDTO.mgr,
            'hiredate': empDTO.hiredate,
            'sal': empDTO.sal,
            'comm': empDTO.comm,
            'deptno': empDTO.deptno
        })
        count = result.rowcount
        session.commit()
    except:
        print('오류! except로 빠짐')
        traceback.print_exc()
        session.rollback()

    # TODO 어디로 갈지 정하자

    # # forward
    # list(request, session)

    # redirect
    print('count : ', count)

    if count == 0 :
        # update 실패
        return RedirectResponse(
            url=f'/modify?empno={empDTO.empno}',
            status_code=303
        )
    else :
        # insert 성공
        return RedirectResponse(
            url='/list',
            status_code=303
        )

@app.post('/api/delete')
def delete(empno:int = Form(), session:Session = Depends(get_session)) :
    print('/api/delete', empno)

    try :
        query = text('''
            delete from emp3
            where empno = :empno
        ''')
        result = session.execute(query, {'empno': empno})
        count = result.rowcount
        session.commit()
    except:
        print('오류! except로 빠짐')
        traceback.print_exc()
        session.rollback()

    if count == 0 :
        # delete 실패
        return RedirectResponse(
            url=f'/modify?empno={empno}',
            status_code=303
        )
    else :
        # delete 성공
        return RedirectResponse(
            url='/list',
            status_code=303
        )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("03_emp:app", port=8000, reload=True, host="0.0.0.0")




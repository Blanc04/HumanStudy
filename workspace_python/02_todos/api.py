from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> dict :
    return {
        'message': 'Hello World!'
    }

# 주소와 방식이 같은 게 있다면 먼저 선언한 것만 실행됨
@app.get('/html')
def html() :
    return "<h1>hello</h1>"

# @app.get('/html')
# def html2() :
#     return "<h1>hello2</h1>"

@app.post('/html')
def html2() :
    return "<h1>hello2</h1>"

@app.get('/no')
def no() :
    print('들어왔음.')
# return 이 없으면 null을 돌려줌(fastAPI 한정)

# deactivate     
# cd todos
# Scripts\activate
# uvicorn api:app --port 8000 --reload


# webserver에 부여되는 고유 번호 = port
# :80(http) , :443(https) 기본 포트값 기억해야 함

# - venv가상환경에 'todos 폴더' 만들기
# D:\workspace\workspace_python>python -m venv todos

# - 가상환경에 만든 'todos 폴더 경로'로 이동
# D:\workspace\workspace_python>cd todos

# - todos 안에 있는 Scripts 폴더에 activate 실행(가상환경 진입)
# D:\workspace\workspace_python\todos>Scripts\activate

# - activate 상태 확인 (좌측 (todos))
# (todos) D:\workspace\workspace_python\todos>

# - pip에 fastapi 설치
# (todos) D:\workspace\workspace_python\todos> pip install fastapi

# - requirements.txt에 로그처럼 실행한 것이 쌓이도록 진행
# (todos) D:\workspace\workspace_python\todos>pip freeze > requirements.txt

# - 서버 열기 위해 uvicorn pip설치
# (todos) D:\workspace\workspace_python\todos>pip install uvicorn

# - 서버 실행 uvicorn api(파일명):app(실행변수) --port 포트 --reload(데이터 추가 시 새로고침)
# (todos) D:\workspace\workspace_python\todos>uvicorn api:app --port 8000 --reload
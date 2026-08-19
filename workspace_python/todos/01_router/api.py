# ★중요-알아둬야함 (REST, RESTful, REST api _ 백엔드에서 서버를 다뤄봤나요?)
# CRUD와 HTTP 방식의 관계
# c : create - insert - post방식 - /board - /board/add
# r : read - select - get방식 - /board - /board
# u : update - update - put방식 - /board - /board/update
# d : delete - delete - delete방식 - /board - /board/delete

# - 서버 실행 uvicorn api(파일명):app(실행변수) --port 포트 --reload(데이터 추가 시 새로고침)
# (todos) D:\workspace\workspace_python\todos>uvicorn api:app --port 8000 --reload

# FastAPI 서버를 만들기 위한 클래스
from fastapi import FastAPI, Request, Path, HTTPException
# 다른 도메인/포트에서 API 요청을 허용하기 위한 CORS 기능
from fastapi.middleware.cors import CORSMiddleware
# todo.py에서 만든 todo 관련 Router 가져오기
from todo import todo_router
# crud.py에서 만든 crud 관련 Router 가져오기
from crud import crud_router
# FastAPI 애플리케이션 객체 생성
app = FastAPI()

# 크로스 도메인 CORS 해결 코드
# 프론트엔드와 백엔드의 주소/포트가 달라도 요청할 수 있도록 허용
app.add_middleware(
    CORSMiddleware,
    # 모든 출처(origin)에서의 요청 허용
    allow_origins = ["*"],
    # GET, POST, PUT, DELETE 등 모든 HTTP 메서드 허용
    allow_methods = ["*"],
    # 모든 HTTP 헤더 허용
    allow_headers = ["*"]
)

# GET 방식으로 "/" 주소에 요청이 들어왔을 때 실행
@app.get('/')
async def welcome() -> dict :
    # JSON 형태로 응답
    return {
        'message': 'Hello World!'
    }

# todo.py에서 만든 todo_router를 현재 FastAPI 앱에 등록
# todo_router에 정의된 API 주소들을 사용할 수 있게 됨
app.include_router(todo_router)

# crud.py에서 만든 crud_router를 현재 FastAPI 앱에 등록
# crud_router에 정의된 API 주소들을 사용할 수 있게 됨
app.include_router(crud_router)

@app.get('/ip')
def test(req : Request):
    ip = req.client.host
    print(ip)

    return ip

@app.get('/err')
def err():
    print('/err 실행')
    raise HTTPException(
        status_code=400,
        detail='글씨 아무거나 asdofihweo'
    )

@app.get('/html')
def html(): 
    return "<h1>hello world</h1>"

# __name__에는 현재 파이썬 파일이 어떤 방식으로 실행되었는지가 들어감
print(1, __name__)

# 이 파일(api.py)을 직접 실행했을 경우에만 실행
# 직접 실행하면 __name__의 값은 "__main__"
if __name__=="__main__":
    print('이 파일 직접 실행')
    # FastAPI 서버를 실행하기 위한 uvicorn
    import uvicorn
    # api.py의 app 객체를 사용하여 8000번 포트에서 서버 실행
    # reload=True : 코드가 수정되면 서버를 자동으로 재시작
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")
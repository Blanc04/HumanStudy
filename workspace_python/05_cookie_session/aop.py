# pip install fastapi jinja2 uvicorn itsdangerous

from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

from typing import Annotated

from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount(
    "/static", # URL 경로
    StaticFiles(directory="static"), # 실제 폴더명
    name="static" # jinja에서 사용할 이름
)

EXCLUDE_PATH = [
    '/join',
    '/login',
]

@app.middleware('http')
async def login_check(request: Request, call_next):

    # 로그인 검사 제외
    url_path = request.url.path
    print('url_path', url_path)
    # if url_path != '/login' :
    #     return await call_next(request)
    if url_path not in EXCLUDE_PATH or not url_path.startswith('/static'):
        # 제외 경로거나
        # /static으로 시작한다면
        # 그냥 통과
        return await call_next(request)
    else :

        # 세션에 로그인 정보가 없으면 로그인 페이지로 이동
        isLogin = request.session.get('isLogin', None)
        # if not isLogin :
        # if not isLogin is None :
        if 'isLogin' in request.session :
            return RedirectResponse(
                url='/login',
                status_code = 302
            )
        else :
            # 그렇지 않으면 원래 하려던 일 계속 하기
            return await call_next(request)

app.add_middleware(
    SessionMiddleware,
    secret_key='Human1234$'
)

templates = Jinja2Templates(directory='templates/')

@app.get('/login')
def login(request: Request):
    # 세션 저장
    request.session['isLogin'] = True
    request.session['id'] = "admin"

@app.get('/mypage')
def mypage(request:Request):
    # isLogin = request.session.get('isLogin', None)
    id = request.session.get('id', None)
    # if isLogin is None :
    #     return "로그인 필요"
    # else :
    #     return f"id: [{id}] 비밀스러운 공간에 오신 걸 환영합니다."
    return f"id: [{id}] 비밀스러운 공간에 오신 걸 환영합니다."

@app.get('/logout')
def logout(request: Request):
    request.session.clear();

    return "로그아웃"

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(request, 'main.html')

if __name__=="__main__":
    import uvicorn
    uvicorn.run('aop:app', port=8000, reload=True, host="0.0.0.0")
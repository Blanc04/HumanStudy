from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

@app.get('/hello')
def hello(request: Request) :
    print('/hello 실행')
    return templates.TemplateResponse(request, 'home.html',{
        'ip': request.client.host,
        'msg':'안뇽?'
    })

if __name__=="__main__":
    # FastAPI 서버를 실행하기 위한 uvicorn
    import uvicorn
    # api.py의 app 객체를 사용하여 8000번 포트에서 서버 실행
    # reload=True : 코드가 수정되면 서버를 자동으로 재시작
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")
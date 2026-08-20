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

@app.get('/youtube')
def youtube(request: Request) :
    print('/youtube 실행')
    return templates.TemplateResponse(request, 'youtube.html', {
        'like': 3,
        'star': 4,
        'bookmark': ['동영상1', '동영상2', '동영상3', '동영상4', '동영상5']
    })

def price(value) :
    return f'{int(value):,}'

templates.env.filters['price'] = price

# 날짜 포멧
from datetime import datetime
def format_data(value, format='%Y-%m-%d %H:%M:%S'):
    v = datetime.fromisoformat(value)
    return v.strftime(format)
templates.env.filters['format_data'] = format_data

# textarea의 엔터 문자인 \n을 <br>로 바꾸고 HTML로 인식 시키는 필터
def n2br(value):
    from markupsafe import Markup # innerHTML로 만들어 주는 모듈
    return Markup(value.replace('\n', '<br>'))
templates.env.filters['n2br'] = n2br

if __name__=="__main__":
    # FastAPI 서버를 실행하기 위한 uvicorn
    import uvicorn
    # api.py의 app 객체를 사용하여 8000번 포트에서 서버 실행
    # reload=True : 코드가 수정되면 서버를 자동으로 재시작
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")
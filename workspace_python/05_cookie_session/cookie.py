# pip install fastapi jinja2 uvicorn

from fastapi import FastAPI, Cookie, Request, Response
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get('/main')
def main(
    request: Request,    # 현재 클라이언트의 요청(Request) 정보
    response: Response,  # 응답(Response) 객체

    # 클라이언트가 보낸 쿠키 중 이름이 "no"인 쿠키를 가져옴
    # 해당 쿠키가 없으면 None
    no: str | None = Cookie(None),

    # 클라이언트가 보낸 쿠키 중 이름이 "yes"인 쿠키를 가져옴
    # Annotated를 사용해서 Cookie 값이라는 것을 FastAPI에게 알려줌
    # 쿠키가 없으면 None
    yes: Annotated[str | None, Cookie()] = None,
):
    # 받아온 쿠키 값 확인
    print('no: ', no)
    print('yes: ', yes)

    # main.html을 렌더링한 새로운 Response 객체 생성
    # 위에서 매개변수로 받은 response 대신
    # TemplateResponse 객체를 response 변수에 다시 저장함
    response = templates.TemplateResponse(
        request,
        'main.html'
    )

    # 쿠키 생성
    # 브라우저에 key=value 형태로 저장됨
    response.set_cookie(
        key='key',
        value='value'
    )

    # 10초 동안 유지되는 쿠키 생성
    # max_age는 쿠키가 유지되는 시간을 초 단위로 지정
    response.set_cookie(
        key='key2',
        value='value2',
        max_age=10  # 10초 후 만료
    )

    # 1000초 동안 유지되는 쿠키 생성
    response.set_cookie(
        key='key3',
        value='value3',
        max_age=1000,

        # JavaScript의 document.cookie 등을 이용해서
        # 이 쿠키에 접근할 수 없도록 설정
        # 보안상 중요한 쿠키에 주로 사용
        httponly=True
    )

    # 쿠키 설정이 포함된 HTML 응답을 클라이언트에게 반환
    return response


# /donate/cookie 주소로 GET 요청이 들어오면 실행
@app.get('/donate/cookie')
def delete_cookie(response: Response):

    # 브라우저에 저장된 특정 쿠키 삭제
    response.delete_cookie('key3')

    # 쿠키 삭제 후 메시지 반환
    return '{"message":"쿠키 key3 삭제 완료"}'

@app.get('/donate/cookie')
def delete_cookie(response: Response):
    response.delete_cookie('Key3')
    return '{"message":"쿠키 key3 삭제 완료"}'

if __name__=="__main__":
    import uvicorn
    uvicorn.run('cookie:app', port=8000, reload=True, host="0.0.0.0")
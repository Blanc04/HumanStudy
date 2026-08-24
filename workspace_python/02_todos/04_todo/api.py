from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

todo_list = [{
        'id': 1,
        'item': '파이썬 공부'
    }, {
        'id': 2,
        'item': 'Jinja 공부'
    }]

# 전체 목록 페이지
# GET 방식으로 /jinjatodo 주소에 접속했을 때 실행
@app.get('/jinjatodo')
def jinjatodo(request: Request):
    # home.html 템플릿을 렌더링해서 응답
    # todo_list를 Jinja에서 사용할 수 있도록 전달
    return templates.TemplateResponse(request, 'home.html', {
            'todo_list': todo_list
        })

# 추가 페이지
# GET 방식으로 /jinjatodo/add 주소에 접속했을 때 실행
@app.get('/jinjatodo/add')
def add_page(request: Request):
    # add.html 템플릿을 렌더링해서 응답
    return templates.TemplateResponse(request, 'add.html')

# TODO 추가
# '/jinjatodo/add' 주소로 POST 요청이 들어왔을 때 실행
# HTML form의 name="item" 값을 Form()으로 받아옴
@app.post('/jinjatodo/add')
def add_todo(item: str=Form()):
    # 새로운 TODO에 사용할 id 생성
    # todo_list가 비어있다면
    if len(todo_list) == 0:
        # 첫 번째 TODO이므로 id를 1로 설정
        new_id = 1
    # todo_list에 기존 TODO가 하나 이상 있다면
    else:
        # todo_list에 있는 모든 todo의 id 중 가장 큰 값을 찾고
        # 거기에 1을 더해서 새로운 id 생성
        new_id = max(todo['id'] for todo in todo_list) + 1
    # 새로 추가할 TODO를 딕셔너리 형태로 생성
    todo = {
        # 위에서 자동으로 생성한 id 저장
        'id': new_id,
        # HTML form에서 전달받은 TODO 내용 저장
        'item': item
    }
    todo_list.append(todo)
    # 추가 완료 후 전체 조회로 이동
    return RedirectResponse(
        url='/jinjatodo',
        status_code=303
    )

# 상세 조회
@app.get('/jinjatodo/{todo_id}')
def detail_todo(request: Request, todo_id: int):
    for todo in todo_list:
        if todo['id'] == todo_id:
            return templates.TemplateResponse(request, 'detail.html', {
                    'todo': todo
                })
    return {
        'message': '존재하지 않는 항목입니다.'
    }

# 수정 페이지
@app.get('/jinjatodo/{todo_id}/edit')
def edit_page(request: Request, todo_id: int):
    for todo in todo_list:
        if todo['id'] == todo_id:
            return templates.TemplateResponse(request, 'edit.html', {
                    'todo': todo
                })
    return {
        'message': '존재하지 않는 항목입니다.'
    }

# 수정
@app.post('/jinjatodo/{todo_id}/edit')
def edit_todo(todo_id: int, item: str=Form()):
    for todo in todo_list:
        if todo['id'] == todo_id:
            todo['item'] = item
            break
    # 수정 완료 후 전체 조회
    return RedirectResponse(
        url='/jinjatodo',
        status_code=303
    )

# 삭제
@app.post('/jinjatodo/{todo_id}/delete')
def delete_todo(todo_id: int):
    for i in range(len(todo_list)):
        if todo_list[i]['id'] == todo_id:
            todo_list.pop(i)
            break
    # 삭제 완료 후 전체 조회
    return RedirectResponse(
        url='/jinjatodo',
        status_code=303
    )

# 서버 실행
if __name__=="__main__":
    # FastAPI 서버를 실행하기 위한 uvicorn
    import uvicorn
    # api.py의 app 객체를 사용하여 8000번 포트에서 서버 실행
    # reload=True : 코드가 수정되면 서버를 자동으로 재시작
    uvicorn.run('api:app', port=8000, reload=True)
# API 주소들을 따로 관리하기 위한 APIRouter
# Form : form 데이터 받기
# Request : 요청 방식(GET, POST 등), 파라미터 등을 직접 확인할 때 사용
from fastapi import APIRouter, Form, Request

# todo 관련 API를 묶어서 관리할 Router 생성
todo_router = APIRouter()

# Todo 데이터를 임시로 저장할 리스트
# 서버가 종료되면 데이터도 사라짐
todo_list = []

# POST 방식으로 "/todo" 요청을 받음
# 요청 Body에서 JSON 형태의 데이터를 dict로 받음
@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    print('todo:', todo)

    # 전달받은 todo를 리스트에 추가
    todo_list.append(todo)

    return {
        'message': 'Todo added successfully.'
    }

# GET 방식으로 "/todo" 요청을 받음
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    # 현재 저장된 todo 목록 반환
    return {
        'todos': todo_list
    }

# GET 방식으로 Query Parameter 받기
# 예) /todo/param?id=1&item=study
@todo_router.get("/todo/param")
async def todoParamGet(id: int, item:str) -> dict:
    print(id, item)

    return {
        'id': id,
        'item': item
    }

# POST 방식으로 Form 데이터 받기
@todo_router.post("/todo/param")
async def todoParamPost(id: int = Form(), item:str = Form()) -> dict:
    print(id, item)

    return {
        'id': id,
        'item': item
    }

# 같은 주소에서 GET, POST, PUT, DELETE 방식 모두 처리
@todo_router.get("/todo/param2")
@todo_router.post("/todo/param2")
@todo_router.put("/todo/param2")
@todo_router.delete("/todo/param2")
async def todoParam(req:Request) -> dict:

    # GET 방식은 데이터를 Query Parameter로 받음
    if req.method == "GET":
        data = req.query_params

    # POST, PUT, DELETE는 Form 데이터로 받음
    else :
        data = await req.form()

    # 전달받은 데이터에서 id와 item 값 가져오기
    id = data.get('id')
    item = data.get('item')

    # 전달받은 값과 현재 HTTP 요청 방식 확인
    print(id, item, req.method)
    
    return {
        'id': id,
        'item': item
    }

# todo.py가 import 되었는지 직접 실행되었는지 확인
print(2, __name__)

# todo.py 파일을 직접 실행했을 때만 실행
# 직접 실행하면 __name__ == "__main__"
if __name__=="__main__":
    print('todo.py 파일 직접 실행')





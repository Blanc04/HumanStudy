# crud.py
# API 주소들을 따로 관리하기 위한 APIRouter 가져오기
from fastapi import APIRouter, Form, Request
from pydantic import BaseModel
class Todo(BaseModel) :
    id: int
    item: str

# CRUD 관련 API들을 묶어서 관리할 Router 생성
crud_router = APIRouter(prefix='/crud')
# Todo 데이터를 임시로 저장할 리스트
# 서버를 종료하면 저장된 데이터도 사라짐
todo_list = []

# Create
# POST 방식으로 '/crud' 요청을 받음
@crud_router.post('/crud')
async def create_todo(id: int = Form(), item: str = Form()):
    if id <= 0:
        return {
            'message': '유효하지 않은 id입니다.'
        }
    for todo in todo_list:
        if todo.get('id') == id:
            return {
                'message': '이미 존재하는 id입니다.'
            }
    todo = {
        'id': id,
        'item': item
    }
    todo_list.append(todo)
    return {
        'todo': todo
    }

# Read
# GET 방식으로 '/crud' 요청을 받음
@crud_router.get('/crud/all')
def read_todo():
    return {
        'todos': todo_list
    }
@crud_router.get('/crud')
async def read_todo(id: int):
    # todo_list에 저장된 데이터를 하나씩 확인
    for todo in todo_list:
        # 전달받은 id와 같은 id를 가진 todo를 찾음
        if todo.get('id') == id:
            return {
                'todo': todo
            }
    # 같은 id를 가진 todo가 없으면 메시지 반환
    return {
        'message': '해당 id가 없습니다.'
    }

# Update
# PUT 방식으로 '/crud' 요청을 받음
@crud_router.put('/crud')
# 수정할 id와 item이 담긴 JSON 데이터를 dict로 받음
async def update_todo(todo: dict):
    # todo_list에 저장된 데이터를 하나씩 확인
    for todo in todo_list:
        # 기존 데이터의 id와 전달받은 todo의 id가 같은지 확인
        if todo.get('id') == todo.get('id'):
            # id가 같으면 기존 item을 전달받은 새로운 item으로 수정
            todo['item'] = todo.get('item')
    # 수정 후 전체 todo_list 반환
    return {
        'todos': todo_list
    }

# Delete
# DELETE 방식으로 '/crud' 요청을 받음
# id는 Query Parameter로 전달받음
@crud_router.delete('/crud')
async def delete_todo(id: int):
    # todo_list의 길이만큼 index 번호를 반복
    for todo in range(len(todo_list)):
        # 현재 index에 있는 데이터의 id와 전달받은 id가 같은지 확인
        if todo_list[todo]['id'] == id:
            # 해당 index의 데이터를 todo_list에서 삭제
            todo_list.pop(todo)
            # 삭제가 끝났으므로 반복문 종료
            break
    # 삭제 후 전체 todo_list 반환
    return {
        'todos': todo_list
    }

# Create 주석
# @crud_router.post('/crud')
# # 요청 Body에서 JSON 데이터를 dict 형태로 받음
# def create_todo(todo: dict):
#     # 전달받은 todo 딕셔너리를 todo_list에 추가
#     crud_list.append(todo)
#     # 추가한 todo를 응답으로 반환
#     return {
#         'todo': todo
#     }

# async def create_todo(request: Request):
#     data = await request.form()
#     id = data.get('id')
#     item = data.get('item')
#     return id, item

# async def create_todo(todo: Todo = Form()):
#     id = data.get('id')
#     item = data.get('item')
#     return id, item
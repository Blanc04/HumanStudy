from fastapi import APIRouter, Form, Request, Depends
from pydantic import BaseModel
from typing import Annotated, Optional

class Todo3(BaseModel) : 
    # 기본적으로 json만 받음
    id: int = -1
    item: str = ''


crud_router = APIRouter()
# crud_router = APIRouter( prefix='/crud' )

todo_list = []

@crud_router.post('/crud/c')
# 실패 : json 형식으로 들어오지 않아서 
# def crud_c(todo:dict) :

# # 성공
# def crud_c(id : int = Form(), item:str = Form()) :
#     print(id, item)

#     return id, item

# # 성공
# async def crud_c(request: Request) :
#     data = await request.form()
#     id = data.get('id')
#     item = data.get('item')
#     print(1, id, item)

#     return id, item

# # 실패 : json 형식으로 들어오지 않아서 
# async def crud_c(todo3: Todo3) :
#     id = todo3.id
#     item = todo3.item
#     print(2, id, item)

#     return id, item

# # 성공
# async def crud_c(todo3: Todo3 = Form()) :
#     id = todo3.id
#     item = todo3.item
#     print(2, id, item)

#     return id, item

# 성공
# 위의 것과 같은 내용을 Annotated로 사용한 경우
async def crud_c(todo3: Annotated[Todo3, Form()]) :
    id = todo3.id
    item = todo3.item
    print(3, id, item, todo3)

    todo_list.append(todo3)

    return id, item

@crud_router.get('/crud')
async def crud() :
    print('/crud 실행')
    print(4, todo_list)

    return todo_list

# id를 전달받고
# 목록 중에 id가 같은 녀석만 return
@crud_router.get('/crud/r')
# # 성공
# # # -> Optional[Todo3] :
# # #    필수는 아니다
# # async def crud_r(id: int) -> Optional[Todo3] :
# #  -> Todo3 | None
# #     결과값이 Todo3 또는 None 인지 검증하라
# async def crud_r(id: int) -> Todo3 | None:
#     print('/crud/r')
#     print(5, 'id:', id)

#     # result = Todo3()
#     result = None
#     for todo in todo_list:
#         if todo.id == id:
#             print(todo)
#             # return todo
#             result = todo

#     return result

# # 성공
# async def crud_r(request: Request) -> Todo3 | None:
#     print('/crud/r')

#     data = request.query_params
#     id = data.get('id', -1)

#     print(5, 'id:', id)

#     # result = Todo3()
#     result = None
#     for todo in todo_list:
#         if todo.id == id:
#             print(todo)
#             # return todo
#             result = todo

#     return result

# 성공
# html에서 form으로 보낼 때 pydantic으로 받는 법
# post : Form()
# get : Depends()
async def crud_r(todo3: Annotated[Todo3, Depends()]) -> Todo3 | None:
    print('/crud/r')
   
    id = todo3.id

    print(5, 'id:', id)

    # result = Todo3()
    result = None
    for todo in todo_list:
        if todo.id == id:
            print(todo)
            # return todo
            result = todo

    return result


@crud_router.get('/crud/r/{id}')
def crud_r_id(id:int) :
    print('/crud/r/'+str(id))
    print(6, 'id:', id)

    # result = Todo3()
    result = None
    for todo in todo_list:
        if todo.id == id:
            print(todo)
            # return todo
            result = todo

    return result

##############
## ajax 전용
##############

@crud_router.post('/crud/api/c')
def crud_api_c(todo3: Todo3):
    print('/crud/api/c')
    print(todo3)

    todo_list.append(todo3)

    return todo3

@crud_router.get('/crud/api/r')
def crud_api_c():
    print('/crud/api/r')
    print(todo_list)
    return todo_list

@crud_router.get('/crud/api/r/{id}')
def crud_api_c(id:int):
    print('/crud/api/r/id')

    result = None
    for todo in todo_list:
        if todo.id == id:
            print(todo)
            # return todo
            result = todo

    return result

@crud_router.put('/crud/api/u')
# @crud_router.post('/crud/api/u')
def crud_api_u(todo3: Todo3):
    print('/crud/api/u', todo3)

    for todo in todo_list:
        if todo.id == todo3.id:
            todo.item = todo3.item

@crud_router.delete('/crud/api/d')
def crud_api_delete(todo3: Todo3):
    print('/crud/api/d', todo3)

    for i in range(len(todo_list)) :
        print('i', i)
        if todo_list[i].id == todo3.id:
            todo_list.pop(i)
            break


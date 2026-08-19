todo_list = []

d1 = {
    'id': 1,
    'item': 'item1'
}

# d1을 리스트에 추가
todo_list.append(d1)
print(todo_list)

d2 = {
    'id': 29681,
    'item': 'item2'
}
todo_list.append(d2)
print(todo_list)

# Read
# id가 29681인 것의 딕셔너리 출력
print(todo_list[1])

for i in todo_list :
# print(i.get('id'))
    if i.get('id') == 29681 :
        print(i)

# id가 29681인 것의 item을 '아이템2'로 바꾼 뒤 todo_list 출력
for i in todo_list :
# print(i.get('id'))
    if i.get('id') == 29681 :
        i['item'] = '아이템2'
print(todo_list)

for i in range(len(todo_list)):
    print('i', i)
    if todo_list[i]['id'] == 29681:
        todo_list.pop(i)
        break
print(todo_list)

# crud.py
# todo_list에 CRUD하는 라우터를 설정하고
# api.py를 실행해서 테스트하기
# 문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
# 문제1-1 : 짝수만 따로 리스트로 만들어서 출력
q1And1 = []
for i in range(len(numbers)):
    if (numbers[i]%2 == 0):
        q1And1.append(numbers[i])
    print(q1And1)
# 문제1-2 : 홀수의 합
q1And2 = []
for i in range(len(numbers)):
    if (numbers[i]%2 == 1):
        q1And2.append(numbers[i])
    print(sum(q1And2))
# 문제1-1 : 짝수만 따로 리스트로 만들어서 출력
q1And1 = []
for i in numbers:
    if (i%2 == 0):
        q1And1.append(i)
    print(q1And1)
# 문제1-2 : 홀수의 합
q1And2 = []
for i in numbers:
    if (i%2 == 1):
        q1And2.append(i)
    print(sum(q1And2))

# 문제 2
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
# 다 샀을 때 가격은?
total = 0
for i in cart:
    # cart[i]에서 가격과 개수를 꺼내서
    cart[i]['가격']
    cart[i]['개수']
    # 가격 × 개수를 total에 더하기
    total = total + cart[i]['가격'] * cart[i]['개수']
print(total)

# 문제3
# UP/DOWN 게임 만들기
# 단, 맞추면 몇번째에 맞췄는지도 출력
# import random
# q3 = random.randint(1, 100)
# count = 0
# while True:
#     # 사용자에게 숫자를 입력받기
#     num = int(input('숫자 입력: '))
#     # 시도 횟수 1 증가
#     count = count + 1
#     # 입력한 숫자가 정답보다 작은 경우
#     if num < q3:
#         print('UP')
#     # 입력한 숫자가 정답보다 큰 경우
#     elif num > q3:
#         print('DOWN')
#     # 위의 두 경우가 아니라면 정답
#     else:
#         print('정답!')
#         print(count, '번째 만에 맞췄습니다.')
#         # 반복문 종료
#         break

# 문제4
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
# 이런 경우 
# id/pw를 입력 받거나 변수에 넣어두고
# id/pw가 맞는지 틀리는지 판단해서
# "아이디가 틀립니다", "비번이 틀립니다", "로그인 성공"
# user_id = input('아이디: ')
# user_pw = input('비밀번호: ')
# if not user_id in users:
#     print('아이디가 틀립니다')
# elif user_pw != users[user_id]:
#     print('비번이 틀립니다')
# else:
#     print('로그인 성공')

# 문제5
# 랜덤 투표 시스템
# 한번에 a, b, c 대상에 랜덤으로 투표
import random
# 랜덤 넣기용 인덱스
q5and1 = ['a', 'b', 'c']
# 값 추가와 대입용 딕셔너리
result = {
    'a': 0,
    'b': 0,
    'c': 0
}
# 문제5-1 : 100번의 투표 결과를 출력하시오
for i in range(100):
    # 히히 a b c 셋 중에 랜덤으로 마구 넣어볼까?
    q5 = q5and1[random.randint(0, 2)]
    # 여기서 [q5]는 사람의 투표 수량이야~
    result[q5] += 1
    print(q5)
# 문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력
maxName = ''
maxCount = 0
# 키와 값을 동시에 가져와서 모두 비교해^^
for name, count in result.items():
    if count > maxCount:
        maxName = name
        maxCount = count
print('최다 득표자:', maxName)
print('득표 수:', maxCount)

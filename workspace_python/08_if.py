a = 10
b = 5
print(3 < b < a < 20)

if True : 
    print(1)
    # print(2)
    print(3)

    if True :
        print(4)

if True :
    pass
else :
    pass

if 1 :
    print('참')


'''
파이썬에서 False란?
False, None, 0.0, 빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리)
'''

a = []
if a :
    print('참')
else :
    print('거짓')

q1 = [89, 72, 93, 82]
q1Av = sum(q1) / len(q1)
if(0 <= q1[0] <= 100) \
    and(0 <= q1[1] <= 100) \
    and(0 <= q1[2] <= 100) \
    and(0 <= q1[3] <= 100) :
    if q1Av >= 80 :
        print('합격')
    else :
        print('불합격')
else :
    print('잘못된 입력')

q2 = int(input(1))
if q2 == 1:
    print('콜라')
elif q2 == 2:
    print('사이다')
elif q2 == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

# break 필요 없음
# or은 | (파이프)

a = 8
match a :
    case '봄' :
        print('봄')
    case 6 | 7 | 8 :
        print('여름')
    case _ :
        print('그 외')
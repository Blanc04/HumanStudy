for i in range(5):
    print(i, end=' ')
print()
for i in reversed(range(5)):
    print(i, end=' ')
print()
l = 10
# 2단부터 9단까지 3단씩 묶어서 반복
# i 값은 2, 5, 8 순서로 변함
for i in range(2, l, 3):
    # 각 단에 곱할 숫자를 1부터 9까지 반복
    for j in range(1, 10):
        # 현재 start부터 3개의 단을 반복
        for k in range(i, i + 3):
            # 구구단은 9단까지만 출력해야 하므로
            # i가 10보다 작을 때만 출력
            if k < l:
                print(f'{k}x{j}={j*k}', end='\t')
        print()
        # 3개의 단이 모두 끝나면 한 줄을 더 띄움
    print()

import random
print(random.random())
print(random.randint(1, 6))

dice = random.randint(1, 6)
count = 0
while dice != 3:
    dice = random.randint(1, 6)
    count += 1
    print(f'{count}번째 주사위: {dice}')
    if dice == 3:
        break
print(f'3은 {count}번 만에 나왔습니다.')

# import turtle as t
# t.shape('turtle')

while True :
    print(1)


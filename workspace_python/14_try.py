def div(x, y):
    if y != 0:
        result = x / y
    else:
        print('두 번째 숫자는 0이 올 수 없습니다.')
    return result

def div2(x, y):
    result = 0
    try:
        result = x / y
    except:
        print('예외 발생')
    return result

def div3(x, y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError:
        print('0 넣지 마라.')
    except TypeError:
        print('숫자만 넣어라.')
    return result

def div4(x, y):
    result = 0
    try:
        result = x / y
    except ZeroDivisionError as e: # 예외 메시지
        print('0 넣지 마라.', e)
    except TypeError as e:
        print('숫자만 넣어라.', e)
    return result

def div5(x, y):
    result = 0
    try:
        result = x / y
    except Exception as e: # 부모 예외 메시지
        print('예외 발생.', e)
    return result

def div6(x, y):
    result = 0
    try:
        result = x / y
    except Exception as e: # 부모 예외 메시지
        print('예외 발생.', e)
    else:
        print('문제 없었다')
    return result

def div7(x, y):
    result = 0
    try:
        result = x / y
    except Exception as e: # 부모 예외 메시지
        print('예외 발생.', e)
    else:
        print('문제 없었다')
    finally:
        print('무조건 실행') # 무조건 실행, 심지어 return을 해도 실행
    return result

a = div(7, 3)
print(a)

# a = div(7, 0)
a = div2(7, 0)
a = div2(7, '3')
print(a)

a = div3(7, 0)
a = div3(7, '3')

a = div4(7, 0)
a = div4(7, 'a')

a = div5(7, 0)
a = div5(7, 'a')

a = div6(7, 0)
a = div6(7, 2)

a = div7(7, 0)
a = div7(7, 2)

# raise Exception('메시지')

def loginCheck(id, pw):
    if id == 'admin' and pw == '1234':
        print('Login Successful')
        return 0
    elif id == '' :
        print('Please type your id')
        return 1

def login():
    id = 'admin'
    pw = '1234'
    result = loginCheck(id, pw)

    if result == 0:
        print('Go to Mainpage')
    elif result == 1:
        print('alert(type your id)')

login()

def loginCheck2(id, pw):
    if id == 'admin' and pw == '1234':
        print('Login Successful')
        return 0
    elif id == '' :
        print('Please type your id')
        raise Exception('code:1')

def login2():
    id = ''
    pw = '1234'
    try:
        result = loginCheck2(id, pw)
        if result == 0:
            print('Go to Mainpage')
    except Exception as e:
        print(e)
        if e == 'code:1':
            print('alert(type your id)')

login2()

import traceback
try:
    a = 3 / 0
except Exception as e:
    print(e)
    traceback.print_exc()
    a = traceback.format_exc()
    print('-'*30)
    print(a)
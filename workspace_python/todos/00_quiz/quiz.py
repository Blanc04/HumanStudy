from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .todo import todo_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn 01_router.00_quiz.quiz:app --port 8000 --reload

# 문제 1
# 브라우저에서
# - input에 몇 단입력
# 파이썬에서
# - 해당 구구단의 단 출력
@app.get('/dan')
def gugudan(dan: int):
    for i in range(1, 10):
        print(dan, '*', i, '=', dan * i)
    return {
        'dan': dan
    }

# 문제 2
# 클라이언트에서
# - 숫자 두 개를 입력
# 파이썬에서
# - 두 개의 합을 출력
@app.get('/plus')
def plus(num1:int, num2:int):
        print(num1, '+', num2, '=', num1 + num2)
        return {
        'plus': num1 + num2
    }

# 문제 3
# 웹에서
# - 숫자 2개와 연산자를 입력
# - 2, "-", 3
# 파이썬에서
# - 결과 출력
# - 화면에도 출력
@app.get('/calc')
def calc(x:int, y:int, op):
    print(f'x:{x}, y:{y}, op:{op}')
    resule = 0
    if op == '+':
        result = x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    elif op == '/':
        result = x/y

    print(result)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('quiz:app')
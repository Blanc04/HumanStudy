# w : 수정 가능
# 'w'는 쓰기 모드이며, 파일이 없으면 새로 만든다.
# 파일이 이미 있으면 기존 내용을 모두 지우고 처음부터 다시 작성한다.
file = open('hello.txt', 'w')
# hello.txt 파일에 문자열을 작성한다.
# \n은 줄바꿈을 의미한다.
file.write('eng\n123\n한글')
# 파일 출력 버퍼에 남아 있는 내용을 즉시 파일에 반영한다.
file.flush() # 버퍼가 꽉 차지 않아도 내보내기
             # 즉시 반영
# 사용이 끝난 파일을 닫는다.
# close()를 실행할 때도 버퍼의 내용이 파일에 반영된다.
file.close()

# 한글 캐릭터셋
# utf-8, euc-kr, cp949
# encoding은 파일에서 사용할 문자 인코딩 방식을 지정한다.
# utf-8은 한글을 포함한 여러 언어를 표현할 수 있는 범용 인코딩이다.
file = open('hello2.txt', 'w', encoding='utf-8')
# UTF-8 방식으로 문자열을 파일에 작성한다.
file.write('eng\n123\n한글')
# 사용이 끝난 파일을 닫는다.
file.close()

# r : 읽기 전용
# hello.txt 파일을 읽기 모드로 연다.
# 읽기 모드는 파일이 존재하지 않으면 FileNotFoundError가 발생한다.
file = open('hello.txt', 'r')
# read()는 파일의 전체 내용을 문자열로 읽어온다.
s = file.read()
# 사용이 끝난 파일을 닫는다.
file.close()
# 파일에서 읽어온 문자열을 출력한다.
print(s)

# '-'를 20번 반복하여 구분선을 출력한다.
print('-'*20)

# UTF-8로 저장한 hello2.txt 파일을 UTF-8 방식으로 읽는다.
file = open('hello2.txt', 'r', encoding='utf-8')
# 파일의 전체 내용을 문자열로 읽어온다.
s = file.read()
# 사용이 끝난 파일을 닫는다.
file.close()
# 읽어온 내용을 출력한다.
print(s)

# 구분선을 출력한다.
print('-'*20)

# hello.txt 파일을 읽기 모드로 연다.
file = open('hello.txt', 'r')
# read(6)은 현재 위치부터 최대 6개의 문자를 읽는다.
# s = file.read(6)
# read(10)은 현재 위치부터 최대 10개의 문자를 읽는다.
# 텍스트 모드에서는 글자 수를 기준으로 읽는다.
s = file.read(10)
# 사용이 끝난 파일을 닫는다.
file.close()
# 읽어온 최대 10개의 문자를 출력한다.
print(s)

# 구분선을 출력한다.
print('-'*20)

# buffering은 파일 입출력에 사용할 버퍼 방식을 지정한다.
# buffering=1은 텍스트 쓰기 작업에서 줄 단위 버퍼링을 의미한다.
# 현재 코드는 읽기 모드이므로 파일을 한 줄씩 읽게 만드는 기능은 아니다.
file = open('hello.txt', 'r', buffering=1)
# 파일의 전체 내용을 읽는다.
s = file.read()
# 사용이 끝난 파일을 닫는다.
file.close()
# 읽어온 내용을 출력한다.
print(s)

# 구분선을 출력한다.
print('-'*20)

# 파일에서 나누어 읽은 문자열을 합쳐서 저장할 변수이다.
text = ''
# hello.txt 파일을 읽기 모드로 연다.
file = open('hello.txt', 'r')
# 파일의 끝에 도달할 때까지 반복한다.
while True :
    # 현재 위치부터 문자를 2개씩 읽는다.
    chunk = file.read(2)
    # 파일의 끝에 도달하면 read()가 빈 문자열을 반환한다.
    # 빈 문자열은 False로 판단되므로 반복문을 종료한다.
    if not chunk :
        break
    # 읽어온 문자열을 text 변수 뒤에 이어 붙인다.
    text += chunk
    # 현재 읽어온 2개의 문자를 출력한다.
    print(chunk)
# 사용이 끝난 파일을 닫는다.
file.close()
# 2개씩 읽어서 합친 전체 문자열을 출력한다.
print(text)

# rb는 바이너리 읽기 모드이다.
# 이미지, 음악, 동영상 등의 파일을 읽을 때 사용한다.
file = open('a.webp', 'rb')
# 바이너리 파일 전체를 bytes 자료형으로 읽는다.
s = file.read()
# 사용이 끝난 파일을 닫는다.
file.close()
# 이미지 자체가 아니라 이미지 파일을 구성하는 바이트 데이터를 출력한다.
print(s)

# 일반적인 open()과 close()를 이용한 파일 읽기 방식이다.
file = open('hello.txt', 'r')
# 파일의 전체 내용을 읽는다.
s = file.read()
# 직접 파일을 닫아야 한다.
file.close()
# 읽어온 내용을 출력한다.
print(s)

# with문을 사용하면 내부 코드가 끝났을 때 파일이 자동으로 닫힌다.
# 따라서 file.close()를 따로 작성하지 않아도 된다.
with open('hello.txt', 'r') as file :
    # 파일의 전체 내용을 읽는다.
    s = file.read()
    # 읽어온 내용을 출력한다.
    print(s)

# 파일에 저장할 리스트이다.
a = [1,2,3,4]
# array1.text 파일을 쓰기 모드로 연다.
# with문이 끝나면 파일은 자동으로 닫힌다.
with open('array1.text', 'w') as file :
    # file 객체 자체를 문자열로 바꾸는 코드이다.
    # 리스트 a를 저장하는 코드가 아니므로 주석 처리되어 있다.
    # file.write(str(file))
    # 리스트 a를 문자열로 변환하여 파일에 저장한다.
    # 파일에는 [1, 2, 3, 4] 형태의 문자열이 저장된다.
    file.write(str(a))
# 리스트 a를 문자열로 변환한 결과를 출력한다.
print(str(a))

# 저장한 array1.text 파일을 읽기 모드로 연다.
with open('array1.text', 'r') as file :
    # 파일의 내용을 문자열로 읽어온다.
    b = file.read()
    # b의 자료형과 내용을 출력한다.
    # 파일에서 읽은 결과이므로 b의 자료형은 str이다.
    print(type(b), b)
    # 문자열 b를 리스트로 변환한다.
    # 원래의 숫자 리스트로 복원되는 것이 아니라 문자열의 각 글자가 요소가 된다.
    # 예: '[1,2]' → ['[', '1', ',', '2', ']']
    c = list(b)
    # c의 자료형과 내용을 출력한다.
    print(type(c), c)

# 파이썬 객체를 원래 자료형 그대로 저장하고 불러올 수 있는 pickle을 가져온다.
import pickle

# pickle 파일에 저장할 문자열이다.
name = 'eng'
# pickle 파일에 저장할 정수이다.
age = 20
# pickle 파일에 저장할 한글 문자열이다.
address = '한글'
# pickle 파일에 저장할 리스트이다.
arr = [1,2,3,4]
# pickle 파일에 저장할 딕셔너리이다.
score = {
    'k': 66,
    'k2' : 'val'
}

# wb는 바이너리 쓰기 모드이다.
# pickle 데이터는 바이너리 형태이므로 'w'가 아니라 'wb'를 사용한다.
with open('pickle.p', 'wb') as f :
    # name을 첫 번째 객체로 저장한다.
    pickle.dump(name, f)
    # age를 두 번째 객체로 저장한다.
    pickle.dump(age, f)
    # address를 세 번째 객체로 저장한다.
    pickle.dump(address, f)
    # arr을 네 번째 객체로 저장한다.
    pickle.dump(arr, f)
    # score를 다섯 번째 객체로 저장한다.
    pickle.dump(score, f)

# rb는 바이너리 읽기 모드이다.
# pickle 데이터를 읽을 때는 저장할 때와 반대로 'rb'를 사용한다.
with open('pickle.p', 'rb') as f :
    # 첫 번째로 저장했던 name을 불러온다.
    p1 = pickle.load(f)
    # 불러온 name을 출력한다.
    print(p1)
    # 두 번째로 저장했던 age를 불러온다.
    p2 = pickle.load(f)
    # age의 값과 원래 자료형인 int를 출력한다.
    print(p2, type(p2))
    # 세 번째로 저장했던 address를 불러온다.
    p2 = pickle.load(f)
    # address의 값과 원래 자료형인 str을 출력한다.
    print(p2, type(p2))
    # 네 번째로 저장했던 arr을 불러온다.
    p2 = pickle.load(f)
    # arr의 값과 원래 자료형인 list를 출력한다.
    print(p2, type(p2))
    # 다섯 번째로 저장했던 score를 불러온다.
    p2 = pickle.load(f)
    # score의 값과 원래 자료형인 dict를 출력한다.
    print(p2, type(p2))
    # 현재 p2에는 score 딕셔너리가 들어 있으므로 'k' 키의 값 66을 출력한다.
    print(p2['k'])

    # dump한 만큼만 꺼낼 수 있다
    # 현재 5번 저장하고 5번 불러왔으므로 한 번 더 load하면 EOFError가 발생한다.
    # p2 = pickle.load(f)
    # print(p2, type(p2))

# pickle 보다 대용량에 특화된 라이브러리
# 특히 큰 배열이나 머신러닝 모델 등을 저장할 때 자주 사용한다.
# import joblib

# a 이어 쓰기
# 'a' 모드는 기존 파일 내용을 지우지 않고 마지막 위치에 내용을 추가한다.
with open('hello.txt', 'a') as f :
    # hello.txt의 기존 내용 뒤에 '123'을 추가한다.
    f.write('123')
    # 'a'는 쓰기 전용이므로 read()를 사용할 수 없다.
    # f.read()

# +
# 파일 모드에 +를 붙이면 읽기와 쓰기를 함께 사용할 수 있다.
# 쓰기 계열에 붙어있으면 읽기 가능해짐
# 예: w+, a+
# 읽기 계열에 붙어있으면 쓰기 가능해짐
# 예: r+

# 먼저 파일을 가져와서 읽기
with open('word.txt', 'r') as file :
    # 내용물 출력을 위해 변수에 저장
    text = file.read()
# 공백을 기준으로 단어를 나누어 리스트로 저장
words = text.split()
# 리스트에서 단어를 하나씩 꺼내 검사
for word in words :
    # , 과 . 제거
    cleanWord = word.replace(',', '')
    cleanWord = cleanWord.replace('.', '')
    # 검사 일관성을 위해 lower 사용
    lowerWord = cleanWord.lower()
    # 만약 c가 있다면 lower 이전의 원본 단어 출력
    if 'c' in lowerWord:
        print(cleanWord)
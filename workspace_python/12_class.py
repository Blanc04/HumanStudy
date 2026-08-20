# Person이라는 이름의 클래스를 정의한다.
# 클래스는 변수와 함수를 묶어서 객체를 만들기 위한 설계도이다.
class Person : 
    # __init__
    # 클래스가 생성될 때
    # 자동으로 먼저 실행되는 메소드
    def __init__(self):
        # Person 객체가 생성되면 숫자 1을 출력한다.
        print(1)
        # 현재 생성된 객체에 hello라는 변수를 만든다.
        # self는 현재 생성되거나 사용 중인 객체 자신을 의미한다.
        self.hello = '안녕하세요'

    # 생성된 Person 객체가 사용할 수 있는 greeting 메소드이다.
    def greeting(self):
        # print('Hello Class')
        # 현재 객체의 hello 변수에 저장된 값을 출력한다.
        print(self.hello)

    # hello라는 이름의 메소드를 정의한다.
    def hello(self):
        # 현재 객체의 greeting 메소드를 실행한다.
        self.greeting()

# Person 객체를 생성하기 전에 숫자 0을 출력한다.
print(0)
# Person 객체를 생성하고 james 변수에 저장한다.
# 객체가 생성되면서 __init__ 메소드가 자동으로 실행된다.
james = Person()
# Person 객체 생성이 끝난 뒤 숫자 2를 출력한다.
print(2)
# james 객체의 greeting 메소드를 실행한다.
james.greeting()

# james 변수에 저장된 Person 객체의 정보를 출력한다.
# 일반적으로 객체가 저장된 메모리 위치와 클래스 이름이 표시된다.
print(james)
# james 객체의 자료형을 출력한다.
# james는 Person 클래스로 만든 객체이므로 Person이 출력된다.
print(type(james))

# Person2라는 새로운 클래스를 정의한다.
class Person2 : 
    # Person2 객체를 생성할 때 name과 age 값을 전달받는다.
    def __init__(self, name, age):
        # 현재 객체에 hello 변수를 만들고 문자열을 저장한다.
        self.hello = '안녕하세요'
        # 전달받은 name 값을 현재 객체의 name 변수에 저장한다.
        self.name = name
        # 전달받은 age 값을 현재 객체의 age 변수에 저장한다.
        self.age = age

    # 현재 객체의 인사말, 이름, 나이를 출력하는 메소드이다.
    def greeting(self):
        # print('Hello Class')
        # f-string을 사용하여 객체에 저장된 값들을 문자열 안에 넣는다.
        print(f'{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다.')

# 이름은 '이름', 나이는 20인 Person2 객체를 생성한다.
# 생성된 객체는 a 변수에 저장된다.
a = Person2('이름', 20)
# a 객체의 greeting 메소드를 실행한다.
a.greeting()
# a 객체의 hello 변수 값을 출력한다.
print(a.hello)
# a 객체의 name 변수 값을 출력한다.
print(a.name)

# 이름은 '다른이름', 나이는 30인 또 다른 Person2 객체를 생성한다.
# 생성된 객체는 b 변수에 저장된다.
b = Person2('다른이름', 30)
# b 객체의 greeting 메소드를 실행한다.
b.greeting()
# b 객체의 name 변수 값을 출력한다.
print(b.name)

# b 객체에 addr이라는 새로운 인스턴스 변수를 추가한다.
# __init__에 정의하지 않은 변수도 객체에 직접 추가할 수 있다.
b.addr = '천안'
# b 객체의 addr 변수 값을 출력한다.
print(b.addr)

# a 객체에는 addr 변수를 추가하지 않았기 때문에 실행하면 에러가 발생한다.
# print(a.addr)
# b 객체의 __init__ 메소드를 직접 다시 실행한다.
# name은 1, age는 2로 바뀌지만 addr 변수는 그대로 남아 있다.
b.__init__(1,2) # 실행됨

# Person3이라는 새로운 클래스를 정의한다.
class Person3 :
    # Person3 객체를 생성할 때 money 값을 전달받는다.
    def __init__(self, money):
        # 현재 객체에 hello 변수를 만들고 문자열을 저장한다.
        self.hello = '안녕하세요'
        # 변수 이름 앞에 밑줄 두 개를 붙이면 외부에서 직접 접근하기 어려워진다.
        # 전달받은 money 값을 비공개 형태의 변수에 저장한다.
        self.__money = money

    # 현재 객체가 가진 돈에서 price만큼 차감하는 메소드이다.
    def pay(self, price): 
        # 비공개 변수 __money에서 전달받은 price 값을 뺀다.
        self.__money -= price
        # 돈을 차감한 후 남은 금액을 출력한다.
        print('남은 돈 : ', self.__money)

    # 메소드 이름 앞에도 밑줄 두 개를 붙여 외부 접근을 어렵게 만들 수 있다.
    def __study(self):
        # __study 메소드가 실행되면 문자열을 출력한다.
        print('히히 나 혼자 레벨 업')

# money가 10000인 Person3 객체를 생성하여 a 변수에 저장한다.
# 기존에 a에 저장되어 있던 Person2 객체는 새로운 객체로 덮어쓴다.
a = Person3(10000)
# a 객체의 돈에서 2500을 차감한다.
a.pay(2500)
# a 객체의 hello 변수 값을 출력한다.
print(a.hello)
# a 객체에 money라는 새로운 변수를 추가한다.
# money와 클래스 내부의 __money는 서로 다른 별개의 변수이다.
a.money = 99999999 # 이건 별개 변수 추가
# money가 666666666인 새로운 Person3 객체를 생성한다.
# 기존 a 객체 대신 새 객체가 a 변수에 저장된다.
a = Person3(666666666)
# 새로 생성된 a 객체의 돈에서 66666666을 차감한다.
a.pay(66666666)
# __study는 비공개 형태의 메소드이므로 외부에서 이 이름으로 직접 접근하면 에러가 발생한다.
# print(a.__study)

# __붙은 변수나 함수는
# 내부에서는 접근 가능
# 외부로 노출되지 않음
# 캡슐화, 은닉화
# print(a.__money) #__+_money

# h1 = HumanJobs()
# h1.setAddr('천안')
# h1_addr = h1.getAddr()
# print(h1_addr)

class Knotted :

    brand = '노티드-디저트맛집'

    def __init__(self, name, addr) :
        # self.brand = '노티드-디저트맛집'
        self.name = name
        self.addr = addr
    def info(self):
        print(self.name)

k1 = Knotted('천안점', '천안')
k2 = Knotted('아산점', '아산')

print(k1.name, k1.brand)
print(k2.name, k2.brand)

print(k1.name, Knotted.brand)
print(k2.name, Knotted.brand)

class Calc :
    PI = 3.141592

    def __init__(self):
        self.meet = 200

    @staticmethod
    def add(x, y):
        return x + y

    def plus(self, x, y):
        return Calc.add(x, y)

print( Calc.add(1,2) * Calc.PI )

class Person4:
    count = 0

    def __init__(self) :
        Person4.count += 1

    @classmethod
    def print_count(cls) :
        print(f'{cls.count}명 생성 됨')

p1 = Person4()
p2 = Person4()
p3 = Person4()
Person4.print_count()


class Account:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, money):
        self.__balance = money

    def getBalance(self):
        return self.__balance

a1 = Account()
# a1.balance = 99999

'''
문제1
멜론 차트 관리 시스템
모든 곡을 리스트로 관리
한 곡에 해당하는 클래스부터 만들자
- 제목, 가수명, 앨범명, 가사

두 곡 이상 정보를 저장
각 곡의 '제목-가수명'을 출력

문제2
휴먼잡스 계정 관리 시스템
내 계정에는 id, pw, 주소가 있다
모두 접근 제한된 private 변수입니다.

메소드를 이용해서 주소를 변경하거나
주소를 return하는 메소드를 만들기

문제3
디저트 카페 노티드 창업을 위한 클래스
 - 상호, 자본금이 필수 요소

노티드를 두군데에 창업할 것이다.
하나를 창업할 때 필수 요소를 꼭 넣어야 생성되도록 만드세요

'''

class Song :
    # - 제목, 가수명, 앨범명, 가사
    def __init__(self, title, singer, album, lyric):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric

s1 = Song('LOVE ATTACK', 'RESCENE (리센느)', 'SCENEDROME', '라부 어택')
s2 = Song('갑자기', '아이오아이 (I.O.I)', 'I.O.I 3rd MINI ALBUM', '써든 어택')

melon = [s1, s2]
for song in melon :
    print(f'{song.title}-{song.singer}')

class HumanJobs :
    def __init__(self):
        self.__id = None
        self.__pw = ''
        self.__addr = ''

    def setAddr(self, addr):
        if addr :
            self.__addr = addr
        else :
            print('주소를 다시 입력하세요')
    def getAddr(self):
        return self.__addr

h1 = HumanJobs()
# print( h1.__id )
h1.setAddr('천안')
h1_addr = h1.getAddr()
print( h1_addr )

class Knotted2 :
    def __init__(self, 상호, 자본금) :
        self.상호 = 상호
        self.자본금 = 자본금

# k1 = Knotted2()
# k1 = Knotted2('천안점')
k1 = Knotted2('천안점', 10000)


class Melon :
    def __init__(self):
        self.songList = []

    def appendSong(self, song):
        self.songList.append(song)
m = Melon()
m.appendSong(s1)
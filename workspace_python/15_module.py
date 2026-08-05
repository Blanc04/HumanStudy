
import fn_15_1

a = fn_15_1.add(1,2)
print(a)

from fn_15_1 import sub
b = sub(3,2)
print(b)

import random
print(random.random())

from random import random as rand
# print(random())
print(rand())

from fn_15_1 import Hero
h = Hero()
h.attack()

import urllib.request
response = urllib.request.urlopen('http://google.co.kr')
print(response.read().decode('utf-8'))







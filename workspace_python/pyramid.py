m = '+'
s = '-'
string = ''
# q1
for i in range(1, 6):
    print(m, end='')
print()
# q2
for i in range(1, 2):
    for j in range(1, 6):
        print(m, end='')
        print(s, end='')
print()
# q3
for i in range(1, 4):
    for j in range(1, 6):
        print(m, end='')
    print()
print()
# q4
for i in range(1, 6):
    for j in range(1, 6):
        print(i, end='')
    print()
print()
# q5
for j in range(1, 6):
    string = ''
    for i in range(1, j+1):
        string += str(j)
    print(string)
print()
# q6
for j in range(1, 6):
    string = ''
    for i in range(1, j+1):
        string += m
    print(string)
print()
# q7
for j in range(1, 6):
    string = ''
    for i in range(1, 7-j):
        string += str(j)
    print(string)
print()
# q8
for j in range(1, 6):
    string = ''
    for i in range(1, j+1):
        string += m
    for i in range(1, 6-j):
        string += s
    print(string)
print()
# q9
for j in range(1, 6):
    string = ''
    for i in range(1, 6-j):
        string += s
    for i in range(1, j+1):
        string += m
    print(string)
print()
# q10
for j in range(1, 6):
    string = ''
    for i in range(1, 6-j):
        string += s
    for i in range(1, j+1):
        string += m
    for i in range(1, j):
        string += m
    print(string)
print()
# q11
for j in range(1, 6):
    string = ''
    for i in range(1, 6-j):
        string += s
    for i in range(1, j+1):
        string += m
    for i in range(1, j):
        string += m
    for i in range(1, 6-j):
        string += s
    print(string)
print()
# q12
line = int(input('줄 입력 : '))
for j in range(line):
    string = ''
    for i in range(1, line-j):
        string += s
    for i in range(1, j+1):
        string += m
    for i in range(1, j):
        string += m
    for i in range(1, line-j):
        string += s
    print(string)
print()
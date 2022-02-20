# import

# Hello World
from fractions import Fraction

print("Hello world")

# variable definition:
a = 2001
print(a)

x = "Kim Chi"
print(x)

b, a, i = 0, "Hello", 1.9
f = Fraction(9, 8)
print(type(i))
print(type(a))
print(type(b))

# Kiểu dữ liệu

# ext Type: 	str
s = 'chuoi thong thuong'
sk = "chuoi nhay kep"
skk = '''chuoi
nhieu
dong'''
'''----------------Like comment--------------------'''

print('\a')

# Numeric Types: 	int (vô hạn) , float(15 chữ số thập phân), complex(số phức)
f = Fraction(9, 8)  # phân số
c = complex(2, 5)  # == 2+5i
# Operator (+ - * / // %)

# Sequence Types: 	list, tuple, range
listA = [1, "x", Fraction(8, 4), True]  # list
print(listA)
listB = [i * 3 for i in range(10)]
print(listB)
listC = list("KimChi")
print(listC)
print(listC[4])
print(listC[-1])  # lấy phần tử cuối
print(listC[1:4])  # lấy phần tử từ 1 ->3
print(listC[:4])  # lấy từ 0 - > 4
print(listC[4:])  # lấy từ 4 trở đi
print(listC[::-1])  # đảo ngược
print(listC.count('i'))  # đếm

# tuple
tupleA = (1, 2, 3)
print(tupleA)
tupleB = tuple("KimChi")
print(tupleB)
tupleC = tuple(i for i in range(10) if i % 2 == 0)
print(tupleC)

# Mapping Type: 	dict
dictA = {"key": "value", 'key2': 3}
print(dictA)
dictB = dict({3: 9})
print(dictB)
dictC = dict(name="KimmChi", age=90)  # = {'name': 'KimmChi', 'age': 90}
print(dictC)
print(dictC['name'])

# Set Types: 	set, frozenset
setA = {1, 2, 3, 4}
print(setA)
setB = {4, 4, 2, 3, 5}
print(setB)  # set không chứa giá trị trùng lặp
setC = set("KimChi")
print(setC)
print(setA & setB)
print(setA - setB)
print(setA ^ setB)
print(setA | setB)

# Boolean Type: 	bool
print(5 > 9)
# Binary Types: 	bytes, bytearray, memoryview
# File
fileA = open('hello.txt', 'r+')
content = fileA.readlines()
fileA.writelines('\nWrite \n line')
print(content)
fileA.close()

# If - else
if 4 < 7:
    print("Hello")
    if 6 > 7:
        print("Hello2")
    elif 6 == 7:
        print("Hello3")
    else:
        print("Hello4")

# While loop
x = 0
while x <= 5:
    print(x)
    x += 1

listX = list(i for i in range(10))
index = 0
while index < len(listX):
    print(listX[index])
    index += 2

# For loop
for i in range(10):
    print("Hello ", i)

inter_ = (x for x in range(10) if x % 2 == 0)
for i in inter_:
    print("test", i)

s = "KimChi"
for i in s:
    print(i)

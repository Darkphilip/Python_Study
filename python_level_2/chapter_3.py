
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(functions), 클래스(Class)
# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))
print()
print()

n=10
# 사용
print(n+100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self,name,price):
        self._name = name
        self._price = price
    def __str__(self):
        return 'Fruit Class Info : {}, {}'.format(self._name,self._price)
    def __add__(self,x):
        print('Called >> __add__ Method.')
        return self._price + x._price
    def __sub__(self,x):
        print('Called >> __sub__ Method.')
        return self._price - x._price
    def __le__(self,x):
        print('Called >> __sub__ Method.')
        return self._price <= x._price
    def __ge__(self,x):
        print('Called >> __sub__ Method.')
        return self._price >= x._price

# 인스턴스 생성
s1 = Fruit('Orange',7500)
s2 = Fruit('Banana', 3000)

# 매직메소드 출력
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1)
print(s2)

# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(functions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드
# 클래스 예제2
class Vector:
    def __init__(self,*args):
        '''Create a vector, example : v = Vector(5,10)'''
        if len(args) == 0:
            self._x,self._y = 0, 0
        else:
            self._x, self._y = args
    def __repr__(self):
        '''Returns the vector informations'''
        return 'Vector(%r,%r)' % (self._x,self._y)
    def __add__(self,other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)
    def __mul__(self,y):
        return Vector(self._x * y, self._y * y)
    def __bool__(self):
        return bool(max(self._x, self._y))

# 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector(0,0)
# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 10)
print(v2 * 3)
print(bool(v1), bool(v2))
print(bool(v3))
print()
print()
# 참고 : 파이썬 바이트 코드 실행
import dis
dis.dis(v2.__add__)

# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(functions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> Python의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3)
# print(pt4)
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename = True) # Default = False

# Dict to Unpacking
temp_dict = {'x' : 75, 'y' : 55}
print(Point1, Point2, Point3, Point4)
# 객체 생성
p1 = Point1(x = 10, y = 35)
p2 = Point2(x= 20, y = 40)
p3 = Point3(x= 45, y = 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print()
print(p1)
print(p2)
print(p3)
# rename
print(p4)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p3
print(x + y)
# 네임드 튜플 메소드
temp = [52, 38]
# _make() : 새로운 객체 생성
p6 = Point1._make(temp)
print(p6)

# fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)
# _asdict : OrderedDict 반환
print(p1._asdict(), p6._asdict())

# 실사용 실습
# 반 20명, 4개의 반(A,B,C,D)
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
students2 = [
    Classes(rank, number)
    for rank in 'A B C D'.split()
        for number in [str(n)
            for n in range(1,21)]]

print(len(students2))
print(students2)

# 출력
for s in students2:
    print(s)
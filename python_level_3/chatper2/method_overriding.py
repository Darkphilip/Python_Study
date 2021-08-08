"""
Chapter 2
Python Advanced(2) - Method Overriding
Keyword  - Overriding, OOP, 다형성

"""
"""

메소드 오버라이딩 효과
1. 서브클래스에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용 가능
3. 부모클래스의 메소드 추상화 후 사용 가능(구조적 접근)
4. 확장 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가, 오류 가능성 감소, 메소드 이름 절약, 유지보수성 증가 등

"""

# EX1
# 기본 Overriding 예제
class ParentEX1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEX1(ParentEX1):
    pass

p1 = ParentEX1()
c1 = ChildEX1()

# 부모 클래스 메소드 호출
print('EX1 >', c1.get_value())

# c1 모든 속성 출력
print('EX1 >', dir(c1))

# 부모 & 자식 모든 속성 출력
print('EX1 >', dir(ParentEX1))
print('EX1 >', dir(ChildEX1))

print()

# 부모 & 자식 인스턴스 속성 출력
print('EX1 >', ParentEX1.__dict__)
print('EX1 >', ChildEX1.__dict__)
print()

# EX2
# 기본 Overriding 메소드 재정의
class ParentEX2():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEX2(ParentEX2):
    def get_value(self):
        return self.value * 10

c2 = ChildEX2()

# 자식 메소드 재정의 후 호출
print('EX2 >', c2.get_value())

print()

# EX3
# Overriding 다형성 예제

import datetime

class Logger(object):
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self,msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now(), msg = msg)
        # super().log(message)
        super(TimestampLogger, self).log(message)

class DateLogger(Logger):
    def log(self,msg):
        message = "{ts} {msg}".format(ts = datetime.datetime.now().strftime('%Y-%m-%d'), msg = msg)
        # super().log(message)
        super(DateLogger, self).log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()

# 메소드 재정의 실습
print('EX3 >', l.log('Called Logger.'))
print('EX3 >', t.log('Called TimestampLogger.'))
print('EX3 >', d.log('Called DateLogger.'))

l.log('Called Logger.')
t.log('Called Logger.')
d.log('Called Logger.')

"""
Chapter2
Python Advanced(2) - Method Overloading
Keyword - overloading, oop, multipledispatch

"""
"""

메소드 오버로딩 효과
1. 동일 메소드 재정의
2. 네이밍 기능 예측
3. 코드 절약, 가독성 향상
4. 메소드 파라미터 기반 호출 방식

"""

# EX1
# 동일 이름 메소드 사용 예제
# 동적 타입 검사 -> 런타임에 실행(타입 에러가 실행시에 발견)

class SampleA():
    def add(self,x,y):
        return x + y
    
    def add(self,x,y,z):
        return x + y + z

    # 팩킹으로 해결 가능
    # def add(self, **args):
    #     return sum(args)

a = SampleA()

# print('EX1 >', a.add(2,3)) # 예외 발생

# 모든 속성 개체 확인
print('EX1 >', dir(a))

# EX2
# 동일 이름 메소드 사용 예제
# 자료형에 따른 분기 처리
class SampleB():

    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)

        if datatype == 'str':
            return ' '.join([x for x in args])

b = SampleB()

# 숫자 연산
print('EX2 >', b.add('int', 5, 6))
# 문자열 연산
print('EX2 >', b.add('str', 'Hi', 'Python'))

# EX3
# multipledispatch 패키지를 통한 메소드 오버로딩
from multipledispatch import dispatch

class SampleC():

    @dispatch(int, int)
    def product(x, y):
        return x * y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z

c = SampleC()

print('EX3 >', c.product(5,6))
print('EX3 >', c.product(5,6,7))
print('EX3 >', c.product(5.1,6.2,7.3))
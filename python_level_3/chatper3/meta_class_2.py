"""
Chapter 3
Python Advanced(3) - Meta Class(2)
Keyword - Type(name, base, dct), Dynamic metaclass

"""
"""

메타클래스
1. 메타클래스 동적 생성 방법 중요
2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점

"""

# EX1
# type 동적 클래스 생성 예제

# Name(이름), Bases(상속), Dict(속성, 메소드)
s1 = type('Sample1', (), {})

print('EX1 >', s1)
print('EX1 >', type(s1))
print('EX1 >', s1.__base__)
print('EX1 >', s1.__dict__)

print()

# 동적 생성 + 상속
class Parent1():
    pass

s2 = type(
    'Sample2',
    (Parent1,),
    dict(attr1 = 100, attr2 = 'Hi')
)

print('EX1 >', s2)
print('EX1 >', type(s2))
print('EX1 >', s2.__base__)
print('EX1 >', s2.__dict__)
print('EX1 >', s2.attr1, s2.attr2)

print()

# EX2
# type 동적 클래스 생성 + 메소드
class SampleEX():
    attr1 = 30
    attr2 = 100

    def add(self,m,n):
        return m + n
    
    def mul(self,m,n):
        return m * n

ex = SampleEX()

print('EX2 >', ex.attr1)
print('EX2 >', ex.attr2)
print('EX2 >', ex.add(100,200))
print('EX2 >', ex.mul(100,9))
print()

# SampleEX 클래스를 type으로 동적 생성

s3 = type(
    'Sample3',
    (object,), # 생략 가능
    dict(attr1 = 30, attr2 = 100, add = lambda x, y: x + y, mul = lambda x, y: x * y)
)

print('EX2 >', s3.attr1)
print('EX2 >', s3.attr2)
print('EX2 >', s3.add(100,200))
print('EX2 >', s3.mul(100,9))
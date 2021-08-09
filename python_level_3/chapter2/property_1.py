"""
Chapter 2 Python Advanced(2) - Property(1) - Underscore
Keyword - access modifier(접근지정자), underscore

"""
"""
다양한 언더스코어 활용
파이썬 접근지정자 설명

"""

# EX1
# Use underscore
# 1. 인터프리터 2. 값 무시 3. 네이밍...(국제화, 자릿수 등)

# Unpacking
x, _, y = (1,2,3)
a, *_, b = (1,2,3,4,5)

print('EX1 >', x, y, a, b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass

# EX2 
# 접근지정자
# name : public
# _name : protected
# __name : private
# 파이썬 -> Public 강제적 할당 X, 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# 타 클래스(클래스변수, 인스턴스 변수 값 쓰기 장려 안함) -> Naming Magling
# 타 클래스 __ 접근하지 않는 것이 원칙.

# No use Property

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0

a = SampleA()
a.x = 1

print('EX2 > x : {}'.format(a.x) )
# print('EX2 > y : {}'.format(a.__y))
print('EX2 > z : {}'.format(a._z))
print(dir(a)) # _SampleA__y

# a._SampleA__y = 2 # 수정가능
# print('EX2 > y : {}'.format(a._SampleA__y))

# EX3
# 메소드 활용 Getter, Setter 작성

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

b = SampleB()
b.x = 1
b.set_y(2)

print('EX3 > x : {}'.format(b.x))
print('EX3 > y : {}'.format(b.get_y()))

# 변수 접근 후 수정 부분에서 일관성, 가독성 하락
print('EX3 >', dir(b))
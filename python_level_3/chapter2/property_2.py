"""
Chapter2 Python Advanced(2) -Property(2) - Getter, Setter
Keyword - @Property

"""
"""
프로퍼터(Property) 사용 장점
1. 파이써닉한 코드
2. 변수 제약 설정
3. Getter, Setter 효과 동등(코드 일관성)  
    - 캡슐화-유효성 검사 기능 추가 용이
    - 대체 표현(속성 노출, 내부 표현 숨기기 가능)
    - 속성의 수명 및 메모리 관리 용이
    - 디버깅 용이
    - Getter, Setter 작동에 대해 설계된 여러 라이브러리(오픈소스) 상호 운용성 증가
    
"""

# EX1
# Property 활용 Getter, Setter 작성

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0 # private

    @property
    def y(self):
        print('Called Get Method.')
        return self.__y
    
    @y.setter
    def y(self, value):
        print('Called Set Method.')
        self.__y = value

    @y.deleter
    def y(self):
        print('Called Del Method.')
        del self.__y

a = SampleA()

a.x = 1
a.y = 2

print('EX1 > x : {}'.format(a.x))
print('EX1 > y : {}'.format(a.y))

# a._SampleA_y = 100 # 변수 수정 가능

# 변수 접근 후 수정 부분에서 일관성, 가독성 하락
print('EX1 >', dir(a))

# deleter 확인
# del a.y
# print('EX1 >', dir(a))

# EX 2
# Property 활용 제약 조건 추가

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 # private

    @property
    def y(self):
        # print('Called Get Method.')
        return self.__y
    
    @y.setter
    def y(self, value):
        # print('Called Set Method.')
        if value < 0:
            raise ValueError('0보다 큰 값을 입력하세요.')
        self.__y = value

    @y.deleter
    def y(self):
        # print('Called Del Method.')
        del self.__y

b = SampleB()

b.x = 1
b.y = 10

# b.y = -5 예외 발생

print('EX2 > x : {}'.format(b.x))
print('EX2 > y : {}'.format(b.y))
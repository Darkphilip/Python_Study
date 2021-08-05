# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량1

car_company = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'Hp' : '400'},
    {'price' : '8000'}
]
car_company2 = 'BMW'
car_detail_2 = [
    {'color' : 'Black'},
    {'Hp' : '270'},
    {'price' : '5000'}
]
car_company3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'Hp' : '300'},
    {'price' : '6000'}
]

# 리스트 구조
# 관리하기 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color' : 'White', 'Hp' : '400', 'price' : '8000'},
    {'color' : 'Black', 'Hp' : '270', 'price' : '5000'},
    {'color' : 'Silver', 'Hp' : '300', 'price' : '6000'}
]
del car_detail_list[1]
del car_company_list[1]
print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {'car_company' : 'Ferrari', 'car_detail' : {'color' : 'White', 'Hp' : '400', 'price' : '8000'}},
    {'car_company': 'Bmw', 'car_detail': {'color' : 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color' : 'Silver', 'horsepower': 300, 'price': 6000}}
]
del car_dicts[1]
print(car_dicts)
print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
print()
print(car_list)
print()
print()

# 반복 (__str__)
for x in car_list:
    print(repr(x))
    # print(x)

# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Car():
    """
    Car class
    Author : Kim
    Date: 2021.04.03
    """
    # 클래스 변수
    car_count = 0
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail info : {} {}'.format(self._company, self._details.get('price')))
    def __del__(self):
        Car.car_count -= 1

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# id 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))
print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# Error
# Car.detail_info()
Car.detail_info(car1)
Car.detail_info(car2)

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__))
print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장 X)
print(car1._company, car2._company)
print(car2._company, car3._company)

print()
print()

# 클래스 변수
# 접근
print(car1.car_count)
print(car2.car_count)
print(Car.car_count)
print()
print()

# 공유 확인
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
del car2
print(car1.car_count)
print(car3.car_count)

# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드

class Car():
    """
    Car class
    Author : Kim
    Date: 2021.04.03
    Description : Class, Static, Instance Method
    """
    # 클래스 변수
    price_per_raise = 1.0
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    # Instance Method
    # self : 객체의 고유한 속성 값 사용
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail info : {} {}'.format(self._company, self._details.get('price')))
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company,self._details.get('price'))
    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company,self._details.get('price')*Car.price_per_raise)
    # Class Method
    @classmethod
    def raise_price(cls,per):
        if per <=1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'Succeed! Price Incresed.'
    # Static Method
    @staticmethod
    def is_Bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok! This car is {}'.format(inst._company)
        return 'Sorry. This car is not BMW.'

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
# 기본 정보
print(car1)
print(car2)
print()
# 전체 정보
car1.detail_info()
car2.detail_info()
print()
# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(클래스 메소드 사용)
Car.price_per_raise = 1.2

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print()
# 가격 정보(인상 후 : 클래스 메소드)
print(car1.get_price_culc())
print(car2.get_price_culc())
# 인스턴스로 호출(스테틱)
print(car1.is_Bmw(car1))
print(car2.is_Bmw(car2))
# 클래스로 호출(스테틱)
print(Car.is_Bmw(car1))
print(Car.is_Bmw(car2))
print(Car.__doc__)
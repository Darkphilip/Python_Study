# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능

# 함수 객체
def factorial(n):
    '''Factorial Function -> n int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(6))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)
print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(10))
print(map(var_func, range(1,11)))
print(list(map(var_func, range(1,6))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higer-order function)
# map, filter, reduce 등
print(list(map(var_func, filter(lambda x : x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])

print()
print()

# reduce()
from functools import reduce
from operator import add

print(reduce(add, range(1,11)))
print(sum(range(1,11)))

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t : x + t, range(1,11)))
print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한 지 확인
# 호출 가능 확인
print(callable(str),callable(list), callable(var_func), callable(3.14))

from inspect import signature
sg = signature(var_func)
print(sg)
print(sg.parameters)
print()
print()

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial
print(mul(10,10))
# 인수 고정
five = partial(mul,5)
# 고정 추가
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))

# 파이썬 심화
# 일급 함수(일급 객체)
# 클로저 기초
# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(10)

# Ex2
b = 20
def func_v2(a):
    print(a)
    print(b)
func_v2(10)

# Ex3
c = 30
def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40
print('>>', c)
func_v3(10)
print('>>>', c)

# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처라힉 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점
# 저장 후 로드

a = 100
print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))

print()
print()

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []
    def __call__(self, v):
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls=Averager()
print(dir(averager_cls))

# 누적
print(averager_cls(15))
print(averager_cls(30))
print(averager_cls(90))

print()
print()

# 파이썬 심화
# 클로저 심화
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(액세스) 가능

# Closure 사용
def closure_ex1():
    # free variable
    series=[]
    # 클로저 영역
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

averager_cls = closure_ex1()

print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))

print()
print()

# function inspection
print(dir(averager_cls))
print()
print(dir(averager_cls.__code__))
print()
print(averager_cls.__code__.co_freevars)
print()
print(dir(averager_cls.__closure__[0]))
print()
print(averager_cls.__closure__[0].cell_contents)
print()
print()

# 잘못된 클로저 사용
def closure_ex2():
    # free variable
    cnt = 0 # local cnt
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager
averager_cls2 = closure_ex2()
# print(averager_cls2(15))

# Nonlocal -> Free variable
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total/cnt
    return averager

averager_cls3 = closure_ex3()
print(averager_cls3(15))
print(averager_cls3(30))
print(averager_cls3(45))
print()
print()

# 클로저 기초
# 데코레이터(Decorator)

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 함수
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성?
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습
import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 함수 종료 시간 계산
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked
@perf_clock
def time_func(seconds):
    time.sleep(seconds)
@perf_clock
def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)
print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)
print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print()
print('-' * 40, 'Called None Decorator -> sum_func')
none_deco2(100, 200, 300, 400, 500)
print()
print()

# 데코레이터 사용
print('-' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print()
sum_func(100, 200, 300, 400, 500)
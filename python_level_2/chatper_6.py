# 병행성(Concurrency)
# 이터레이터, 제너레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text file, list, dict, set, tuple, unpacking, *args : iterable

# 반복 가능한 이유 -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for 반복
for c in t :
    print(c)

print()

# while 반복
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

from collections import abc
# 반복형 확인
# print(dir(t))
print(hasattr(t,'__iter__'))
print(isinstance(t,abc.Iterable))
print()
print()

# next 사용
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))
print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self,text):
        self._text = text.split(' ')

    def __iter__(self):
        print('Called __iter__')
        for word in self._text:
            yield word # 제너레이터
        return
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)
print(wt)
print(wg)
print()
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1

def generator_ex1():
     print('Start')
     yield 'A point.'
     print('Countinue')
     yield 'B point'
     print('End')

temp = iter(generator_ex1())
# print(next(temp))
# print(next(temp))
# print(next(temp))
for v in generator_ex1():
    print(v)
print()

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())
print(temp2)
print(temp3)
print()
for i in temp2:
    print(i)
print()
print()
for i in temp3:
    print(i)
print()
print()

# Generator Ex3(중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby
import itertools
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한
print()

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))
for v in gen2:
    print(v)
print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])
for v in gen3:
    print(v)
print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
    print(v)
print()

# 연결 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))
print()
# 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

#그룹화
gen9 = itertools.groupby('AAABBCCCDDEEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))
print()

# 코루틴(Coroutine)

# 코루틴 : 단일 쓰레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS 관리, CPU코어에서 실시간, 시분할 비동기 작업
# yield, send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드 -> 멀티 쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# def -> async, yield -> await

# 코루틴 Ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))
# 제너레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# cr1.send(100)

# 잘못된 사용

cr2 = coroutine1()

# cr2.send(100) # 예외 발생

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태
def coroutine2(x):
    print('>>> coroutine started. : {}'.format(x))
    y = yield x
    print('>>> coroutine received. : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received. : {}'.format(z))

cr3 = coroutine2(10)
from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

print(cr3.send(15))

print()
print()

# 코루틴 Ex3
# StopIteration 자동 처리(3.5 -> await)
# 중첩 코루틴 처리
def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y
t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()
print(list(t2))

def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))

# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2

# GIL(Global Interpreter Lock) : 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 액세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행, 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)
#       특정 시점에서 하나의 쓰레드만 실행됨.
#       CPU 작업이 많은 멀티쓰레딩에서는 파이썬이 효율적이지 않을 수 있다.
# GIL : 멀티프로세싱 사용, CPython

import os
import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 10000000]

# 동시성 합계 계산 메인함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))
def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)
    # 종료 시간
    end_tm = time.time() - start_tm
    # 츌력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))

# 실행
if __name__ == '__main__':
    main()
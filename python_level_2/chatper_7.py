# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# non-blocking 비동기 처리
# Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 가지고 있다. 타 함수는 대기
# Nonblocking I/O : 호출된 함수가(서브루틴) return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# 쓰레드 단점 : 디버깅, 자원 접근 시 레이스컨디션(경쟁상태), 데드락(Dead Lock) -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 X -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현되어 있어야 하거나, 직접 비동기로 구현해야 한다.

# Asyncio 웹 스크래핑 실습
# aiohttp 권장

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()

urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://wemakeprice.com/']

async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)

    # 결과 반환
    return res.read()[0:5]



async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    rst = await asyncio.gather(*futures)
    print()
    print('Result :', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total running time : ', duration)

    # Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# non-blocking 비동기 처리
# Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 가지고 있다. 타 함수는 대기
# Nonblocking I/O : 호출된 함수가(서브루틴) return 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속
#
# 쓰레드 단점 : 디버깅, 자원 접근 시 레이스컨디션(경쟁상태), 데드락(Dead Lock) -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 X -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현되어 있어야 하거나, 직접 비동기로 구현해야 한다.

# Asyncio 웹 스크래핑 실습
# aiohttp 권장

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 실행 시작 시간
start = timeit.default_timer()

urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://wemakeprice.com/']

async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)

    soup = BeautifulSoup(res.read(), 'html.parser')
    # 전체 페이지 소스 확인
    # print(soup.prettify())
    # 이 부분에서 BeautifulSoup Selector(선택자)를 활용해서 다양한 정보 가져오기 가능
    result_data = soup.title

    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)

    # 결과 반환
    return result_data



async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    rst = await asyncio.gather(*futures)
    print()
    print('Result :', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total running time : ', duration)
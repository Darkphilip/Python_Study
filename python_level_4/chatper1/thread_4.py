"""
Chapter 1
Multithreading - Thread(4).Lock, DeadLock
Keyword - Lock, DeadLock, Race Condition, Thread synchronization

"""
"""

용어 설명
(1). 세마포어 & 뮤텍스: 여러 프로세스나 쓰레드가 공유 자원에 접근하는 것을 제어하기 위한 방법
    - 병행 처리를 위한 프로세스 동기화 기법

(2). 세미포어 동작 원리
    - semWait 연산: 세마포어 값을 감소시킴. 값이 음수가 되면 프로세스는 블록
    - semSignal 연산: 세마포어 값을 증가시킴. 값이 양수가 아니면(0이거나 음수) 블록된 프로세스를 깨운다

(3). 뮤텍스(Mutex)
    - 임계영역에 들어갈 때 락(Lock)을 걸어 다른 프로세스(혹은 스레드)가 접근하지 못하도록 하고
    임계 영역에서 나와 해당 락을 해제한다.

(3). Lock: 상호 배제를 위한 잠금(Lock)처리 -> 데이터 경쟁

(4). 데드락(DeadLock): 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)

(5). Thread synchronization(스레드 동기화)를 통해서 안정적으로 동작하게 처리한다(동기화 메소드, 동기화 블럭)

(6). Semaphore와 Mutex 차이점
    - 세마포어는 공유 자원에 세마포어의 변수만큼의 프로세스(or 쓰레드)가 접근할 수 있다.
    - 반면에 뮤텍스는 오직 1개만의 프로세스(or 쓰레드)만 접근할 수 있다.

    - 현재 수행중인 프로세스가 아닌 다른 프로세스가 세마포어를 해제할 수 있다. 
    - 하지만 뮤텍스는 락을 획득한 프로세스가 반드시 그 락을 해제해야 한다.


"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore():
    # 공유 변수(value)
    def __init__(self):
        self.value = 0

    # 변수 업데이트 함수
    def update(self, n):
        logging.info('Thread %s: Starting Update.', n)

        # 뮤텍스 & Lock 등 동기화(Thread synchronization 필요)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info('Thread %s: Finishing Update.', n)



if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    # 클래스 인스턴스화
    store = FakeDataStore()

    logging.info('Testing update. Starting value is %d', store.value)

    # with context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info('Testing update. Ending value is %d', store.value)
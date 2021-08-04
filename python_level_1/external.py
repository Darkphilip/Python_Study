# 파이썬 외장 함수
# 실제 프로그램 개발 중 자주 사용
# 종류: sys,pickle, os, shutil, glob, temfile, time, random 등

# sys : 실행 관련 제어
import sys
print(sys.argv)
# sys.exit()
print(sys.path)

#  pickle : 객체 파일 쓰기
import pickle
# 쓰기
f = open("test.obj",'wb')
obj = {1:'python', 2 : 'study', 3 : 'Basic'}
pickle.dump(obj, f)
f.close()
# 읽기
f = open("test.obj",'rb')
data = pickle.load(f)
print(data)
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdirm(디렉토리 생성), rmdir(비어있으면 삭제), rename
import os

# 시스템의 환경 변수
print(os.environ)
print(os.environ['USERNAME'])
# 현재 경로
print(os.getcwd())

# time : 시간 관련 처리
import time
print(time.time())
print(time.localtime(time.time()))
print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M%S',time.localtime(time.time())))
# 시간 간격 발생
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴
import random

print(random.random())

print(random.randint(1, 45))
print(random.randrange(1, 45))

# 섞기
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# webbrowser : 본인 OS 의 웹 브라우저 실행
import webbrowser
webbrowser.open("http://google.com")
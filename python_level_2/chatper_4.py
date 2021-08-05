# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview]
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '+_)(*$!%#@^~'
code_list1 = []
for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # map(함수, 리스트)

print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I',(ord(s) for s in chars))
print(type(tuple_g))
print(next(tuple_g))
print(array_g)
print(array_g.tolist())
print()
print()

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B','C','D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A', 'B','C','D'] for n in range(1,21)):
    print(s)

# 리스트 주의
marks1 = [['~'] * 3 for n in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])

# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview]
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급
# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100,9))
print(divmod(*(100,9)))
print(*(divmod(100,9)))
print()

x, y, *rest = range(5)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(rest)

print()
print()
# Mutable(가변) vs Immutable(불변)
i = (15, 20, 25)
m = [15, 20, 25]
print(i, id(i))
print(m, id(m))
i = i * 2
m = m * 2
print(i, id(i))
print(m, id(m))

i *= 2
m *= 2
print(i, id(i))
print(m, id(m))
print()
print()

# sort vs sorted
# reverse, key = len, key = str.Lower, key = func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya','lemon', 'strawberry','coconut']
print('sorted - ',sorted(f_list))
print('sorted(reverse) - ',sorted(f_list,reverse = True))
print('sorted(len) - ',sorted(f_list,key = len))
print('sorted[-1] - ',sorted(f_list, key = lambda x : x[-1]))
print('sorted[-1](reverse) - ',sorted(f_list, key = lambda x : x[-1], reverse = True))
print()
print('sorted - ',f_list)
print()

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort(reverse) - ', f_list.sort(reverse = True), f_list)
print('sort(len) - ', f_list.sort(key=len), f_list)
print('sort([-1]) - ', f_list.sort(key=lambda x : x[-1]), f_list)
print('sort([-1]reverse) - ', f_list.sort(key=lambda x : x[-1],reverse = True), f_list)

# List vs Array 적합한 사용법 설명
# List : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)

# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Key에 Value를 저장하는 구조 __dict__
# Dict(해시테이블의 예, 키 값의 연산결과에 따라 직접 접근이 가능한 구조)
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])

print(hash(t1))
# print(hash(t2)) list 예외
print()
print()

# Dict Setdefault 예제
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5')
)
new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k,v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# Use Setdefault

for k,v in source:
    new_dict2.setdefault(k,[]).append(v)

print(new_dict2)

# 주의
new_dict3 = {k:v for k ,v in source}
print(new_dict3)

print()

# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict
from types import MappingProxyType

d = {'key1' : 'value1'}

# Read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key1'] = 'value2'
# 수정 가능
d['key2'] = 'value2'
print(d)
print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # not []
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')
# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행

from dis import dis

print('-------')
print(dis('{10}'))

print('-------')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

print('------')
print({name(chr(i),'') for i in range(0,256)})
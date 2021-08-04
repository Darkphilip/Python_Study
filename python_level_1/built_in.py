# 절대값
# abs()
print(abs(-3))

# all, any : iterable 요소 검사(참,거짓)
print(all([1, 2, 3]))
print(any([1, 2, 0]))

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))

for i, name in enumerate(['abc', ['bcd', 'efg']]):
    print(i, name)


# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# max, min : 최대값, 최솟값

print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('python study'))


# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)
print(list(map(conv_abs, [1, -3, 4, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))
print(pow(2, 10))
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))
print(round(6.5781, 2))
print(round(5.6))

# sorted : 정렬

print(sorted([6, 7, 4, 3, 1, 2]))
a = sorted([6, 7, 4, 3, 1, 2])
print(a)
print(sorted(['p','y','t','h','o','n']))

# sum : 합

print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

# type : 자료형 확인
print(type(3))
print(type({}))
print(type([]))
print(type(()))

# zip : 반복가능한 객체(iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50,777])))
print(type(list(zip([10,20,30],[40,50,777]))[0]))
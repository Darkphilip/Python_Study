# 파이썬 리스트
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서, 중복, 수정, 삭제)

# 선언
a = []
b = list()
c = [70,75,80,85]
d = [1000, 10000,'Ace', 'Base', 'Captine']
e = [1000, 10000,['Ace', 'Base', 'Captine']]
f = [21.3, 'foobar', 3, 4, 'bark', False, 3,14159]

# 인덱싱
print('d-',type(d),d)
print('d-',d[1])
print('d-',d[0],d[1],d[2])
print('d-',d[-1])
print('e-',e[-1][1])
print('d-',list(e[-1][1]))

# 슬라이싱
print('d-',d[0:3])
print('d-',d[2:])
print('e-',e[2][1:3])

# 리스트 연산
print('c + d', c+d)
print('c * 3', c*3)
print("Test + c[0]-",'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
# 같은 id 값
temp = c
print(c==temp)

print()
c[0] = 4
print('c-',c)
c[1:2] = ['a','b','c']
print('c-',c)
c[1] = ['a','b','c']
print('c-',c)
c[1:3] = []
print('c-',c)
del c[3]
print('c-',c)

# 리스트 함수
a = [5,2,3,1,4]
print('a-',a)
a.append(6)
print('a-',a)
a.sort()
print('a-',a)
a.reverse()
print('a-',a)
print('a-',a.index(5))
a.insert(2,7)
print('a-',a)
a.reverse()
print('a-',a)
a.remove(1)
print('a-',a)
print('a-',a.pop())
print('a-',a.pop())
print('a-', a)
print('a-',a.count(4))
ex = [8,9]
a.extend(ex)
print('a-', a)

# 삭제 remove, pop, del
while a:
    l = a.pop()
    print(l)
# Keyword - shallow & deep copy
# EX1 - Copy
a_list = [1,2,3,[4,5,6],[7,8,9]] # 변경 가능
b_list = a_list

# 완전히 복사
print('EX1 >', id(a_list))
print('EX1 >', id(b_list))

b_list[2] = 100
print('EX1 >', a_list)
print('EX1 >', b_list)

b_list[3][2] = 100
print('EX1 >', a_list)
print('EX1 >', b_list)
print()
# immutable: int, str, float, bool, unicode... 변경 불가

# EX2 (Shallow Copy)
import copy

c_list = [1,2,3,[4,5,6],[7,8,9]]
d_list = copy.copy(c_list)

print('EX2 >', c_list)
print('EX2 >', d_list)

# id 값 다름
print('EX2 >', id(c_list))
print('EX2 >', id(d_list))

d_list[1] = 100

print('EX2 >', c_list)
print('EX2 >', d_list)

d_list[3].append(1000)
d_list[4][1] = 10000 

# list 값은 그대로 복사
print('EX2 >', c_list)
print('EX2 >', d_list)
print()

# EX3 (Deep Copy)
e_list = [1,2,3,[4,5,6],[7,8,9]]
f_list = copy.deepcopy(e_list)

# id 값 다름
print('EX3 >', id(e_list))
print('EX3 >', id(f_list))
print()

f_list[3].append(1000)
f_list[4][1] = 10000

print('EX3 >', e_list)
print('EX3 >', f_list)
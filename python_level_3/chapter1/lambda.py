# Keyword - lambda, map, filter, reduce
# EX1
cul = lambda a, b , c: a * b + c
print('EX1 >', cul(10, 15, 20))

# EX2
digits1 = [x * 10 for x in range(1,11)]
print('EX2 >', digits1)

result = list(map(lambda i : i ** 2, digits1))
print('EX2 >', result)

def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)

print('EX2 >', list(also_square(digits1)))

# EX3
digits2 = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x % 2 == 0, digits2))
print('EX3 >', result)

def also_even(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)

print('EX3 >', list(also_even(digits2)))

# EX4
from functools import reduce
digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digits3) # 최종 누적 결과 값 
print('EX4 >', result)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)

print('EX4 >', also_add(digits3))
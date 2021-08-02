# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스와 인스턴스 차이 이해
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 접근 가능, 공유
# 인스턴스 변수: 객체마다 별도 존재

# 예제1


class Dog:
  species = 'first dog'

  def __init__(self, name, age):
    self.name = name
    self.age = age

print(Dog)
print()

a = Dog('mikky', 2)
b = Dog('baby', 3)

print(a == b, id(a), id(b))

print('dog1', a.__dict__)
print('dog2', b.__dict__)

print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
  print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)
print()

class SelfTest:
  def func1():
    print('Func1 called')
  def func2(self):
    print(id(self))
    print('Func2 called')

f = SelfTest()

print(id(f))
print()

f.func2()
print()
SelfTest.func1()
SelfTest.func2(f)

# 예제3
class Warehouse:
  stock_num = 0
  def __init__(self, name):
    self.name=name
    Warehouse.stock_num += 1
  
  def __del__(self):
    Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Yoon')

print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)
print()

class Dog2:
  species='firstdog'
  
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def info(self):
    return '{} is {} years old.'.format(self.name, self.age)
  def speak(self, sound):
    return '{} says {}!'.format(self.name, sound)

c = Dog2('july', 4)
d = Dog2('Marry', 3)

print(c.info())
print(d.info())
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))

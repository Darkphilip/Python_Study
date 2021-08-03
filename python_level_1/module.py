# Module: 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
def add(x,y):
  return x+y

def substract(x,y):
  return x - y

def multiply(x,y):
  return x * y

def divide(x,y):
  return x / y

def power(x,y):
  return x ** y

if __name__ == '__main__':
  print('-' * 15)
  print('called!__main__')
  print(add(5,5))
  print(substract(15,5))
  print(multiply(15,5))
  print(divide(15,5))
  print(power(15,5))
  print('-' * 15)

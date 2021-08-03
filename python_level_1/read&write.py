# 파일 읽기 및 쓰기
# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./'), 절대 경로('C:\yoonl\example..')
# 파일 읽기(Read)
# 예제1
f = open('./resource/it_news.txt1','r',encoding = 'UTF-8')
print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
cts=f.read()
print(cts)
f.close()

# 예제2
with open('./resource/it_news.txt','r',encoding = 'UTF-8') as f:
  c = f.read()
  print(c)
  print(iter(c))
  print(list(c))

print()

# 예제3
# read() : 전체 읽기, read(10) : 10Byte
with open('./resource/it_news.txt','r',encoding = 'UTF-8') as f:
  c = f.read(20)
  print(c)
  c = f.read(20)
  print(c)
  f.seek(0,0)
  c = f.read(20)
  print(c)
print()
#  예제4
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt','r',encoding = 'UTF-8') as f:
  line = f.readline()
  print(line)
  line = f.readline()
  print(line)
print()
# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt','r',encoding = 'UTF-8') as f:
  cts = f.readlines()
  print(cts)
  print()
  for c in cts:
    print(c,end='')
print()

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt','w',encoding = 'UTF-8') as f:
  f.write('I love python\n')
with open('./resource/contents1.txt','a',encoding = 'UTF-8') as f:
  f.write('I love python2\n')
# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt','w') as f:
  list = ['Orange\n','Apple\n','Banana\n','Melon\n']
  f.writelines(list)
with open('./resource/contents3.txt','w') as f:
  print('Test Text Write!',file=f)
  print('Test Text Write!',file=f)
  print('Test Text Write!',file=f)
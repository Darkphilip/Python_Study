import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

print(type(pst))

# 타임존 시간 출력

print('Current Date Time in PST =', datetime.now(pst))
print('Current Date Time in IST =', datetime.now(ist))

# 타입 확인
print(type(ist))
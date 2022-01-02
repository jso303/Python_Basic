print(abs(-5))  # |-5| = 5
print(pow(4, 2))    # 4^2 = 4*4 = 16   
print(max(5, 12))   # 가장 큰 값 = 12
print(min(5, 12))   # 가장 작은 값 = 5
print(round(3.14))  # 반올림 = 3
print(round(3.99))  # 반올림 = 4

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 정수 값 생성

# 로또 번호 랜덤 값 6자리 생성하기
for i in range(1,7):
    print(int(random() * 45) +1 )   # 1 ~ 45 이하의 임의의 정수 값 생성


print(randrange(1, 46)) # 1~ 46 미만의 임의의 정수 값 생성
print(randint(1,45))    # 1 ~ 45 이하의 임의의 정수 값 생성
import random as RD  # random 모듈 호출, random을 별칭으로 RD라고 부름 

RD_Num = RD.random()    # 0~1 사이의 값 무작위 추출

print(RD_Num)

RD_int = round(RD_Num*100)

print("랜덤으로 정수 0~100 사이의 값 추출 = " , RD_int)
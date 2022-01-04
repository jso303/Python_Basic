gun = 10

# def checkpoint(soldiers):
#     gun
#     gun = gun - soldiers
#     print("남은 총 : {0}".format(gun))

# 위와 같이 사용시 오류 발생.
# def 안의 gun 은 지역변수로서 초기화가 되지 않았기 때문

def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("남은 총 : {0}".format(gun))
    return gun
    
print("전체 총 : {0}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 3)
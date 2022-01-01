import random as RD

print ("로또 번호 6자리 추첨 : ")

for i in range(1,7):

    RD_Num = round(RD.random()*100)

    while RD_Num > 45:
        if RD_Num >= 90:
            RD_Num = RD_Num - 11;   # 음수가 나오지 않게 하기 위해 처리   
        RD_Num = 90-RD_Num;
    

    
    print(RD_Num, '', end='')


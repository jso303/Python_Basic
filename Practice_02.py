List01 = ['A사업부', 27683, 32577]
List02 = ['B사업부', 24382, 39997]
List03 = ['C사업부', 18335, 21471]
List04 = ['D사업부', 6904, 10818]

F_SALES = []
G_RATE = []
PERFORM = []

for i in range(1,5):
    
    if i == 1:
        List_Name = List01;
    elif i == 2:
        List_Name = List02;
    elif i == 3:
        List_Name = List03;
    elif i == 4:
        List_Name = List04;
        
    F_SALES_L = (List_Name[1]*30)/20    # 30일 판매
    G_RATE_L = round(F_SALES_L/List_Name[2]*100)  # 목표치 달성률      
    F_SALES.append(F_SALES_L)   # for문을 돌리며 F_SALES 리스트안에 F_SALES_L를 하나씩 쌓아둠
    G_RATE.append(G_RATE_L)     # for문을 돌리며 G_RATE 리스트안에 G_RATE_L을 하나씩 쌓아둠

    if G_RATE_L > 99:
        PERFORM_L = 'A'
    elif G_RATE_L > 94 and G_RATE_L <= 99:
        PERFORM_L = 'B'
    elif G_RATE_L > 90 and G_RATE_L <= 94:
        PERFORM_L = 'C'
    elif G_RATE_L > 79 and G_RATE_L <= 90:
        PERFORM_L = 'D'
    else:
        PERFORM_L = 'F'

    PERFORM.append(PERFORM_L)

print(List01[0], '현 판매 : ', List01[1], '판매 목표 : ', List01[2], '30일 판매 : ', F_SALES[0], '목표치 달성률 : ', G_RATE[0], '%', '성과 등급 : ', PERFORM[0])
print(List02[0], '현 판매 : ', List02[1], '판매 목표 : ', List02[2], '30일 판매 : ', F_SALES[1], '목표치 달성률 : ', G_RATE[1], '%', '성과 등급 : ', PERFORM[1])
print(List03[0], '현 판매 : ', List03[1], '판매 목표 : ', List03[2], '30일 판매 : ', F_SALES[2], '목표치 달성률 : ', G_RATE[2], '%', '성과 등급 : ', PERFORM[2])
print(List04[0], '현 판매 : ', List04[1], '판매 목표 : ', List04[2], '30일 판매 : ', F_SALES[3], '목표치 달성률 : ', G_RATE[3], '%', '성과 등급 : ', PERFORM[3])

    
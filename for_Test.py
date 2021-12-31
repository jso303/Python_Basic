T_sum = 0;
for i in range(1,101):
    T_sum = T_sum + i;
    
print(T_sum);

T_sum1 = 0;
for i in range(1,101):
    if i % 2 == 0:
        T_sum1 = T_sum1 + i;
        
print(T_sum1);

print('\n-----------구구단------------\n');

for i in range(1,10):
    for j in range(1,10):
        Result01 = i*j;
        if j == 9:
            print(Result01);
        else:
            print(Result01, '', end='');    # 구구단에서 j가 9인 경우에 문단을 넘기고 9가 아닌 경우에 붙혀서 출력하기 위함
            
            
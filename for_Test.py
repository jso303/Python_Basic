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
            print(Result01, '', end='');    #end='' 는 줄바꿈 없이 이어쓰기
            
            
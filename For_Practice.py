for i in range(1,101):
    if i % 10 == 0:
        print(i);
    else:
        print(i, '', end=''); #end='' 는 줄바꿈 없이 이어쓰기
        
print('-------------3의 배수를 0으로 교체하기---------------');

for i in range(1,101):
    output = i;
    
    if output % 3 == 0:
        output = 0;
        
    if i % 10 == 0:
        print(output);
    else:
        print(output, '', end='');
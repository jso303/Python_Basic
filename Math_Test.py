Cal01 = 2;
Cal02 = 3;

Cal03 = Cal01 + Cal02;
Cal04 = Cal03 * Cal01;

Cal05 = 10 / 4;

print (Cal01, '\n', Cal02, '\n', Cal03, '\n', Cal04, '\n', Cal05);

print('--------------------------------');

List_Cal = [1,2,3,4,5,6,7,8,9,10]
for i in List_Cal :

    print(i,'',end='');
    
    
print('\n--------------------------------');

for i in List_Cal :
    if i % 2 == 0 :
        print('짝', end='');
    else:
        print('홀', end='');
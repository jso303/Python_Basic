Operator = input('연산자를 입력해 주세요:');
Num01 = int(input('피 연산자1 : '));
Num02 = int(input('피 연산자2 : '));

if Operator == '+':
    Result01 = Num01 + Num02;
elif Operator == '-':
    Result01 = Num01 - Num02;
elif Operator == '*':
    Result01 = Num01 * Num02;
elif Operator == '/':
    Result01 = Num01 / Num02;
    
print('연산 결과는 : ', Result01);
    
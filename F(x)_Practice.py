List_Num = [10, 22, 8, 5, 32, 64, 7]

Max_Num = 0;

for i in List_Num:
    if i > Max_Num:
        Max_Num = i;
        
print(Max_Num);

print(max(List_Num))    # 위의 작업을 max 함수가 처리해줌 (가장 큰 숫자 찾기)


Num = 123.456

Round01 = round(Num)
Round02 = round(Num,1)
Round03 = round(Num,2)

print("Round01은 : ", Round01, "\n", "Round02은 : ", Round02, "\n", "Round03은 : ", Round03)
# round 함수는 반올림함수이다. 
# round(X1, X2) ==> X1은 반올림할 숫자, X2는 반올림 할 소수점 아랫 자리수

Num01 = input();
Num02 = input();
Num03 = input();

if int(Num01) >= int(Num02) and int(Num01) >= int(Num03):
    print("양쪽이 모두 참인 경우");
elif int(Num01) >= int(Num02) or int(Num01) >= int(Num03):
    print("둘 중 하나만 참인 경우")
else:
    print("둘 다 참이 아닌 경우")
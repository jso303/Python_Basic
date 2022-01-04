customer = "토르"
index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다")
        
customer = "아이언맨"
index += 1
while index <= 10:
    print("{0}님 커피가 나왔습니다. {1}번째 호출".format(customer, index))
    index += 1
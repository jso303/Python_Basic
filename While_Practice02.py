customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님 커피가 준비되었습니다. 픽업대로 오세요".format(customer))
    person = input("성함이 어떻게 되세요? ")
    if person == customer:
        print("맛있게 드세요")
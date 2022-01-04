# continue : continue 아래의 명령을 실행하지 않고 바로 반복문을 이어 실행

absent = [2, 5] # 결석
no_book = [7]   # 책을 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("책을 안가져온 사람이 있구나 {0}번은 앞에 나와서 손내밀어라".format(student))
        break
    print("{0}번, 일어나서 지문을 읽어봐라".format(student))
cabinet = {3:"유재석", 100:"김태호"}    # 3번에 유재석, 100번에 김태호를 넣는다.
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# print(cabinet[5])
# print("hi")         # 대괄호로 불러오면 값이 없을 시 오류가 발생하고 프로그램 종료

print(cabinet.get(5))   # get으로 불러오면 값이 없을 시 None을 받아옴
print("hi")

print(cabinet.get(5, "사용 가능"))   # 디폴트인 None가 아닌 임의의 값을 설정해 줄 수도 있다.
print("hi")

print(3 in cabinet) # True  캐비넷에 키 3에 해당되는 값이 있는가?
print(5 in cabinet) # False 캐비넷이 키 5에 해당되는 값이 있는가?

cabinet02 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet02)    # 키 값으로 스트링 값도 사용 가능함


# 수정 및 추가 가능
cabinet02["A-3"] = "김종국"
cabinet02["C-24"] = "조세호"
print(cabinet02)

# 삭제
del cabinet02["A-3"]
print(cabinet02)

# key, value 들만 출력
print(cabinet02.keys())
print(cabinet02.values())

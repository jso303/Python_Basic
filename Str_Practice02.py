python = "Python is Amazing"
print(python.lower())   # 문자열을 소문자로
print(python.upper())   # 문자열을 대문자로
print(python[0].isupper)    # 문자열의 해당 문자가 대문자인가 판단
print(len(python))      # 문자열의 길이
print(python.replace("Python", "Java")) # 문자열에서 검색 후 변환 // 첫번째 문자 -> 두번째 문자로 ("Python" => "Java") 

index = python.index("n")   # 문자열에서 해당 문자 탐색
print(index)
index = python.index("n", index + 1)    # 문자열에서 두번째 n을 찾는다.
print(index)

# print(python.index("Java"))   # index로 찾을 때 값이 없다면 오류가 나오고 프로그램 정지
print(python.find("Java"))      # find 로 찾을 때 값이 없다면 무시하고 계속 진행

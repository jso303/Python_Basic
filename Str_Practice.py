Str = "문자열 길이 조절 하기"

C_Str = Str[0:3]    # 문자열 [시작지점 : 종료지점] 으로 조절한다.

print(C_Str)

print("-------------------------")

Str01 = Str[:3]
Str02 = Str[4:6]
Str03 = Str[7:]     # 시작지점과 종료지점은 생략이 가능, 생략 시 처음, 끝이 디폴트로 들어감

print(Str01)
print(Str02)
print(Str03)

Str04 = Str[0]
Str05 = Str[1]
Str06 = Str[2]

print("-------------------------")

print(Str04)
print(Str05)
print(Str06)        # 문자를 하나씩 추출도 가능

print("-------------------------")

Str_Len = len(Str)  # 문자열의 길이 = 12
print(Str_Len)      

print("-------------------------")

Find_Str = Str.find("조")   # find는 찾는 문자열의 위치를 숫자로 반환한다.
print(Find_Str)             # "조" 는 7번째에 위치해 있음.      "문자열 위치 조절하기" 공백도 카운팅되며 0부터 센다.


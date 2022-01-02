# 방법 1 : % 사용

print("나는 %d살 입니다." %28)                      # %d : 숫자
print("나는 %s을 공부하고 있습니다." % "파이썬")      # %s : 문자열
print("Apple 은 %c 로 시작해요." % "A")             # %c : 문자 하나

# 방법 2 : format 사용

print("나는 {}살 입니다.".format(28))                          # 중괄호 사용시 format 안의 내용이 들어감
print("나는 {}색과 {}색을 좋아해요" .format("파란","하얀"))     
print("나는 {0}색과 {1}색을 좋아해요" .format("파란","하얀"))    # 중괄호내에 숫자를 넣으면 format의 리스트 번호에 따라 들어감   
print("나는 {1}색과 {0}색을 좋아해요" .format("파란","하얀"))

# 방법 3 : format에 함수 적용

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 28, color = "파란"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "파란", age = 28))


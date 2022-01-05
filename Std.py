print("Python", "Java", "C++")

print("Python", "Java", "C++", sep = ",")   # spe = 구분 값 설정

print("Python", "Java", "C++", sep = ",", end="?")  # 문장의 끝을 ?으로 함
print("\n")

import sys
print("Python", "Java", file=sys.stdout)    # 표준 출력으로 처리
print("Python", "Java", file=sys.stderr)    # 표준 에러로 처리

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(8) 왼쪽 정렬(8칸 공간확보)  # rjust(4) 오른쪽 정렬(4칸 공간확보)
    
# 은행 대기순번표
# 001, 002, 003, 004, ...
for num in range(1, 21):
    print("대기번호 : ", str(num).zfill(3)) # zfill()는 비는 자리를 0으로 채워줌
    
# 자리 확보 (10자리), 오른쪽 정렬
print("{0:10}".format(500))

# 부호 표기
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

# 3자리 마다 콤마를 찍어주기, 부호 붙이기, 자릿수 확보하기, 빈자리를 ^로 채우기
print("{0:^<+20,}".format(100000000))

# 소수점 출력하기
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지 표시
print("{0:.2f}".format(5/3))

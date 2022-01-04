# 출석번호 1,2,3,4,5 앞에 100을 붙이기로 함 => 101, 102, 103, 104, 105
students = [1,2,3,4,5]
students = [100+i for i in students]
print(students)

# 이름을 길이로 변환
name = ["토르", "아이언맨", "닥터 스트레인지"]
name = [len(i) for i in name]
print(name)
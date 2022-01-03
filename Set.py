# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)   # 중복 불가이므로 뒤의 3은 무시됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python 중 하나라도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# set에 추가
python.add("김태호")
print(python)

# set에서 제거
python.remove("박명수")
print(python)
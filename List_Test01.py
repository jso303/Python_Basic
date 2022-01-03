subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))   # 조세호는 몇번째 칸에 타고 있는가?

subway.append("하하")       # 하하가 다음 칸에 탐
print(subway)

subway.insert(1, "정형돈")  # 정형돈이 유재석, 조세호 사이에 탐
print(subway)

print(subway.pop())
print(subway)           # 뒤에서부터 한명씩 뺌

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

Num_List = [5, 4, 3, 2, 1]
Num_List.sort() # 숫자 크기대로 정렬
print(Num_List)

Num_List.reverse()     # 순서 뒤집기
print(Num_List)

Num_List.clear()        # 리스트 비우기
print(Num_List)

mix_List = ["유재석", 3, True]
print(mix_List)     # 다양한 자료형으로 사용 가능
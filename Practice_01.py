List01 = ['A사업부', 27683, 32577]
List02 = ['B사업부', 24382, 39997]
List03 = ['C사업부', 18335, 21471]
List04 = ['D사업부', 6904, 10818]

Full_Sales01 = (List01[1]*30)/20
Full_Sales02 = (List02[1]*30)/20
Full_Sales03 = (List03[1]*30)/20
Full_Sales04 = (List04[1]*30)/20

Rate01 = round(Full_Sales01/List01[2]*100)  # round 함수는 반올림 함수이다.
Rate02 = round(Full_Sales02/List02[2]*100)
Rate03 = round(Full_Sales03/List03[2]*100)
Rate04 = round(Full_Sales04/List04[2]*100)

List01.extend([Full_Sales01, Rate01])   # .extend 는 해당 리스트에 두개이상의 값을 추가할 때 사용하는 코드이다.
List02.extend([Full_Sales02, Rate02])   # .append 는 해당 리스트에 하나의 값을 추가할 때 사용한다.
List03.extend([Full_Sales03, Rate03])
List04.extend([Full_Sales04, Rate04])

print(List01[0], '현 판매 : ', List01[1], '판매 목표 : ', List01[2], '30일 판매 : ', List01[3], '목표치 달성률 : ', List01[4], '%')
print(List02[0], '현 판매 : ', List02[1], '판매 목표 : ', List02[2], '30일 판매 : ', List02[3], '목표치 달성률 : ', List02[4], '%')
print(List03[0], '현 판매 : ', List03[1], '판매 목표 : ', List03[2], '30일 판매 : ', List03[3], '목표치 달성률 : ', List03[4], '%')
print(List04[0], '현 판매 : ', List04[1], '판매 목표 : ', List04[2], '30일 판매 : ', List04[3], '목표치 달성률 : ', List04[4], '%')

def profile(name="홍길동", age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))
    
# 값이 입력되지 않았다면 설정한 기본값으로 나옴
profile("유재석")
profile()

# 키워드를 지정하여 순서 상관없이 입력 가능
profile(age=25, main_lang="자바", name="김태호")


# 가변인자

def profile02(name, age, *lang):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age, end=" "))
    for lang in lang:
        print(lang, end=" ")
    print()

profile02("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile02("김태호", 25, "Kotlin", "Swift")
# w = 쓰기, 이미 있는 파일에 사용시 덮어쓰기

score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# a = 이어 쓰기

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")
score_file.close

# r = 읽기

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
print("\n")

# readline()는 한줄씩 읽음, 한 줄 읽고 커서는 다음 줄로 이동

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end='')
print(score_file.readline(), end='')
print(score_file.readline(), end='')
print(score_file.readline())
score_file.close()
print("\n")

# 줄의 길이를 모를때 readline() 사용

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:            # 줄이 없을 때 break
        break
    print(line, end='')
score_file.close()
print("\n")

# list 형태로 저장하기

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end='')
    
score_file.close()
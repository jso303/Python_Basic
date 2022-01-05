# pickle 파일도 불러올 수 있음

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))


# with로 파일 처리를 하면 코드가 간단해지고 close 할 필요가 없어 수월하다.

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요\n")
    study_file.write("하루에 2시간씩은 빼먹지 않고 해요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
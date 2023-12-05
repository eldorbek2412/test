#csv(Comma Separated Values)




# import csv
# FILENAME = "users.csv"
# users = [
# ["Ali", 25],
# ["Sobir", 32],
# ["Dilnoza", 14]
# ]

# with open(FILENAME, "w", newline="") as fayl:
#     writer = csv.writer(fayl)
#     writer.writerows(users)

# with open(FILENAME, "a", newline="") as fayl:
#     user = ["Shaxnoza",  18]
#     writer = csv.writer(fayl)
#     writer.writerow(user)



# import csv
# FILENAME = "users.csv"
# users = [
# {"ism": "Ali", "yosh": 25},
# {"ism": "Sobir", "yosh": 32},
# {"ism": "Dilnoza", "yosh": 14}
# ]

# with open(FILENAME, "w", newline="") as fayl:
#     ustunlar = ["ism", "yosh"]
#     writer = csv.DictWriter(fayl, fieldnames=ustunlar)
#     writer.writeheader()
#     # bir qancha qatorlarni yozish
#     writer.writerows(users)
#     user = {"ism": "Shaxnoza", "yosh": 18}
#     # bitta qatorni yozish
#     writer.writerow(user)


# with open(FILENAME, "r", newline="") as fayl:
#     reader = csv.DictReader(fayl)
#     for row in reader:
#         print(row["ism"], "-", row["yosh"])





# Binar fayllar

import pickle

# user1 = {'ism':'ali', 'familiya':'husanov'}
# user2 = {'ism':'alijon', 'familiya':'ganiyev'}

# with open('my_file','wb+') as file:
#     pickle.dump(user1,file)
#     pickle.dump(user2,file)

# with open('my_file','rb') as file:
#     a = pickle.load(file)
#     b = pickle.load(file)
# print(a)
# print(b)



# FILENAME = "user.dat"
# ism = "ali"
# yosh = 25
# with open(FILENAME, "wb") as file:
#     pickle.dump(ism, file)
#     pickle.dump(yosh, file)

# with open(FILENAME, "rb") as file:
#     ism = pickle.load(file)
#     yosh = pickle.load(file)
#     print("Ism: ", ism, "\tYosh: ", yosh)


# FILENAME = "users.dat"
# users = [
# ["Ali", 25, True],
# ["Sobir", 32, False],
# ["Dilnoza", 14, False]
# ]

# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)


# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)
#     print(users_from_file)
#     for user in users_from_file:
#         print("Ism: ", user[0], "\tYosh: ", user[1],
#         "\tUylangan(turmushga chiqan): ", user[2])





#  mkdir() – yangi papka yaratadi;
#  rmdir() – papkani oʻchiradi;
#  rename() – fayl nomini oʻzgartiradi;
#  remove() – faylni oʻchiradi.


# import os
# #Skirpt joylashgan adresga nisbiy yo’l
# os.mkdir("hello")
# # absolyut adres
# os.mkdir("c://somedir")
# os.mkdir("c://somedir/hello")
# os.rename("C://SomeDir/somefile.txt",
# "C://SomeDir/hello.txt")
# os.remove("C://SomeDir/hello.txt")



filename = input ("Faylning yo'lini kiriting:")
if os.path.exists(filename):
    print("ko'rsatilgan fayl mavjud")
else:
    print("Fayl mavjud emas")






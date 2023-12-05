# open(file, mode)


# r (Read) - Fayl o'qish uchun ochadi. Fayl topilmasa, FileNotFoundError
# xatolik qaytaradi;
# w (Write). Fayl yozish uchun ochadi. Agar fayl yo'q bo'lsa, u hosil bo'ladi.
# Bunday fayl allaqachon mavjud bo'lsa, u yangidan yaratiladi va shunga mos
# ravishda eski ma'lumotlar o'chiriladi.
# a (Append). Faylni qayta yozish uchun fayl ochiladi. Agar fayl yo'q bo'lsa, u
# hosil bo'ladi. Bunday fayl allaqachon mavjud bo'lsa, ma'lumotlar oxiridan
# yozish davom ettiriladi.


# meningfaylim = open("salom.txt", "w")
# meningfaylim.close()


# meningfaylim = open("salom.txt", "w")
# meningfaylim.close()


# with open("salom.txt", "w") as somefile:
# somefile.write("Salom Python")


# with open("salom.txt", "w") as fayl:
# fayl.write("salom olam")



# with open("salom.txt", "a") as fayl:
# fayl.write("\nHayr, olam")



# with open("salom.txt", "a") as salom_fayl:
#     print("Salom, olam", file=salom_fayl)



#  readline() - fayldan bir qator o'qiydi;
#  read() - faylning butun tarkibini bir qatorga o'qiydi;
#  readlines() - faylning barcha satrlarini ro'yxatga oladi.


# with open("salom.txt", "r") as fayl:
# for satr in fayl:
# print(satr, end="")



# with open("salom.txt", "r") as fayl:
# str1 = fayl.readline()
# print(str1, end="")
# str2 = fayl.readline()
# print(str2)

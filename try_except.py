# try:
#     sonuc = 5 / 0
# except ZeroDivisionError:
#     print("Sifarga bo'lish mumkin emas.")


# x,y=5,10
# try:
#    y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")


# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# try:
#     sonuc = int("non-integer")
# except TypeError:
#     print("To'g'ri turi kiritilmagan.")



# try:
#     son = int(input("Butun son kiriting: "))
# except ValueError:
#     print("To'g'ri son kiritilmadi.")


# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
# except:
#     print("Butun son kiritmadingiz")
#
# print("Dastur Tugadi!")


# filename = "data.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Bosh fayl tanlang.")


# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}
#
# key="tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")


# BIR NECHTA XATOLARNI USHLASH

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
#     print('ishladi')
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")


# XATOLARNING OLDINI OLISH


# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
#
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")




# try:
#     sonuc = 8 / 4
# except ZeroDivisionError:
#     print("Sifarga bo'lish mumkin emas.")
# finally:
#     print("Dastur tugadi.")


# a = 10
# b = 7
#
# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError as error:
#     print(error)
# finally:
#     print('Finishing up.')



import random
from faker import Faker

for i in range(10):
  a = random.randint(12, 67)
  print(a)

fake = Faker()
for i in range(10):
    my_names =fake.name()
    print(my_names)



# # a = open('test1.txt', 'r')
# # s = 0
# # for i in a:
# #     print(i, end='')
# #
# # a.close()
#
# # ism = input("Ism kiriting:")
# # familiya = input("Familya kiriting:")
# # yosh = input("Yoshingizni kiriting:")
# # with open('test2.txt', 'w') as apple:
# #      apple.write(f"{ism} {familiya} {yosh}")
#
#
#
# # with open('test1.txt', 'r') as my_file:
# #      for i in my_file:
# #           if int(i) % 2 != 0:
# #                with open('test_toq.txt' and 'test2.txt', 'a') as my_file_write:
# #                     my_file_write.write(i.rstrip()+' ')
# #           else:
# #                with open('test_juft.txt', 'a') as my_file_write:
# #                     my_file_write.write(i)
#
# # from faker import Faker
# # fake = Faker()
# # for i in range(50):
# #   with open('test2.txt', 'a') as my_names:
# #     my_names.write(f"{fake.name()}\n")
#
# d = []
# with open('test2.txt', 'r') as my_file_read:
#   for i in my_file_read:
#     a = i.split()
#     d.extend(a)
#     print(d)
#
#
# with open("test1.txt", 'r') as fayl:
#   matn = fayl.readlines()
#
#  # for i in matn:
#     # if i.isdigit():
#     #   print(i)
#   print(matn)


# with open('test1.txt', 'r') as fayl:
#   d = fayl.read().split()
#   for i in d:
#     if i.istitle():
#       print(i)

# with open("file_7.txt", "w") as my_file7, :
#     my_file7.write("Hello my nam465e's John. My phon1e nu0mber is +998952783000")
# with open("file_7.txt", "r") as my_file7:
#   print(my_file7.read())
# with open("file_7.txt", "r") as my_file7:
#   for i in my_file7:
#     sonlar = "Matnda qatnashgan sonlar - "
#     s = 0
#     for j in i:
#       if j.isdigit():
#         sonlar += (j)
#         j = int(j)
#         s += 1
#     print(sonlar)
#     print("Ularning soni", s, "ta")


# with open("lesson2_2.txt", "r") as my_file1:
#     s = set()
#     x = my_file1.read()
#     for i in x:
#         if i.isdigit():
#             s.add(int(i))
# with open("lesson2_2,2.txt", "r") as my_file2:
#     y = my_file2.read()
#     for j in my_file2:
#         if j.isdigit():
#             s.add(int(j))
# with open("lesson2_2new", "w") as my_file3:
#     dic = {}
#     for i in s:
#         dic.update({i:pow(i,2)})
#     dic = str(dic)
#     my_file3.write(dic)



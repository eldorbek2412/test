# a = input("Siz qaysi fayldan sonlarni olmoqchisiz: ")
# b = input("Siz qaysi faylga tub sonlarni yozmoqchisiz: ")
#
# for i in range(100):
#     with open(f"{a}.txt", 'a') as fayl:
#         fayl.write(str(i)+ '\n')
#
# with open(f"{a}.txt", 'r') as fayl_read:
#     for j in fayl_read:
#         d = 0
#         for x in range(1, int(j)+1):
#             if int(j) % x == 0:
#                 d += 1
#         if d == 2:
#             with open(f"{b}.txt", 'a') as fayl:
#                 fayl.write(j)
import csv

# import csv
#
# FILENAME = "users.csv"


# users = [
# ["Ali", 25],
# ["Sobir", 32],
# ["Dilnoza", 14]
# ]
#
#
# with open(FILENAME, "w", newline="") as fayl:
#     writer = csv.writer(fayl)
#     writer.writerows(users)

# with open(FILENAME, "a", newline="") as fayl:
#     user = ["Shaxnoza",  '18']
#     writer = csv.writer(fayl)
#     writer.writerow(user)



# users = [
# {"ism": "Ali", "yosh": 25, 'city':'Buxoro' },
# {"ism": "Ali", "yosh": 25, 'city':'Buxoro' },
# {"ism": "Ali", "yosh": 25, 'city':'Buxoro' },
# {"ism": "Ali", "yosh": 25, 'city':'Buxoro' },
#
# ]


# with open(FILENAME, "w", newline="") as fayl:
#     ustunlar = ["ism", "yosh", 'city']
#     writer = csv.DictWriter(fayl, fieldnames=ustunlar)
#     writer.writeheader()
#     # bir qancha qatorlarni yozish
#     writer.writerows(users)
    # user = {"ism": "Shaxnoza", "yosh": 18}
    # # bitta qatorni yozish
    # writer.writerow(user)


# with open(FILENAME, "r", newline="") as fayl:
#     reader = csv.DictReader(fayl)
#     for row in reader:
#         print(row["ism"], "-", row["yosh"])

# def hd(s):
#     print(('10' * s)[:s])
#
# hd(6)

xodimlar = 'xodim.csv'

xodim = [
    {'ID': 1, 'ism':'Shaxzod', 'age': 23},
    {'ID': 2, 'ism':'elbek', 'age': 24},
    {'ID': 3, 'ism':'bekzod', 'age': 20}
]

with open(xodimlar, 'w', newline='') as fayl:
    ustun = ('ID', 'ism', 'age')
    jadval = csv.DictWriter(fayl, fieldnames=ustun)
    jadval.writeheader()
    jadval.writerows(xodim)

buyurtmalar = 'buyurtma.csv'
buyurtma = [
    {'ID_M': 1, 'sum': 200, 'ID': 2},
    {'ID_M': 2, 'sum': 56, 'ID': 1},
    {'ID_M': 3, 'sum': 210, 'ID': 2},
    {'ID_M': 4, 'sum': 150, 'ID': 3},
    {'ID_M': 5, 'sum': 70, 'ID': 3},
]
with open(buyurtmalar, "w", newline="") as buy:
    ust = ('ID_M', 'sum', 'ID')
    savdo = csv.DictWriter(buy, fieldnames=ust)
    savdo.writeheader()
    savdo.writerows(buyurtma)


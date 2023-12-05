# # d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = {}
# for i in d1:
#     for j in d2:
#         if i == j:
#             d[i] = d1[i] + d2[j]
#
# print(d)
#
#
# # for k,v in dict1.items():
# #     if k in dict2.keys():
# #         dict2[k] += v
# #     elif k not in dict2.keys():
# #         dict2.update({k:v})
# # print(dict2)


# a = ('Assalom').lower()
# d = {}
# for i in a:
#     d[i] = a.count(i)
# print(d)



# a = 'mexanizasiyalashtirilmaganligidandirda'
# d = {}
# for i in a:
#     d[i] = a.count(i)
# a = sorted(d.items(), key=lambda x:x[1])
# d = a.pop()
# print(d)








# b = {' ':' ',
#      'й':'y',
#      'ц':'ts',
#      'у':'u',
#      'к':'k',
#      'е':'e',
#      'н':'n',
#      'г':'g',
#      'ш':'sh',
#      'щ':'sh',
#      'з':'z',
#      'х':'x',
#      'ъ':"'",
#      'ф':'f',
#      'ы':'i',
#      'в':'v',
#      'а':'a',
#      'п':'p',
#      'р':'r',
#      'о':'o',
#      'л':'l',
#      'д':'d',
#      'ж':'dj',
#      'э':'e',
#      'я':'ya',
#      'ч':'ch',
#      'с':'s',
#      'м':'m',
#      'и':'i',
#      'т':'t',
#      'ь':'',
#      'б':'b',
#      'ю':'yu',
#      'ё':'yo'
#      }
#
# a = input("So'z kiriting(kril):")
# d = ''
# for j in a:
#     for i in b:
#         if i == j:
#             d += b[i]
# print(d)


a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
c = 0


# a = (12, 34, 35, 60, 45, 67, 15)
# s = (i for i in a if i % 15 ==0)
# print(tuple(s))


# d = ('olma', 'anor', 'olcha', 'gilos')
# s = {i for i in d if "a" not in i}
# print(s)



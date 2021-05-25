# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:45:38 2021

@author: Shokh-Jakhon
"""
# 1-vazifa
# son = float(input(f'Istalgan son kiriting: '))
# if son%2 == 0:
#     print(f"{son} juft son")
# else:
#     print(f"{son} toq son")

# 2-vazifa
# yosh = int(input(f'Iltimos yoshingizni kiriting: '))
# if yosh <= 4 or yosh >= 60:
#     narx = 0
# elif yosh <= 18:
#     narx = 10000
# elif yosh > 18:
#     narx = 20000
# print(f"Muzeyga kirish chiptasi siz uchun {narx} so'm bo'ladi")

# 3-vazifa
# x = float(input(f"Birinchi sonni kiriting: "))
# y = float(input(f"Ikkinchi sonni kiriting: "))
# if x > y:
#     print(f"{x} > {y}")
# elif x < y:
#     print(f"{x} < {y}")
# else:
#     print(f"{x} = {y}")

# 4-vazifa
# mahsulotlar = ['uzum', 'olma', 'qovun', 'banan', 'gilos', 'behi', 'xurmo', 'olcha', 'pomidor', 'ananas']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1} Mahsulotni kiriting: "))

# for mahsulot in  savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Mahsulot do'konimizda yo'q ")

# 5-vazifa
# mahsulotlar = ['olma', 'non', 'un', 'shakar', 'tuz', 'qovun', 'tarvus', 'banan', 'choynak', 'salat', 'coffee']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1} Mahsulotni kiriting: "))
# bor_mahsulotlar = []
# mavjud_emas = []
# if mahsulotlar:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             bor_mahsulotlar.append(mahsulot)
#         elif mahsulot not in mahsulotlar:
#             mavjud_emas.append(mahsulot)
# l = len(mavjud_emas) #mavjud emas mahsulotlarning soni
# if l > 0:
#     print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mah in mavjud_emas:
#         print(mah)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6-vazifa
# loginlar = ['anvar', 'sanjar', 'bobur', 'umar', 'sobir']
# login = input("Yangi login tanlang: ")
# if login.lower() not in loginlar:
#     print("Xush kelibsiz!")
# else:
#     print("Login band, yangi login tanlang!")

# 7-vazifa
son = int(input("Istalgan butun son kiriting: "))
for n in range(2,son):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi ")
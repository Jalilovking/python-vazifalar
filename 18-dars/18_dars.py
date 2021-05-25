# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:24:16 2021

#18-dars: WHILE VA RO'YXATLAR

@author: Shokh-Jakhon
"""

# buyurtmalar = []

# print('Buyurtmalarni qabul qilish dasturi! ')
# n=1
# while True:
#     savol = f"{n}-buyurtmangizni kiriting: "
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     javob = input(f"Yana buyurtma berasizmi? (ha, yo'q) ")
#     if javob == "ha":
#         n +=1
#     else:
#         break
# print("\nBuyurtmalaringiz ro'yhati: ")
# for buyurtma in buyurtmalar:
#     print(buyurtma.title())
    

# print("e-bazar uchun ro'yhat tayyorlash dasturi! ")
# maxsulotlar = {}
# ishora = True
# while ishora:
#     maxsulot = input("Maxsulot kiriting: ")
#     narx = input(f"{maxsulot.title()}ning narxini kiriting: ")
#     maxsulotlar[maxsulot] = int(narx)
    
#     javob = input("Yana maxsulot kiritasizmi? (ha, yo'q') ")
#     if javob == "yo'q":
#         break
# print("Maxsulotlar ro'yhati: ")
# for maxsulot, narx in maxsulotlar.items():
#     print(f"{maxsulot.title()}ning narxi {narx} so'm")


# maxsulotlar = {
#     'olma':3000,
#     'shaftoli':5000,
#     'nok':7000,
#     'behi':6000,
#     'gilos':10000
#     }
# n=1
# while True:
#     savol = f"{n}-maxsulotni kiriting: "
#     buyurtma = input(savol)
#     if buyurtma in maxsulotlar:
#         print(f"{buyurtma.title()}ning narxi {maxsulotlar[buyurtma]} so'm")
#     else:
#         print("Bizda bunday maxsulot yo'q!")
#     javob = input("Yana buyurtma berasizmi? (ha, yo'q) ")
#     if javob == "ha":
#         n +=1
#     else:
#         break

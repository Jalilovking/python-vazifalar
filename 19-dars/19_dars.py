# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:32:34 2021

#19-dars: FUNCTIONS (FUNKSIYALAR)

@author: Shokh-Jakhon
"""

# def t_yilni_hisobla(ism, yosh):
#     """Ism va yoshini so'rab tugulgan yilini hisoblovchi funksiya"""
#     print(f"{ism.title()} {2021-int(yosh)}-yilda tug'ulgan")
# ism = input("Ismingizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
# t_yilni_hisobla(ism, yosh)



# def kvad_kub_hisobla(son):
#     """Foydalanuvchidan son olib uni kvadrati va kubini hisoblovchi dastur"""
#     print(f"{son} ning kvadrati {son**2} ga teng")
#     print(f"{son} ning kubi {son**3} ga teng")
# son = int(input("Istalgan son kiriting: "))
# kvad_kub_hisobla(son)



# def juft_toq_hisobla(son):
#     """Sonni juft yoki toqligini hisoblovchi funksiya"""
#     if son%2 != 0:
#         print(f"{son} toq23 son")
#     else:
#         print(f"{son} juft son")
# son = int(input("Istalgan son kiriting: "))
# juft_toq_hisobla(son)



# def kattasini_hisobla(son1, son2):
#     """Ikkita sondan kattasini konsolga chiqaruvchi funksiya"""
#     if son1 > son2:
#         print(son1)
#     elif son1 < son2:
#         print(son2)
#     else:
#         print("Ikkila son ham teng! ")
# son1 = float(input("Birinchi sonni kiriitng: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# kattasini_hisobla(son1, son2)



# def daraja_hisobla(x, y):
#     """Sonni darajasini hisoblovchi funksiya"""
#     print(x**y)
# x = float(input("x sonni kiriting: "))
# y = float(input("y sonni kiriting: "))
# daraja_hisobla(x, y)



# def daraja_hisobla(x, y=2):
#     """Sonni darajasini hisoblovchi funksiya"""
#     print(x**y)
# x = float(input("x sonni kiriting: "))
# y = float(input("y sonni kiriting: "))
# daraja_hisobla(x, y)



# def qoldiqsiz_bolish(son):
#     """Sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for n in range(1, 11):
#         if son % n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")

# son = int(input("Istalgan son kiriting: "))
# qoldiqsiz_bolish(son)
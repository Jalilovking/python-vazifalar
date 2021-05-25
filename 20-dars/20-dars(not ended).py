# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:50:08 2021

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

@author: Shokh-Jakhon
"""

# def oraliq(min, max, qadam=''):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         if qadam:
#             min += qadam
#         else:
#             min += 1
#     return sonlar

# min = int(input("Boshlang'ich sonni kiriting: "))
# max = int(input("Oxirgi sonni kiriting: "))
# qadam = int(input("Oraliq sonni kiriting: "))
# print(oraliq(min, max, qadam))



# foydalanuvchilar = []
# def foydalanuvchi_info(ism, familiya, t_joy, t_yil, email='', telefon=None):
#     """Mijozlarni malumotlarini saqlovchi funksiya"""
#     foydalanuvchi = {
#         'ism':ism,
#         'familiya':familiya,
#         'tugulgan_joyi':t_joy,
#         'tugulgan_yili':t_yil,
#         'yosh':2021-t_yil,
#         'email':email,
#         'telefon':telefon
#         }
#     return foydalanuvchi
# while True:
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     t_joy = input("Tug'ulgan joyingizni kiriting: ")
#     t_yil = int(input("Tug'ulgan yilingizni kiriting: "))
#     email = input("Emailingizni kiriting: ")
#     telefon = int(input("Telefoningizni kiriting: "))
    
#     foydalanuvchilar.append(foydalanuvchi_info(ism, familiya, t_joy, t_yil, email, telefon))
    
#     javob = input("Yana boshqa mijozni malumotlarini kiritasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print("Foydalanuvchilar:")
# for foydalanuvchi in foydalanuvchilar:
#     print(f"{foydalanuvchi['ism'].title()} {foydalanuvchi['familiya'].title()}," 
#           f"{foydalanuvchi['yosh']} yoshda, telefoni: {foydalanuvchi['telefon']}")



# def maxni_top(a, b, c):
#     """Uchta sondan kattasi topish funksiyasi"""
#     max = a
#     if b > max:
#         max = b
#     if c > max:
#         max = c
#     return max
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# print(maxni_top(a, b, c))



# def aylanani_hisobla(r):
#     aylana_info = {
#         'radius' : r,
#         'diametr' : r*2,
#         'uzunligi' : r*2*3.14,
#         'yuzi' : r*r*3.14
#         }
#     return aylana_info

# r = float(input("Aylanani radiusini kiriting: "))
# print(aylanani_hisobla(r))



# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar


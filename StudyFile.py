import math
# from random import randint
# class car:
#     pass

# class fire_car:
#     pass

# car1 = car()
# car2 = fire_car()

# # result = isinstance(car1,car)
# # print(result)
# class buterbrod:
#     xleb = 2
#     colbasa = 1
    
#     def __init__(self, cucumbers, salat, cheese, salami):
#         self.cucumbers = cucumbers
#         self.salat = salat
#         self.cheese = cheese
#         self.salami = salami

#     def fall(self,):
#         result = randint(1,4)
#         if result == 1:
#             print("Упал огурцом вниз")
#         elif result == 2:
#             print("Упал салатом вниз")
#         elif result == 3:
#             print("Упал сыром вниз")
#         else:
#             print("Упал салями вниз")
# sandwich = buterbrod(2,1,1,2)
# sandwich.fall()
# haystack =['junk','needle','govno', None]

# for i in haystack:
#     if i == 'needle':
#         print('found the needle at position', haystack.index('needle')+1

# Как работает %
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,224]
# odd_nums = []
# even_nums = []
# for i in nums:
#     if i%2 == 0:
#         even_nums.append(i)
#     else:
#         odd_nums.append(i)
# print(even_nums)
# print(odd_nums)

# Срезы

# items = [1,5,7,15,0]
# print(items[-1::-1])

# a = [1,3,8,7]
# a[1:3] = [0, 0, 0]
# del a[:-2]
# print(a)


# a = 1434322

# for i in a:
#     i <

# Возвращение числа по убыванию его цифр
# string = 1656564
# string_spisok = list(str(string))
# int_spisok = []
# str_spisok = []
# for i in string_spisok:
#     int_spisok.append(int(i))
# int_spisok.sort(reverse=True)
# for i in int_spisok:
#     str_spisok.append(str(i))
# string1 = "".join(str_spisok)
# string1 = int(string1)
# return string1
# Попробовать решить задачу с помощью функции max



# Нахождение площади треугольника по его сторонам
# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# p = (a+b+c)/2
# s = math.sqrt((p*(p-a)*(p-b)*(p-c)))

# if s > 0:
#     print('True')
# else:
#     print('False')
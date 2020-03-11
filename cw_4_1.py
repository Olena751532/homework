# Cереднє арифметичне значення довільної кількості чисел.

def ser(*numlist):
    print(sum(numlist)/len(numlist))
ser(31, 11, 15, 61)


# Повернення абсолютного значення числа

type = int(input('Type number: '))
print(abs(type))

#Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)
from functools import reduce

def pryamokut(a, b):
    """Обчислює площу прямокутника"""
    return a*b
a = float(input("a = "))
b = float(input("b = "))
print("Площа прямокутника = ", pryamokut(a,b))


def trykut(a, b, c):
    """Обчислює площу трикутника"""
    p = (a + b + c) / 2.0  # Полупериметр
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("Площа трикутника = ", trykut(a, b, c))

def kolo(r):
    s = 3,14 * r**2
    return s
r = float(input("r = "))
print("Площа кола = ", kolo(r))
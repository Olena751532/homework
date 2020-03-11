# Максимальне/мінімальне
quantity = [int(input()) for i in range(int(input('How long is your list?: ')))]
print(min(quantity), max(quantity))

#2.  В інтервалі від 1 до 10 визначити числа
# парні, які діляться на 2,
# непарні, які діляться на 3,
#числа, які не діляться на 2 та 3.

a = []
b = []
c = []

for x in range(1, 11):

     # print(x, 'is even multiple of 2')
     if x % 2 == 0:
          a.append(x)

     # print(x, 'is an odd multiple of 3')
     elif x % 3 == 0:
          b.append(x)

     # print(x, 'not divisible by 2 and 3')
     else:
          c.append(x)

print(a)
print(b)
print(c)



# Факторіал числа без рекурсивного виклику функції

number = int(input("Enter number more then 0  "))
factorial = 1
for i in range(1, number + 1):
    factorial*= i
print("Factorial", number, "equal", factorial)

 #  Напишіть скрипт, який перевіряє логін, який вводить користувач.
#Якщо логін вірний (First), то привітайте користувача.
#Якщо ні, то виведіть повідомлення про помилку.
#(використайте цикл while)

login = input("")
while login != "First":
     input("Try again ")
print("You are right ")



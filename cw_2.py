# Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше
a = int(input("Input the number a="))
b = int(input("Input the number b="))
if a <= b:
    min_value, max_value = a, b
else:
    min_value, max_value = b, a

st = "The number a={0} is minimal number,the number b={1} is maximum number".format(min_value, max_value)
print(st)

# Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.
a = int(input())
if a % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

# Написати скрипт, який обчислить факторіал введеного числа.

n = int(input())
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)

# Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою.

spysok = [22, 1, 3, 15]
i = 0
for value in spysok:
    spysok[i] = float(value)
    i = i+1
print(spysok)



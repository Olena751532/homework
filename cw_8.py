#1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
try:
    a = int(input())
    if a %2 == 0:
        print("a - парне")
    else:
        print("a - непарне")
        raise ValueError("дані некоректні")
except ValueError as a:
    print("a is ", a)
#2.  Напишіть програму, яка пропонує користувачу ввести свій вік,
# після чого виводить повідомлення про те чи вік є парним чи непарним числом.
# Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
#  Головний код має викликати функцію, яка обробляє введену інформацію.


try:
    age = int(input("Enter your age: "))
    if age<0:
        raise ValueError("Error!, U not born yet")
    if age>170:
        print ("Hmm, Are u sure? I dont know any people with this age. Please try again")
    if age%2==0:
        print ("your age even")
    else:
        print ("your age odd")
except ValueError:
    print ("ValueError!!!")
except TypeError:
    print ("TypeError!!!")
except SyntaxError:
    print ("SyntaxError!!!")
finally:
    print ("Try again")


# Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, передбачити випадок ділення на нуль,
#випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.

def divide(x, y):
    try:
        result = int(input(x / y))
    except ZeroDivisionError:
        print("division by zero!")
    except SyntaxError:
        print("syntax is wrong")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(x, y)


# 4.  Написати  програму, яка аналізує введене число та в залежності
# від числа видає день тижня, який відповідає цьому числу
# (1 це Понеділок, 2 це Вівторок і т.д.) . Врахувати випадки введення
# чисел від 8 і більше, а також випадки введення не числових даних.
week={1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
num = int(input("Enter the number of day: "))
try:
    user_input = int(input("Enter number of the day: "))
    print(week[user_input])

except KeyError:\
    print(f"There`s no {user_input}`s day in normal life")
except ValueError:\
    print("ValueError!!!")
except SyntaxError:\
    print("SyntaxError!!!")
except TypeError:\
    print("Typer error")
finally:
    print("Ended")
'''
Creating user-defined variables
-----------------------------------
Создание задаваемых пользователем переменных
'''

while True:
    try:
        x = float(input("enter first number "))
        y = int(input("enter second number "))
    except:
        print("that's not a number!\nTry again")
        continue
    break

"""
1st solution way
--------------------------------------
1й способ решения (через оператор **)
"""
def my_func(x, y): #задаём функцию
    while True:
        try:
            answer = x ** y
            print(f"Answer is {answer}")
            
        except ZeroDivisionError: #обработка деления на ноль
            print("You tried to divide by zero :(")
        break


"""
2nd solution way
-----------------------------------------
2й способ решения (через циклы)
"""

def my_func1(x, y):
    while True:
        a = 1 #промежуточный результат
        i = 1 #счётчик
        if y > 0: #решение, когда степень положительна
            for i in range(0, y):
                a = a * x
                i += 1
            print(f"Answer is {a}")
            break
        elif y == 0: #решение, когда степень равна нул.
            print(f"Answer is {a}")
            break
        elif y < 0: #решение, когда степень отрицательна (КАК В УСЛОВИИ ЗАДАЧИ)
            try:
                for i in range(0, abs(y)):  # abs() - модуль от числа
                    a = a * (1 / x)
                    i += 1
                print(f"Answer is {a}")
            except ZeroDivisionError: #обработка деления на ноль
                print("You tried to divide by zero :(")
            break
        break

'''
Passing user-defined variables to both functions as arguments
----------------------------------------------------------------
Передача заданных пользователем переменных обеим функциям в качестве
аргументов
'''

my_func(x, y)
my_func1(x, y)
'''
Сreate a function that performs division
-----------------------------------------
Создание функции, осуществляющей деление
'''
def division(a, b):
    while True:
        try:
            result = a / b
            print(f"Result of division {a} and {b} is {result}") # вывод результата деления
            return result #возвращение функцией результата деления для возможности использования его в дальнейшем
        except ZeroDivisionError: # обработка деления на ноль
            print("You cannot divide by zero!\nPlease try again")
        break
'''
Insert two user-defined numbers
----------------------------------------
Ввод двух задаваемых пользователем чисел
'''
while True:
    try:
        a = float(input('Insert first number: '))
        b = float(input('Insert second number: '))
    except:
        print("It is not a number!\nPlease try again") #обработка неверного значения (например, введена буква)
        continue
    break
'''
Function call
-----------------
Вызов функции
'''

division(a,b)
'''
Creating a function that displays information about users in 
one line
-------------------------------------------------------------
Создание функции, выводящей информацию о пользователе одной
строкой
'''

def collect_userdata(**kwargs): # в качестве аргумента задаётся неопределённое количество именованных параметров
    for i in kwargs.values():
        print(i, end=' ')
        
'''
Passing user-supplied parameters to a function
------------------------------------------------------
Передача пользовательских параметров в функцию
'''
collect_userdata(name = input("Insert your name: "), # Имя
surname = input("Insert your surname: "), # Фамилия
byear = input("Insert your birth year: "), # Год рождения
city = input("Insert your city: "), # Город
email = input("Insert your email: "), # электронная почта
phone = input("Insert your phone number: ")) # телефон
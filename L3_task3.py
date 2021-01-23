"""
Creating a function that calculates the sum of the maximum 
two of the three entered arguments and displays result on 
the screen
-----------------------------------------------------------
Создание функции, высчитывающей сумму двух наибольших из 
трёх принятых аргументов и выводящей результат на экран
"""
def my_func(a, b, c):
    cort = (a, b, c)
    for i, item in enumerate(cort):
        if min(cort) == cort[i]:
            summa = cort[i - 1] + cort[i - 2] #i-1 и i-2 вместо i-1 и i+1 чтоб не выйти за границы cort()
    print(summa)

############################################################
"""
Лирическое отступление:) В задаче не указано, какие именно
данные будет складывать пользователь (строки или числа),
поэтому я решил дать пользователю выбрать, что именно
он будет складывать :)
"""
############################################################


"""
Creating user-define variables
-----------------------------------
Создание переменных, задаваемых пользователем
"""
while True:
    type_of_data = input('What type of data summ do you want to find? (string/number): ')
    if type_of_data.lower() == 'string':
        a = input('Insert first element: ')
        b = input('Insert second element: ')
        c = input('Insert third element: ')
        break
    elif type_of_data.lower() == 'number':
        while True:
            try:
                a = float(input('Insert first element: '))
                b = float(input('Insert second element: '))
                c = float(input('Insert third element: '))
            except:
                print("That's not a number!\nPlease try again")
                continue
            break
        break
    else:
        print("Are you serious?\nPlease learn to read and try again")
        continue
    break

"""
Passing user-defined variables to the function as arguments
------------------------------------------------------
Передача заданных пользователем переменных в функцию в
качестве аргументов
"""
my_func(a, b, c)
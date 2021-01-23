"""
Creating of a function that counts the sum of the items in a list and also processes input of a non-digit character
-------------------------------------------------------------------------
Создание функции, считающей сумму элементов списка, а также обрабатывающей ввод символа, не являющегося цифрой
"""
summ = 0
def summ_from_input(args):
    #print(args)
    summ1 = summ
    while True:
        try:
            for element in args:
                summ1 = summ1 + float(element)
        except:
            print("You entered a no-digit symbol. \nThe program will display the sum of the numbers entered before and close")
            global Flag  
            Flag = False #смена значения глобальной переменной Flag для остановки программы
        break
    return summ1

"""
Applying a previously created function to a user-entered string
------------------------------------------------------------------
Применение созданной ранее функции к строке, вводимой пользователем

"""
Flag = True # создание переменной, являющейся "флагом" для остановки работы программы
args = [] #создание пустого списка, заполняемого пользователем
while Flag == True:
    try:
        args += input("Please insert string splitted by space\n(If you want to exit enter any no-digit symbol (eg. 'a', '$' etc.): ").split()
        #print(args)
        print(f"The sum of the numbers you entered: {summ_from_input(args)}")
    except:
        Flag = False
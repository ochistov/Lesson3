'''
Creating of a function that changes the first character of a string 
from lowercase to uppercase
----------------------------------------------------------------
Создание функции, изменяющей первый символ строки со строчной буквы на заглавную
'''
def int_func(string):
    string1 = string.capitalize()
    return string1 # функция возвращает значение string1

"""
Receiving a string consisting of words from the user, converting the string to a list, 
applying the int_func() function to each element of the list, displaying the result on the screen
--------------------------------------------------------------------------------------------------
Получение от пользователя строки, состоящей из слов, преобразование строки в список, применение функции
int_func() к каждому элементу списка, вывод результата на дисплей
"""
users_words = input("Insert some lowcase words splitted by space: ").lower().split()
print(f"Here is you words each starts from uppercase letter: {' '.join((str(int_func(word)) for word in users_words))}")
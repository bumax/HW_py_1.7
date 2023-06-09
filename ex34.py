# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


in_str = input("Введите строку: ")
# in_str = "пара-ра-рам рам-пам-папам па-ра-па-да"

# Определяем функцию, которая считает гласные в слове
def count_syllables(word):
    vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
    res = list(filter(lambda x: x in vowels, word))
    return len(res)

# Считаем гласные во всех словах, потом полученный список преобразовываем во множество и смотрим размер, 
# если он равен 1, то значит во всех словах одинаковое количество гласных
if len(set(map(count_syllables,in_str.lower().split()))) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
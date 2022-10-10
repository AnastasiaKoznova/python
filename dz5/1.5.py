#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
some_words = ['ночь', 'дом', 'Забвение', 'Забава', 'кот', 'автомобиль']

for i in some_words:
    if 'абв' in i.lower():
        some_words.remove(i)


print(some_words)

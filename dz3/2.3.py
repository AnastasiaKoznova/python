#Напишите программу, которая найдёт произведение пар чисел списка (C4писок создаем как в предыдущем задании). Парой считаем первый и последний элемент, второй и предпоследний и т.д.
n = int(input('Укажите размер списка:'))
my_list = []
for i in range(n):
    my_list.append(i)
print(my_list)
newList = []
for i in range((len(my_list) + 1) // 2):
    newList += [int(my_list[i]) * int(my_list[-i-1])]
print(f'Произведение пар чисел списка = {newList}')
#Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from curses.ascii import isdigit
from ipaddress import summarize_address_range


N= [i for i in range(int(input('Введите число:')))]
list=N[1::2] #делаем срез (1-с элемента с индексом 1, шаг 2)
print(sum(list))



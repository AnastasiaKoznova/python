#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from tkinter import N


n=int(input("Введите число"))
i=2 #первое простое число
list=[]
first=n
while i<=n:
    if n%i==0:
        list.append(i)
        n//=i
        i=2
    else:
        i+=1
print(f"простые множители числа {first}  приведены в списке {list}")

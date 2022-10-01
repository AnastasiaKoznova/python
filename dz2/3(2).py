#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
N=int(input("Введите число")) #int для введения целого числа
def array(number):
    list=[]
    for i in range (1, number+1): 
        list.append((1+1/n)**n)
        return list
print(array(N))

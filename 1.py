#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

N=int(input('Ввеите число'))
print(N)
for i in range (-N+1,N+1):
    print(i)

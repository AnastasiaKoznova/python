#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x=int(input('Введите значение x='))
y=int(input('Введите значение y='))
z=int(input('Введите значение z='))
if (not(x or y or z))==(not x and (not y) and ( not z)):
    print('true')
else:
    print('false')

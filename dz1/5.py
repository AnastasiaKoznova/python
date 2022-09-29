#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from ast import For


x=int(input('Введите значение x='))
y=int(input('Введите значение y='))
z=int(input('Введите значение z='))
if (not(x or y or z))==(not x and (not y) and ( not z)):
    print('true')
else:
    print('false')

# 2 вариант решения (более правильный). не нужно вводить конкретную переменную. (тройной цикл)
trigger=True #флаг(переменная) , (если условие не сработает, то он меняет переменную тру на фолс)
for x in [True, False]:
    for y in [True,False]:
        for z in [True, False]:
            if(not(x or y or z))!=(not x and (not y) and ( not z)):
                print ('Не верно')
                trigger=False
                break
if trigger: print("Выражение верно")
 
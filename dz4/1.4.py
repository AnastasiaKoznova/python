# # Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141

number=float(input('Введите любое число'))
d=float(input('Введите заданную точность'))
new_number=int(number/d) #получаем целочисленное число
print('При заданной точности число=', new_number*d)
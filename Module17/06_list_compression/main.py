import random

N = int(input('Количество чисел в списке: '))
initial = [random.randint(0, 2) for i in range (N)]

print('Список до сжатия: ', initial)

final = [i for i in initial if i]

print('Список после сжатия: ', final)
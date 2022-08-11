import random

N = int(input('Количество палок: '))
K = int(input('Количество бросков: '))

stik = ['I' for i in range(N)]

for i in range (1, K + 1):
    Right_i = random.randint(1, N + 1)
    Left_i = random.randint(1, Right_i)
    print('Бросок', i, 'сбиты палки с номера ', Left_i, 'по номер ', Right_i)

for i in range(Left_i, Right_i + 1):
    stik[i - 1] = '.'

print(stik)
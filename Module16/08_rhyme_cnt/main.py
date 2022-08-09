N = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке: '))

print('Значит, выбывает каждый', k, '-й человек')

numbers = list(range(1, N + 1))
stop = 0

for i in range (N - 1):
    print('Текущий круг людей: ', numbers)
    start = stop % len (numbers)
    stop = (start + k - 1) % len(numbers)
    print('Начало счёта с номера ', numbers[start])
    print('Выбывает человек под номером', numbers[stop])
    numbers.remove(numbers[stop])

print('Остался человек под номером', numbers)
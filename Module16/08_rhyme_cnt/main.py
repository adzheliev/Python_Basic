N = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке: '))

print('Значит, выбывает каждый', k, '-й человек')

numbers = list(range(1, N + 1))
i = 0

while len(numbers) > 1:
    print('Текущий круг людей: ', numbers)
    print('Начало счёта с номера ', numbers[i])
    print('Выбывает человек под номером', numbers[(k % len(numbers)) - 1])
    numbers.pop((k % len(numbers) - 1))
    print (numbers)
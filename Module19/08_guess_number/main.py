N = int(input('Введите максимально число: '))
fromonetomax = {number for number in range (1, N + 1)}

while True:
    numbers = input('Нужное число есть среди вот этих чисел: ')
    if numbers != 'Помогите!':
        numbers = set(numbers.split())
        numbers = {int(i) for i in numbers}
        response = input('Ответ Артёма: ')
        if response == 'Нет':
            fromonetomax = fromonetomax.symmetric_difference(numbers)
        elif response == 'Да':
            fromonetomax = numbers
    else:
        print('Артём мог загадать следующие числа: ',fromonetomax)
        break




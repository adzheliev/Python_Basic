def slicer(posl, number):
    posl = list(posl)
    newlist = []
    for index, value in enumerate(posl):
        if value == number:
            newlist = posl[index:]
            break
    for index, value in enumerate(newlist):
        if value == number:
            newlist = newlist[:index + 1]
            break
    newlist = tuple(newlist)
    return newlist


tup = tuple(input("Введите последовательность чисел кортежа: "))
element = int(input('Введите случайный элемент: '))
a = slicer(tup, element)
print('Ответ в консоли:', a)

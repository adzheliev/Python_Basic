list1 = []
list2 = []

for i in range (1, 4):
    print('Введите', i, '-e число для первого списка: ', end='')
    number1 = int(input())
    list1.append(number1)

for i in range (1, 8):
    print('Введите', i, '-e число для второго списка: ', end='')
    number2 = int(input())
    list2.append(number2)

print('Первый список: ', list1)
print('Второй список: ', list2)

list1.extend(list2)
new_list = list(set(list1))

print('Новый первый список с уникальными элементами: ', new_list)
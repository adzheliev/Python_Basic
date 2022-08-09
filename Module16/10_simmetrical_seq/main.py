N = int(input('Кол-во чисел: '))

number_list = []
reverse_number_list = []

for i in range (N):
    number = int(input('Число: '))
    number_list.append(number)

print('Последовательность: ', number_list)

for i in range(len(number_list) - 1, -1, -1):
    reverse_number_list.append(number_list[i])

while True:
    if number_list[len(number_list) - 1] == reverse_number_list[0]:
        reverse_number_list.remove(reverse_number_list[0])
    else:
        break
print("Нужно приписать чисел: ", len(reverse_number_list))
print("Сами числа: ", reverse_number_list)

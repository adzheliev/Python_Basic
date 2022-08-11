string = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите текст: ').lower()
step = int(input('Введите сдвиг: '))

index_list = ''

for i in text:
    if i == ' ':
        string[new_position] == ' '
    else:
        position = string.find(i)
        new_position = (position + step) % len(string)
    index_list += string[new_position]

print(index_list)

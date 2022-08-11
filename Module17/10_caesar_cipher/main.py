string = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите текст: ').lower()
step = int(input('Введите сдвиг: '))

index_list = ''

for i in text:
    if i == ' ':
        index_list += ' '
    else:
        position = string.find(i)
        new_position = (position + step) % len(string)
        index_list += string[new_position]

print(index_list)

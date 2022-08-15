string = input('Введите строку: ').split()

print('Самое длинное слово: ', max(string, key=len))
print('Длина этого слова: ',len(max(string, key=len)))
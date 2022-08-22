def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст: ')
hist = histogram(text)

print('Оригинальный словарь частот')

for i_sym in hist.keys():
    print(i_sym, ':', hist[i_sym])

inverted_dict = dict()
for i in range(1, max(hist.values()) + 1):
    i_list = []
    for i_sym_key, i_sym_value in hist.items():
        if i_sym_value == i:
            i_list.append(i_sym_key)
    inverted_dict[i] = i_list

print('')
print('Инвертированный словарь частот:')

for i in inverted_dict.keys():
    print(i, ':',inverted_dict[i])

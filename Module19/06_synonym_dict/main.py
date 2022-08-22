N = int(input('Введите количество пар слов: '))

pairs_dict = dict()

for i in range(1, N + 1):
    print(i,'-я пара: ',end='')
    pair = input().split(' — ')
    pairs_dict[pair[0]] = pair[1]

while True:
    word = input('Введите слово: ')
    if word.title() not in pairs_dict.keys() and word.title() not in pairs_dict.values():
        print('Такого слова в словаре нет.')
    else:
        if word.title() in pairs_dict.keys():
            print('Синоним: ',pairs_dict[word.title()])
        elif word.title() in pairs_dict.values():
            rev = [key for key, value in pairs_dict.items() if value ==  word.title()]
            print('Синоним: ', rev[0])
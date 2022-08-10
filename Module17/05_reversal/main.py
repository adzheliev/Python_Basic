string = input('Введите строку: ')

firsth = string.index('h') + 1
secondh = string.rindex('h')

new = string[firsth:secondh]

print('Развёрнутая последовательность между первым и последним h: ', new[::-1])
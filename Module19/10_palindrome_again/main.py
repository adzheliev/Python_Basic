import itertools

string = input('Введите строку: ')
count = 0
for i in list(itertools.permutations(string)):
    if i == tuple(reversed(i)):
        count += 1

if count > 0:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')



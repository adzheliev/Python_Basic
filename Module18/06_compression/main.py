import itertools

string = input('Введите строку: ')

newstring =''

for k, g in itertools.groupby(string):
    newstring = newstring + (k + str(sum(1 for _ in g)))

print(newstring)



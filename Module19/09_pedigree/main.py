num = int(input('Введите количество человек: '))

tree = dict()
family = dict()

for i_index in range(num - 1):
    couple = input(f'{i_index + 1} пара: ').split()
    tree[couple[0]] = couple[1]

for child, parent in tree.items():
    if parent in tree:
        family[child] = family[parent] + 1
    else:
        family[parent] = 0
        family[child] = 1

for i_key in sorted(family):
    print(i_key, family[i_key])


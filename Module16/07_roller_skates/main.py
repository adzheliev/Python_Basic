N = int(input('Количество коньков: '))

rollers = []
people = []

for i in range (1, N + 1):
    print('Размер', i, '-й пары: ', end='')
    shoe = int(input())
    rollers.append(shoe)

K = int(input('Количество людей: '))

for i in range (1, K + 1):
    print('Размер ноги', i, '-го человека: ', end='')
    size = int(input())
    people.append(size)

count = 0
rollers.sort()
people.sort()


for i in people:
    for l in rollers:
        if l >= i:
            rollers.remove(l)
            count += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики: ', count)
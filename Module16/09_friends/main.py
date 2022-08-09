N = int(input('Кол-во друзей: '))
k = int(input('Долговых расписок: '))

friends = [0] * N

for i in range (1, k + 1):
    print(i,'-я расписка')
    debitor = int(input ('Кому: '))
    creditor = int(input('От кого: '))
    money = int(input('Сколько: '))
    friends[debitor - 1] -= money
    friends[creditor - 1] += money

print('Баланс друзей:')
for i in range (1, len(friends) + 1):
    print(i,':',friends[i-1])
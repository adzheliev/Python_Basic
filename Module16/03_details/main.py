shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

part = input('Название детали: ')

total = 0
summ = 0

for i in shop:
        if i[0] == part:
                summ += i[1]
                total += 1

print('Кол-во деталей - ', total)
print('Общая стоимость — ', summ)

